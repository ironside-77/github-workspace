from prefect import flow
from prefect_github.repository import GitHubRepository

SOURCE_REPO = GitHubRepository.load("gitblock")

# Source for the code to deploy (here, a GitHub repo)


if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="data_pipeline.py:main" # Specific flow to run  
        
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my_pool",
        job_variables={'pip_packages':['pandas','prefect-github']}# Run every hour
    )
