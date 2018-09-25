import os, logging

import pandas as pd
import psycopg2
import psycopg2.extras
from pymongo import MongoClient
from openflow import DataSource

class Postgres(DataSource):
    def __init__(self, query, preprocess=None):
        super().__init__(Postgres.fetch, preprocess)
        self.set_context({ 'query': query })

    def fetch(context):
        try:
            creds = "host='{}' dbname='{}' user='{}' password='{}'".format(os.environ['POSTGRES_HOST'], os.environ['POSTGRES_DBNAME'], os.environ['POSTGRES_USER'], os.environ['POSTGRES_PASSWORD'])
            conn = psycopg2.connect(creds)
        except:
            logging.error('Cannot connect to PostgreSQL database')
            exit()

        cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        query = context.get('query')
        cur.execute(query)

        return pd.DataFrame(cur.fetchall())

class Mongo(DataSource):
    def __init__(self, function, preprocess=None):
        super().__init__(Mongo.fetch, preprocess)
        self.set_context({ 'function': function })

    def fetch(context):
        try:
            client = MongoClient(os.environ['MONGO_URI'])
            db = client[os.environ['MONGO_DATABASE']]
        except:
            logging.error('Cannot connect to Mongo database')
            exit()

        rows = context.get('function')(db)
        return pd.DataFrame([row for row in rows])

class Request(DataSource):
    def __init__(self):
        super().__init__(Request.fetch)

    def fetch(context):
        return pd.DataFrame(context.get('request'), index=[0])
