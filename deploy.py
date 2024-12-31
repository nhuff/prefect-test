from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/nhuff/prefect-test.git",
        entrypoint="testflow.py:my_flow",
    ).deploy(
        name="my-github-deployment",
        work_pool_name="test",
    )
