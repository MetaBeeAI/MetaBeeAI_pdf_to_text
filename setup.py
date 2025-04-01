# setup.py
from setuptools import setup, find_packages

setup(
    name="metabeeai-pdf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "requests",
        "pandas",
        "pyyaml",
        "python-dotenv",
        "openai",
        "unidecode",
    ],
    author="Rachel Parkindon",
    author_email="rachel.parkinson@biology.ox.ac.uk",
    description="MetaBeeAI Pipeline for PDF processing",
    keywords="pdf, data extraction",
)