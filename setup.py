'''
The setup.py file is an essential part of packaging and distributing python projects. It is used by setuptools to define the package metadata and dependencies.

--> find_packages() is a function that goes into every folder and searches for the __init__.py file. If it finds one, it considers that folder as a package and includes it in the distribution.
'''


from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
  '''
  This function will return the list of requirements
  '''
  requirement_list = []
  try:
    with open('requirements.txt') as file:
      lines = file.readlines()
      for line in lines:
        requirement = line.strip()
        #ignore empty lines and -e .
        if requirement and requirement != '-e .':
          requirement_list.append(requirement)
  except FileNotFoundError:
    print("File not found")

  return requirement_list

setup(
  name='NetworkSecurity',
  version='0.0.1',
  author='Amruth Kannan',
  author_email='amruthkannan117@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements(),
)
