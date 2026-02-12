from setuptools import setup, find_packages

setup(
    name="admz",
    version="0.1.0",
    description="Axis Device Management Zone - Intelligent device management for Axis cameras",
    author="dnobj",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0",
        "requests>=2.28.0", 
        "cryptography>=3.4.0",
        "pydantic>=1.10.0",
        "click>=8.0.0",
        "rich>=12.0.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "admz=src.cli:main",
        ],
    },
)
