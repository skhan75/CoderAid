# SQL vs NOSQL

## SQL joins have bad time complexity

The first problem with RDBMS stems from the join operation in SQL

In a SQL join operation, your relational database is combining results from two or more different tables. Not only are you reading quite a bit more data but you're also comparing the values to the other to determine which values should be returned.

Your results will vary based on the type of JOIN you're using as well as the indexes on your tables, but you may be getting linear time `O(M+N))` or worse.

These CPU intensive operations will work fine during testing or while your data is small. As your data grows, you will start to see CPU usage rise and query performance fall. As such you may want to scale up your database. This leads us to the next issue with relational database.

## It's difficult to horizontally scale an RDBMS

The second problem with RDBMS is that they are difficult to scale horizontally.
There are two ways to scale a database:

- **Vertical Scaling**, by increasing the CPU or RAM of your existing database machine(s), or
- **Horizontal Scaling** by adding additional machines into your database cluster, each of which handles a subset of the total data.

At lower scale, there is probably not a huge difference between vertical and horizontal scaling.

However, you will eventually hit the limits of vertical scaling. Your cloud provider won’t have a box big enough to handle your growing database. At this point you may want to consider horizontal scaling. Now you’re running into bigger problems.

The whole point of horizontal scaling is that each machine in your overall cluster will only handle a portion of the total data. As your data continues to grow, you can add additional machines to get the amount of data on each machine relatively steady.

### Problems

- Horizontal scaling is tricky with a relational database, as there is often not a clear way to split up the data. You'll often want to store all results from a given table on the same machine so that you can correctly handles uniqueness and other requirement.

- If you split across different machines, now your SQL joins require a network request in addition to the CPU computation.

- Horizontal scaling works best when you can shard the data in a way that a single request can be handled by a single machine. Jumping around multiple servers and making requests between them will result in slower performance.

**For read heavy systems, it is straightforward to provision multiple read-only replicas (with master slave replication), but for write-heavy systems, the only option often times is to vertically scale the database up, which is generally more expensive than provisioning additional servers.**

- By increasing the number of read replicas, a _trade-off_ is made between consistency and availability. Having more read servers leads to higher availability, but in turn sacrifices consistency (provided that updates are asynchronous) since there is a higher chance of accessing stale data.
- Its not impossible to horizontally scale write-heavy SQL databases, looking for _Google Spanner_ and _Cockroach DB_, but its a very challenging problem and makes for a highly complex database architecture.

## Relational queries are unbounded

The third problem with RDBMS is that, by default, SQL queries are unbounded, meaning there is no inherent limit to the amount of data you can scan in a single request to your database, which also means there;s no inherent limit to how a single bad query can gobble up your resources and lock up your database.
A simple example would be a query like `SELECT * FROM large_table` — a full table scan to retrieve all the rows. But that’s pretty obvious to see in your application code and less likely to consume all your database resources.

A more nefarious example would be something like the following:

```sql
SELECT user_id, sum(amount) AS total_amount
FROM orders
GROUP BY user_id
ORDER BY total_amount DESC
LIMIT 5
```

The example also examines the `orders` table in an application to find the top 5 users by the amount spent. Application developer might think this isn't an expensive operation, as its only returning 5 rows. But think of the steps involved in this operation:

- Scan the entire `orders` table
- Group orders by the user_id and sum the order amount by user to find a total.
- Return the top 5 results.
  This is expensive on a number of different resources -- CPU, memory, and disk. And it's completely hidden from the developer.

Aggregations are bear traps for the unwary, ready to take down your database right when you hit scale.

## How NoSQL databases handle these relational problems

In the previous section, we saw how relational databases run into problems as they scale. In this section, we’ll see how NoSQL databases like DynamoDB handle these problems. Unsurprisingly, they’re essentially the inverse of the problems listed above:

- DynamoDB does not allow joins;
- DynamoDB forces you to segment your data, allowing for easier horizontal scaling; and
- DynamoDB puts explicit bounds on your queries.

Again, let’s review each of these in order.

### How NoSQL databases replaces joins

