import cassandra
from cassandra.cluster import Cluster
from sql_queries import create_table_queries


def create_keyspace(session):
    session.execute("DROP KEYSPACE IF EXISTS sparkify;")
    session.execute(
        "CREATE KEYSPACE sparkify WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};")
    session.set_keyspace("sparkify")


def create_tables(session):
    for query in create_table_queries:
        session.execute(query)


def main():
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()
    create_keyspace(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
