#!/usr/bin/env python
# coding: utf-8

# In[12]:

# from sqlalchemy import MetaData, Table, Column, String
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
import numpy as np


class Database():

    engine = db.create_engine('postgresql://postgres:post_password@localhost:5432/metahuman_db')
    Session = sessionmaker(bind=engine)

    def __init__(self):
        self.connection = self.engine.connect()

    def saveData(self, dna, meta):
        try: 
            dna_sample = DnaSample(dna_array=str(dna), ismeta=meta)
            session = Session(bind=self.connection)
            session.add(dna_sample)
            session.commit()
            
        # pk alreasy existing
        except:
            pass

    def fetchStats(self):
        fetchQuery = self.connection.execute("""SELECT COALESCE(sum(cast(ismeta as integer)),0), 
                                               count(dna_array) FROM dna_samples""")
        result = fetchQuery.fetchall()
        final_result = result[0]
        population = final_result[1]
        if population == 0:
            return 0,0,0
        else: 
            ismeta = final_result[0]
            ishuman = final_result[1] - final_result[0]
            ratio = final_result[0]/final_result[1]
            return  ismeta,ishuman,ratio


Base = declarative_base()


class DnaSample(Base):
    __tablename__ = "dna_samples"

    dna_array = db.Column(db.String, primary_key=True, nullable=False)
    ismeta = db.Column(db.Boolean)

    def __repr__(self):
        return "<DnaSample(dna='%s', ismeta='%s')>" % (self.dna_array, self.ismeta)

# In[ ]:
# In[ ]:
