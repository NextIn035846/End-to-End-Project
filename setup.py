
from setuptools import setup,find_packages
from typing import List

REQUIRMENT_FILE = 'requirements.txt'
HYPHEN_E = "-e ."
def get_requirement_list()->List[str]:
    #read the requirement files
    with open(REQUIRMENT_FILE) as requriment_files:
        requriment_list = requriment_files.readlines()
        # replace the new line charater to blank
        requriment_list = [requriment_name.replace("\n","") for requriment_name in requriment_list]

        if HYPHEN_E in requriment_list:
            requriment_list.remove(HYPHEN_E)
        return requriment_list





PROJECT_NAME = "Machine Learning"
VERSION = "0.0.1"
DESCRPTION= "This is my end to end project"
AUTHOE_NAME = "Thomas Patole"
AUTHOR_EMAIL = "thomaspatole19@gmail.com"

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRPTION,
      author=AUTHOE_NAME,
      author_email=AUTHOR_EMAIL,
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires = get_requirement_list()
     )