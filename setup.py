
from setuptools import setup, find_packages

setup(
    name="ASBPredictor",
    version="0.1.0",
    author="Yang Fang",
    author_email="yangfangscu@gmail.com",
    description="A Python package for predicting ASB risk from clinical data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yangfangs/ASBPredictor",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.0",
        "scikit-learn>=1.5.0"
    ],
    entry_points={
        "console_scripts": [
            "ASBPredictor=ASBPredictor.predictor:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
