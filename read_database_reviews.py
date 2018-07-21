# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:22:28 2018

@author: user


pip install --upgrade google-cloud-bigquery
created json file for service account https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python
SA name : hagit-926@cooladata-cs-solutions.iam.gserviceaccount.com
created json file in C:\Users\user\Documents\Python Scripts\thesis\cooladata-cs-solutions-3be46bd05169.json

set env variable GOOGLE_APPLICATION_CREDENTIALS=C:\Users\user\Documents\Python Scripts\thesis\cooladata-cs-solutions-3be46bd05169.json 

import pandas as pd
# https://github.com/SohierDane/BigQuery_Helper
from bq_helper import BigQueryHelper

bq_assistant = BigQueryHelper("bigquery-public-data", "github_repos")

"""
# Imports the Google Cloud client library
from google.cloud import bigquery
import pandas as pd
 
# Instantiates a client
bigquery_client = bigquery.Client()
projectid = "cooladata-cs-solutions"

for j in range(10):
    print (j) 
    stmt = 'SELECT user_id,text  FROM imdb2.text_of_4000_concat where grp={}'.format(j) 
    df = pd.read_gbq(stmt, projectid  )

 
#Create 1 file per user 

    i=0
    
    for index, row in df.iterrows():
        K=row['user_id']
        filename = 'review_data\\review_{}.txt'.format(K)
         
        with open(filename, "w") as text_file:
            text_file.write(row['text'].encode('utf-8').strip()  )    
        