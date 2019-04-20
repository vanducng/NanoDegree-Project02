import cassandra
from cassandra.cluster import Cluster
import pandas as pd
from tabulate import tabulate
from sql_queries import select_queries


def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)


def main():
    # Initialize the cassandra connection
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()
    session.set_keyspace("sparkify")

    # Config to convert data from Cassandra row to pandas dataframe
    session.row_factory = pandas_factory
    session.default_fetch_size = None

    # Run the select query
    for query in select_queries:
        rows = session.execute(query)
        print(query)
        print(tabulate(rows._current_rows, headers='keys',
                       tablefmt='psql', showindex=False))
        print("\n\n")

    # Close the connection to cassandra
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
