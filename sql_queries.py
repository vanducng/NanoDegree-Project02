# DROP TABLES
music_log_by_session_drop = "DROP TABLE music_log_by_session"
music_log_by_session_and_user_drop = "DROP TABLE music_log_by_session_and_user"
user_log_by_song_drop = "DROP TABLE user_log_by_song"


# CREATE TABLES
music_log_by_session_create = """
CREATE TABLE IF NOT EXISTS music_log_by_session
 (session_id int, item_in_session int, artist text, song_title text, song_length float, PRIMARY KEY(session_id, item_in_session));
"""

music_log_by_session_and_user_create = """
CREATE TABLE IF NOT EXISTS music_log_by_session_and_user
 (session_id int, user_id int, item_in_session int, artist text, song_title text, user_first_name text, user_last_name text, PRIMARY KEY ((session_id, user_id), item_in_session))
  WITH CLUSTERING ORDER BY (item_in_session ASC);
"""

user_log_by_song_create = """
CREATE TABLE IF NOT EXISTS user_log_by_song
 (song_title text, user_first_name text, user_last_name text, PRIMARY KEY(song_title));
"""

# INSERT DATA
music_log_by_session_insert = """
INSERT INTO music_log_by_session(session_id, item_in_session, artist, song_title, song_length)
 VALUES(%s, %s, %s, %s, %s)
"""

music_log_by_session_and_user_insert = """
INSERT INTO music_log_by_session_and_user(session_id, user_id, item_in_session, artist, song_title, user_first_name, user_last_name)
 VALUES(%s, %s, %s, %s, %s, %s, %s)
"""

user_log_by_song_insert = """
INSERT INTO user_log_by_song(song_title, user_first_name, user_last_name)
 VALUES(%s, %s, %s)
"""

# SELECT QUERY
music_log_by_session_select = "SELECT * FROM music_log_by_session WHERE session_id = 338 AND item_in_session = 4;"
music_log_by_session_and_user_select = "SELECT * FROM music_log_by_session_and_user WHERE user_id = 10 AND session_id = 182;"
user_log_by_song_select = "SELECT * FROM user_log_by_song WHERE song_title = 'All Hands Against His Own';"


create_table_queries = [music_log_by_session_create,
                        music_log_by_session_and_user_create,
                        user_log_by_song_create]

drop_table_queries = [music_log_by_session_drop,
                      music_log_by_session_and_user_drop,
                      user_log_by_song_drop]

insert_table_queries = {"music_log_by_session": music_log_by_session_insert,
                        "music_log_by_session_and_user": music_log_by_session_and_user_insert,
                        "user_log_by_song": user_log_by_song_insert}

select_queries = [music_log_by_session_select,
                  music_log_by_session_and_user_select,
                  user_log_by_song_select]
