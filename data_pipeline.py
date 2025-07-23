from prefect import task, flow
import pandas as pd
from prefect_github.repository import GitHubRepository
import os

git = GitHubRepository.load("gitblock")
git.get_directory()




@task(log_prints=True)
def importing_data():
    print("running task 1. ----------Attempting to import data---------- !")
    v = 'YES' if os.path.exists('data.csv') else 'NO'
    print('IS DATA.CSV PRESENT??? : ' + v)
          if v == 'YES':
              df = pd.read_csv('data.csv')
          else:
              return None

    
    
    return df

@task(log_prints=True)
def load(df):
    print("Running task 2 -----------Attempting to load data-------------")
    df.to_json('data.json')
    print("DOES DATA.JSON EXISTS?:" + str(os.path.exists('data.json')))
    

@flow(log_prints=True)
def main():
    print("running main flow")
    data = importing_data()
    load(data)




    
