from prefect import task, flow
import pandas as pd
from prefect_github.repository import GitHubRepository
from io import StringIO

git = GitHubRepository.load("gitblock")



@task(log_prints=True)
def importing_data():
    print("running task 1. ----------Attempting to import data---------- !")

    csv_bytes = git.read_path('data.csv')
    csv_string = csv_bytes.decode("utf-8")
    
    
    data = pd.read_csv(StringIO(csv_string))
    
    return data

@task(log_prints=True)
def load(df):
    print("Running task 2 -----------Attempting to load data-------------")
    csv_str = df.to_json()
    git.write_path(path='data.json', content=csv_str)

@flow(log_prints=True)
def main():
    print("running main flow")
    data = importing_data()
    load(data)




    
