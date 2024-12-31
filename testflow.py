from prefect import flow
from pathlib import Path


@flow
def my_flow() -> str:
    Path('/tmp/file.txt').touch()
    print("Hello, world!")
