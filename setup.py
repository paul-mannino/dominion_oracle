from setuptools import setup, find_packages

setup(
    name="dominion_oracle",
    version="0.1",
    description="Library for making fun insights about the Dominion card game",
    packages=find_packages(),
    install_requires=["beautifultable"],
    extras_require={"testing": ["pytest"], "dev": ["pre-commit"]},
)
