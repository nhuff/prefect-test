from prefect import flow


@flow
def my_flow() -> str:
    print("Hello, world!")
