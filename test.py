# import time
# from helper_functions import get_player_season_stats, get_player_career_stats
# import csv
# import crud

# import pandas as pd


# stats = get_player_season_stats("Jordan","Poole",2024)
# print(stats)
# def read_csv():
#     df = pd.read_csv("player.csv")
#     try:
#         last_index = 10
#         for index,row in df.iterrows():
#             if index ==last_index:
#                 time.sleep(5)
#                 last_index +=10
#             print(row['first_name'],row['last_name'])
#     except Exception as e:
#         return {"Message":e}

# for i in pd.read_csv("player.csv",chunksize=10):
#     for j in i:
#         print(j)
#         print("---------")


# read_csv()
# df = pd.read_csv("player.csv")
# print(df.head(10))
# print(df.info())

# for index,row in df.iterrows():
#     print(row["first_name"])

# for i in df:
#     print(i)
# print(df.to_string())

# from basketball_reference_web_scraper import client
# from basketball_reference_web_scraper.data import OutputType

# client.player_box_scores(
#     day=1, month=1, year=2017, 
#     output_type=OutputType.JSON, 
#     output_file_path="./1_1_2017_box_scores.json"
# )

# import sqlite3

# try:
#     conn = sqlite3.connect('nba.sqlite') # Connect to your database file
#     cursor = conn.cursor()

    # Example: List all tables in the database
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # print("Tables in the database:", cursor.fetchall())

    # Example: Select all data from a specific table (assuming 'users' table exists)
    # cursor.execute("SELECT * from player")
    # user_data = cursor.fetchall()

    # print("\nData from 'users' table:")
    # active_players = 0
    # for row in user_data:
    #     if row[4] == 1:
    #         active_players += 1
    # print(active_players)
    # inactive_players = len(user_data)-active_players
    # print(inactive_players)
    # total_players = len(user_data)
    # print(total_players)

#     cursor.execute("SELECT * from draft_history")
#     user_data = cursor.fetchall()       
#     for row in user_data:
#         print(row)
# except sqlite3.Error as e:
#     print(f"Database error: {e}")

# finally:
#     if conn:
#         conn.close()


import sqlite3

# Define the input SQLite database file and the output SQL dump file
sqlite_db_file = 'nba.sqlite'
output_sql_file = 'output_dump.sql'

try:
    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db_file)

    # Open the output SQL file in write mode
    with open(output_sql_file, 'w') as f:
        # Iterate through the database dump and write each line to the file
        for line in conn.iterdump():
            f.write(f'{line}\n')

    print(f"Successfully dumped '{sqlite_db_file}' to '{output_sql_file}'")

except sqlite3.Error as e:
    print(f"Error dumping database: {e}")

finally:
    # Close the database connection if it was opened
    if 'conn' in locals() and conn:
        conn.close()



# import psycopg2

# def run_sql_file(sql_file_path, db_config):
#     """
#     Executes a SQL file against a PostgreSQL database.

#     Args:
#         sql_file_path (str): Path to the SQL file.
#         db_config (dict): Dictionary containing database connection details.
#                           Expected keys: 'host', 'database', 'user', 'password', 'port'.
#     """
#     conn = None
#     try:
#         # Connect to the PostgreSQL database
#         conn = psycopg2.connect(**db_config)
#         conn.autocommit = True  # Set autocommit to True for schema creation/data insertion

#         # Create a cursor object
#         cur = conn.cursor()

#         # Read the SQL file content
#         with open(sql_file_path, 'r') as f:
#             sql_script = f.read()

#         # Execute the SQL script
#         cur.execute(sql_script)

#         print(f"SQL file '{sql_file_path}' executed successfully.")

#     except psycopg2.Error as e:
#         print(f"Error executing SQL file: {e}")
#     finally:
#         if conn:
#             conn.close()





# #             # psql -U postgres -d nba_data -h localhost -p 5432 -f output_dump.sql

# # if __name__ == "__main__":
# #     # Database connection details
# #     db_configuration = {
# #         'host': 'localhost',
# #         'database': 'nba_data',
# #         'user': 'postgres',
# #         'password': 'Nomadic1',
# #         'port': 5432
# #     }

# #     # Path to your SQL file
# #     sql_file = 'output_dump.sql'

# #     run_sql_file(sql_file, db_configuration)


# import sqlite3
# import psycopg2
# import pandas as pd

# # Connect to SQLite
# sqlite_conn = sqlite3.connect("nba.sqlite")

# # Connect to Postgres
# pg_conn = psycopg2.connect("dbname=nba_data user=postgres password=Nomadic1 host=localhost")

# # Get list of tables
# tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", sqlite_conn)

# for table in tables['name']:
#     df = pd.read_sql(f"SELECT * FROM {table}", sqlite_conn)
#     df.to_sql(table, pg_conn, if_exists='replace', index=False, method='multi')

# sqlite_conn.close()
# pg_conn.close()