from setuptools import setup, find_packages

setup(
    name="hedgehog",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlmodel",
        "alembic",
        "fastapi",
        "pydantic>=2.5.2",
        "python-dotenv>=1.0.1,<2.0.0",
        "logfire>=3.7.1",
        "typer[all]",
        "pydantic-ai>=0.0.35",
        "pydantic-graph>=0.0.17",
        "typing-extensions>=4.9.0",
        "logfire-api>=3.7.1",
        "typing-inspection>=0.4.0",
    ],
)