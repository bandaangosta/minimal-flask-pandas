from setuptools import setup, find_packages

setup(
    name='minimalflaskpandas',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==1.0.2',
        'smartsheet-python-sdk==1.3.3',
        'pandas==0.23.4',
    ],
)
