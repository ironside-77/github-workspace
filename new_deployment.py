from prefect import flow

# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO='https://github.com/ironside-77/github-workspace'

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="data_pipeline.py:main", # Specific flow to run  
        
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my_pool",
        cron="0 * * * *",  # Run every hour
    )
