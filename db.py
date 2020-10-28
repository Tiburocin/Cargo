import psycopg2
from psycopg2.extras import DictCursor 
import logging as logger 

class Database:

    def __init__(self):
        self.host = 'localhost'
        self.database = "Cargo"
        self.user = "postgres"
        self.password = "0000"
        self.con = None

    def connect(self):
        if self.con is None:
            try:
                self.con = psycopg2.connect(
                    host = self.host,
                    database =self.database,
                    user = self.user,
                    password = self.password,
                )
            except psycopg2.DatabaseError as e:
                logger.error(e)
                raise e
            finally:
                logger.info('Connection successfully')

    def selectRows(self,query):
        self.connect()
        with self.con.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records  

    def add(self, query, records):
        self.connect()
        with self.con.cursor() as cur:
            cur.execute(query,records)
            self.con.commit()
            count = cur.rowcount
            cur.close()
            return count  

    def getQuantity(self, query):
        self.connect()
        with self.con.cursor() as cur:
            cur.execute(query)
            self.con.commit()
            count = cur.fethone()
            cur.close()
            return count


