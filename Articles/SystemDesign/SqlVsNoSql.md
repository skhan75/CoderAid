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
