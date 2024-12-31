from prefect import flow
from pathlib import Path


@task
def touch_file()
    Path('/tmp/file.txt').touch()

@flow
def my_flow() -> str:
    print("Hello, world!")
