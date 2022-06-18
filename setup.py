from setuptools import find_packages, setup
from typing import List

#Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION="0.0.3"
AUTHOR="Rajkumar k"
DESCRIPTION="This is a first FSDS Nov batch Machine Learning Project"
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)
