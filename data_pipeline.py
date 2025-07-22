from prefect import task, flow
import pandas as pd


@task(log_prints=True)
def importing_data():
    data = pd.read_csv('data.csv')
    print('running task 1')
    return data

@task(log_prints=True)
def to_json(data):
    print("Running task 2")
    data.to_json('data.json', orient='records')

@flow(log_prints=True)
def main():
    print("running main flow")
    data = importing_data()
    to_json(data)




    
