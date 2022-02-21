# Designing Data Intensive Applications

## Chapter 1: Data Models and Query Languages

### SQL

- Data is organized into relations (called _tables_ in SQL)
- Each relation is an unordered collection to tuples (_rows_ in SQL)

### The Object Relational Mismatch

- If data is stored in relational table, an awkward translation layer is required between the objectors in the application code and storage layer.
- This disconnect between the models is sometimes called \*_Impedance Mismatch_.
- ORM (Object Relation Mapping) frameworks like Active Record and Hibernate reduces the amount of boiler plate code required for this translation.
- Some developers feel that the JSON model reduces the impedance mismatch between the application code and the storage layer.
- JSON representation has better _locality_ than multi table schema.
- If you want to fetch a profile in the relational db example, you need to either perform multiple queries (query each table by `user_id`) or perform a messy way to join the users table and its subordinate tables.
- While in the JSON representation, all the information is in one place and one query is sufficient.

### Many-to-One and Many-to-Many Relationships

- The advantage of using `ID` is that because it has no meaning to humans, it never needs to change.
- Remove duplications is the key behind **normalization** in the databases.
  - Prevent write overheads
  - Prevent risk of inconsistencies, where some copies of information are updated but others aren't.
