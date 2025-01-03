from setuptools import setup, find_packages
from datetime import datetime

current_version = f"1.0.0+{datetime.now().strftime('%Y%m%d.%H%M')}"

setup(
    name="credit_analysis_ruzanv",
    version=current_version,
    description="Credit default analysis package for ruzanv",
    author="ruzanv",
    packages=find_packages(),
    install_requires=[
    ],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
