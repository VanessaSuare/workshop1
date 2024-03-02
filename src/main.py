"""Connection, create and inserts to postgres"""

import csv
import psycopg2
from config import config


def connect():
    """ connection database """
    connection = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        with psycopg2.connect(**params) as connection:

            # create a cursor
            with connection.cursor() as crsr:

                # drop in case exist
                crsr.execute('DROP TABLE IF EXISTS candidates')

                # create table
                create_table = """
                    CREATE TABLE IF NOT EXISTS candidates (
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR(255) NOT NULL,
                    lastname VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NULL,
                    applicationdate TIMESTAMP NULL,
                    country VARCHAR(255) NOT NULL,
                    yoe INT NOT NULL,
                    seniority VARCHAR(255) NOT NULL,
                    technology VARCHAR(255) NOT NULL,
                    codechallengescore INT NULL,
                    technicalinterviewscore INT NULL);"""
                crsr.execute(create_table)

                # Insert data
                with open('candidates_EDA.csv', newline='', encoding="utf-8") as csv_file:
                    data = csv.reader(csv_file, delimiter=';')
                    for index, row in enumerate(data):
                        if index == 0:
                            continue
                        insert_data = crsr.mogrify("""
                            INSERT INTO candidates (
                            firstname, lastname, email, applicationdate, country, yoe, seniority, technology, codechallengescore, technicalinterviewscore) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s);""", row)
                        crsr.execute(insert_data)
                        connection.commit()
                # Create a new table for candidate hired
                create_new_table= """
                    CREATE TABLE candidates_hired AS
                    SELECT *,
                        CASE WHEN "codechallengescore" >= 7 AND "technicalinterviewscore" >= 7 THEN TRUE ELSE FALSE END AS hired
                    FROM candidates"""
                crsr.execute(create_new_table)
                connection.commit()
    except (ImportError, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


connect()
