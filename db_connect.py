#!/usr/bin/env /Applications/MAMP/Library/bin/python

import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': 3306,
  'database': 'spotify_weather',
  'raise_on_warnings': True
}
def connect2db():
    con = mysql.connector.connect(**config)
    # cursor = con.cursor(dictionary=True)
    cursor = con.cursor(dictionary=True)
    return [con, cursor]


# cnx.close()