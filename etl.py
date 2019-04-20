import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra.cluster import Cluster
from sql_queries import insert_table_queries


def process_data(session, event_data):
    """
    Load data from event data into 3 tables: music_log_by_session, music_log_by_session_and_user and user_log_by_song

    Parameters:
    session: session of connection to cassandra sparkify database
    event_data: the list of collected event data that was preprocessed

    Returns: null
    """
    for line in event_data:
        session.execute(insert_table_queries.get("music_log_by_session"),
                        (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))

        session.execute(insert_table_queries.get("music_log_by_session_and_user"),
                        (int(line[8]), int(line[10]), int(line[3]), line[0], line[9], line[1], line[4]))

        session.execute(insert_table_queries.get("user_log_by_song"),
                        (line[9], line[1], line[4]))


def preprocess_data(file_path_list):
    """
    Combine event data, filer empty Artist column and export a new csv file as "event_datafile_new.csv"

    Parameters:
    file_path_list (str): where the csv files stored

    Returns:
    clean_data_row_list: list of filtered and clean data from raw input
    """
    full_data_rows_list = []
    clean_data_row_list = []
    for f in file_path_list:
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # skip header row

            for line in csvreader:
                full_data_rows_list.append(line)
    csv.register_dialect(
        'myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName',
                         'length', 'level', 'location', 'sessionId', 'song', 'userId'])
        for row in full_data_rows_list:
            if(row[0] == ''):
                continue
            row_list = [row[0], row[2], row[3], row[4], row[5],
                        row[6], row[7], row[8], row[12], row[13], row[16]]
            writer.writerow(row_list)
            clean_data_row_list.append(row_list)
    return clean_data_row_list


def main():
    # Get the path to event data folder
    filepath = os.getcwd() + "/event_data"
    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root, "*"))

    # Preprocess even data by cleaning, filtering and merging into one for further processing
    event_data = preprocess_data(file_path_list)

    # Initialize the connection and call process data method to insert data to target tables
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()
    session.set_keyspace("sparkify")
    process_data(session, event_data)

    # Close the connection after task completed
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
