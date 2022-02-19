# Database Internals

## Storage Engines

Databases are modular systems and consists of multiple parts:

- **Transport Layer**, accepting requests
- **Query Processor**, determining the most efficient way to run queries
- **Execution Engine**, carrying out the operations
- **Storage Engine**

To compare databases, its helpful to understand the use case in great detail and define the current
and anticipated variables, such as:

- Schema and record sizes
- Number of clients
- Types of queries and access patterns
- Expected changes in any of these variables.

Most databases already have stress tools that can be used to reconstruct specific use cases.
