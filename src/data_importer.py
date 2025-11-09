import os
import sys
import pandas as pd
from sqlalchemy import create_engine,URL

#input parameters
#local dev purpose
# input_file = "./data/paris_airbnb_listing/paris_airbnb_listings.csv"
# docker_URL = "postgresql://sqluser:secret@192.168.1.92:5432/global_data"

#input_variables

input_file = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
host = sys.argv[4]
port = sys.argv[5]
database = sys.argv[6]
table_name = sys.argv[7]

#read the csv and store into a dataframe
df = pd.read_csv(input_file)

#Create an engine to connect to the database
dbms_url = URL.create(
    "postgresql", #drivername is handled by SQLAlchemy. Never changes b/w envs. 
    username = username,
    password = password,
    host = host,
    port = port,
    database = database
)
engine = create_engine(dbms_url,echo = False)

#We can directly push the df to the PostgresSQL server
df.to_sql(name = table_name, con = engine, if_exists = 'replace')

