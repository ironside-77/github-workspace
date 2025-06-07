from prefect import task, flow
import pandas as pd

@task
def importing_data():
    data = pd.read_csv('C:/scripts/data.csv')
    print('running task 1')
    return data

@task
def to_json():
    df = importing_data()
    df.to_json('C:/workspace/data.json', orient='records')

@flow
def main():
    importing_data()
    to_json()

if __name__ == "__main__":
    main()
    
