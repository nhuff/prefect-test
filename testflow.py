from prefect import flow, task
from pathlib import Path


@task
def touch_file():
    Path('/tmp/file.txt').touch()

@flow(persist_result=True)
def my_flow() -> str:
    touch_file()
    return "Hello, world!"
