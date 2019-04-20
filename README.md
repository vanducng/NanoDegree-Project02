# NanoDegree-Project02
## Summary of project
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

This project aims to reate an Apache Cassandra database which can create queries on song play data to answer the questions. The data model relies on the requested queries from analytics team. 

## How to run the python scripts
1. Download and install **Cassandra** on your machine by following official document with your respective OS system. The latest version is 3.11. Download and instruction here: [Cassandra Download](http://cassandra.apache.org/download/)
Run Cassandra as forground mode by ```cassandra -f``` from the terminal. On other terminal, we can start running cql script shell by ```cqlsh```

>> ![cassandra querry lanaguage](/images/cqlsh.png)

2. Run ```python create_tables.py``` to create the sparkify keyspace and 3 required tables. The tables can be checked by using this cql ```SELECT table_name FROM system_schema.tables WHERE keyspace_name = 'sparkify';```. Table details can be also checked by ```DESCRIBE TABLE music_log_by_session``` for example.

>> ![Table Setup](/images/sparkify_tables.png)

3. Run `python etl.py` to load data from event data into 3 created tables in step 2.

4. Run `python test.py` test the queries which derived the purpose of creating these 3 tables. The result is displayed as below:
>> ![Query validation](/images/query_validation.png)

5. You can add more tables or testing query under ```sql_queries.py``` file. The jupyter notebook will help to understand the steps of how to model Cassandra tables.



