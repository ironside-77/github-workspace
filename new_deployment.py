from prefect import flow

# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="C:/workspace/"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="data_pipeline.py:main", # Specific flow to run  
        pull_steps=[{"prefect.deployments.steps.set_working_directory":{'directory': "C:/workspace"}}]
    ).deploy(
        name="my-first-deployment",
    
        parameters={
            "github_repos": [
                "PrefectHQ/prefect",
                "pydantic/pydantic",
                "huggingface/transformers"
            ]
        },
        work_pool_name="my_pool",
        cron="0 * * * *",  # Run every hour
    )
