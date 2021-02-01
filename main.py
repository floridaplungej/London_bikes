from datetime import datetime
from __init__ import DatabaseContextManager


# def create_table_bikesharing():
#     query = """CREATE TABLE `bikesharing` (
#     `tstamp` timestamp,
#     `cnt` integer,
#     `temperature` decimal(5, 2),
#     `temperature_feels` decimal(5, 2),
#     `humidity` decimal(4, 1),
#     `wind_speed` decimal(5,2),
#     `weather_code` integer,
#     `is_holiday` boolean,
#     `is_weekend` boolean,
#     `season` integer);"""
#
#     with DatabaseContextManager() as db:
#         db.execute(query)


# def convert_line_to_values(line):
#     values = line.split(",")
#     # convert timestamp to datetime
#     values[0] = datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")
#     print(values[0])
#     return values
#
#
# sql = """
#         INSERT INTO bikesharing
#         (tstamp, cnt, temperature, temperature_feels, humidity, wind_speed,
#         weather_code, is_holiday, is_weekend, season) VALUES
#         (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
#
# with DatabaseContextManager() as db:
#     with open("london-bikes.csv") as f:
#         for i, line in enumerate(f):
#             if i == 0:
#                 continue
#             values = convert_line_to_values(line)
#             db.execute(sql, values)
#             if i % 15000 == 0:
#                 db.commit()
#         db.commit()
#     f.close()
#     db.close()
#
# create_table_bikesharing()
# convert_line_to_values(line)

def get_shares_by_season():
    query = """SELECT season, SUM(cnt) AS shares FROM bikesharing GROUP BY season"""

    with DatabaseContextManager("CRUD") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

def get_shares_by_thunderstorms():
    query = """SELECT weather_code, SUM(cnt) 
    AS shares FROM bikesharing WHERE weather_code >= 4"""

    with DatabaseContextManager("CRUD") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

def get_shares_by_time():
    query = """SELECT tstamp, cnt AS most_new_shares FROM bikesharing ORDER BY cnt DESC LIMIT 1"""

    with DatabaseContextManager("CRUD") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

get_shares_by_season()
get_shares_by_thunderstorms()
get_shares_by_time()