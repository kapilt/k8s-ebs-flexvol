from setuptools import setup, find_packages

setup(
    name="aws-ebs-flexvol",
    version='0.0.1',
    description="k8s ebs flexvol driver",
    classifiers=[
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Distributed Computing"
    ],
    url="https://github.com/kapilt/k8s-ebs-flexvol.git",
    license="Apache-2.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ebs-flexvol = ebs_flexvol.cli:cli']},
    install_requires=["boto3", "click"],
)
