import json 
import s3fs

import pandas as pd

def lambda_handler(event, context):


    # ##### Hardcoded path - Use this for manual testing - 
    bucket = 's3_directory_name'
    key = 'subdirectory/filename.csv'    


    # ##### Use this for trigger-based run
    # # bucket = event['Records'][0]['s3']['bucket']['name'] + '/'
    # # key = event['Records'][0]['s3']['object']['key']

    # # print('bucket:',bucket)
    # # print('key:', key)
    
    path = f's3://{bucket}{key}'
    print(path)

    df = pd.read_csv(path)
    print(df.head())
