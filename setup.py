from setuptools import setup, find_packages

def packages(file_path):
    requirements = []
    with open(file_path) as File_obj:
        requirements_file=File_obj.readlines()
        requirements = [requirement.replace('\n','') for requirement in requirements_file]
    return requirements

setup(
    name='ML_project',
    version='0.1',
    packages=find_packages(),
    author='Umez Harge',
    author_email='UmezHarge63@email.com',
    install_requires=packages('requirements.txt')
)