The canonical way to model your data in a relational database is to [normalize](https://en.wikipedia.org/wiki/Database_normalization) your entities. Normalization is a complex subject that we won’t cover in depth here, but essentially you should avoid repeating any singular piece of data in a relational database. Rather, you should create a canonical record of the data and reference this canonical record whenever needed.

When a design decision is involved, we often need to decide the extent to which tables should be **Normalized**. Generally speaking, normalized tables have:

- Simpler schema
- More standardized data
- Carry less redundancy

However, a proliferation of smaller tables also means that tracking data relations requires:

- More diligence
- Querying patterns also become more complex (more `JOINS`)

For example, a customer in an e-commerce application may make multiple orders over the course of the year. Rather than storing all customer information on the order record itself, the order record would contain a `CustomerId` property which would point to the canonical customer record.

![https://user-images.githubusercontent.com/6509926/71933607-34c66b00-3168-11ea-940f-1dc50fe5bf68.png](https://user-images.githubusercontent.com/6509926/71933607-34c66b00-3168-11ea-940f-1dc50fe5bf68.png)

In the example above, Order #348901 has a `CustomerId` property with a value of `145`. This points to the record in the Customers table with an `Id` of `145`. If Customer #145 changes something about him, such as his name or address, the Order doesn't have to make corresponding changes.

However, as noted above, this flexibility comes at a cost — joins require a lot of CPU and memory. Thus, to get rid of SQL joins, NoSQL needs to handle the three benefits of joins:

1. Flexible data access
2. Data integrity
3. Storage efficiency

Two of these are handled by specific _trade-offs_, while the third is less of a concern anymore.

### How NoSQL compensates for the benefits of JOINS

- NoSQL databases avoid the need for flexibility in your data access by requiring you to do planning up front. How will you read your data? How will you write your data? When working with a NoSQL database, you need to consider these questions thoroughly before designing your data model. Once you know your patterns you can design your database to handle these questions specifically.
- The second trade off NoSQL database is _data integrity_ is now a n application level concern. While JOINS would allow you for a "write once, refer many" pattern for referenced items, you may need to denormalize and duplicate data in your database. For pieces of data that is unchanging, this is not a problem. But for mutable entities like `name` or `price` you may find yourself updating multiple records in the event of a change. Denormalization of NoSQL databases leads to _Eventual Consistency_, which means it may be a possibility that, if there is a change in data, there may be a possibility that you may retrieve stale data, but its ensured that data will become consistent eventually.

### Why are JOINS so much important

It is much easier to query from a denormalized table(aka wide table), because all of the metrics and dimensions are already pre-joined.

### Some issues with NoSQL databases

- Given their large sizes, however, data processing for wide tables is slower and involved more upstream dependencies. Maintenance of data tables are more difficult, because there the unit of work is not as modular.
- NoSQL databases are less storage efficient that their relational counterpart, but its mostly not a concern. When RDBMS were designed, storage was at more of a premium than compute. This is no longer the case -- storage prices have dropped to the floor, while Moore's Law is slowing down. Compute is the most valuable resource in your systems, so it makes sense optimize for compute over storage.

### Why NoSQL databases can scale horizontally

The main reason relational databases cannot scale horizontally is due to the flexibility of the query syntax. SQL allows you to add all sorts of conditions and filters on you data such that its impossible for the database system to know which pieces of your data will be fetched until your query is executed.

As such, all data needs to be kept local on the same node, to avoid cross machine network calls when executing a query.

**Remedy**: To avoid this problem, NoSQL databases require you to split up your data into smaller segments and perform all queries within one of these segments. This is common across all NoSQL databases. In DynamoDB and Cassandra, its called _partition key_. In MongoDB, its called _shard key_.

**The easiest way to think of NoSQL database is a _hash table_ where the value of each key in the hash table is a _B-Tree_. The partition key is the key in the hash table and allows you to spread data across an unlimited number of nodes.**

Without table relationships, data in NoSQL databases can be sharded across different data stores allowing for distributed databases. This makes horizontal scaling much easier, and very large amounts of data can be stored without having to purchase a single, expensive server.

NoSQL databases can flexibly support both _read-heavy_ and _write-heavy_ systems. With data spread out across multiple shards/servers, hashing and consistent hashing are very important techniques for determining which shards to route the application queries to.

**Example:** MongoDB uses a query router, which is a reverse proxy that accepts a query and routes it to the appropriate shard(s). The router then sends the query response back to the calling application. Note that, query router is very similar to load balancer.

### Eventual Consistency of NoSQL systems

NoSQL databases are typically designed for distributed use cases, and write-heavy systems can be supported by having multiple write shards for the same data partition (called peer-to-peer replication). However, the trade-off is a loss of strong consistency. After a write to a shard in a distributed NoSQL cluster, there will be a small delay before that update can be propagated to other replicas. During this time, reading from a replica can result in accessing stale data. This weakness of the data eventually being up-to-date, a.k.a eventual consistency, was actually seen earlier with master-slave replication (which can be used for SQL or NoSQL). Eventual consistency isn't exactly a fault of NoSQL databases, but distributed databases in general. A single shard NoSQL database can be strongly consistent, but to fully take advantage of the scalability benefits of NoSQL, the database should be set up as a distributed cluster:

- NoSQL databases are designed to run intelligently on clusters.
- NoSQL databases had to sacrifice Strong consistency, ACID Transactions, and much more to scale horizontally over a cluster and across the data centers. The data with NoSQL databases is more eventually consistent as opposed to being strongly consistent.
- When working with relational databases, a big chunk of our time goes into learning how to design well-normalized tables, setting up relationships, trying to minimize joins, and so on.

## Cons of NoSQL Databases

### Inconsistency

Since an entity is spread throughout the database, one has to update the new values of the entity at all places.

Failing to do so, makes the entity inconsistent. This is not a problem with relational databases. since they keep the data normalized (at unique places).

### No support for ACID transactions

Also, NoSQL distributed databases don't provide ACID transactions

Transactions in distributed systems come with terms and conditions applied.
