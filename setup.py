from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
     this function will return list of req
    """
    req_lst:List[str]=[]
    try:
        with open("req.txt","r") as file:
            lines =file.readlines()
            for line in lines:
                req=line.strip()
                ## ignore the empty lines and -e.
                if req and req != "-e .":
                    req_lst.append(req)
    except FileNotFoundError:
        print("req.txt file not found")
    return req_lst

setup(
    name="NetworkSecurity",
    version="0.1",
    author="dareproton",
    author_email="assis.mohanty.98@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)