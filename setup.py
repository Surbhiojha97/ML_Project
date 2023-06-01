from setuptools import find_packages,setup
from typing import List

E_DOT ="-e ."
def get_requirements(file_path:str)->List[str]:
    """
        This function will return the list of libraries we require in our project.
    """
    requirements=[]
    with open(file_path) as fp:
        requirements = fp.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)

    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Surbhi Ojha',
    author_email="ojhasurbhi68@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)