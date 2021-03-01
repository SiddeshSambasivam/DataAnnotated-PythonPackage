import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataAnnotated",
    version="1.0.0",
    author="Siddesh Sambasivam Suseela",
    author_email="plutocrat45@gmail.com",
    description="Python package for DataAnnotated platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SiddeshSambasivam/DataAnnotated-PythonPackage",
    project_urls={
        "Bug Tracker": "https://github.com/SiddeshSambasivam/DataAnnotated-PythonPackage/issues",
    },
    install_requires=[
        'appdirs==1.4.4',
        'args==0.1.0',
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'click==7.1.2',
        'clint==0.5.1',
        'colorama==0.4.4',
        'idna==2.10',
        'numpy==1.20.1',
        'pandas==1.2.2',
        'prompt-toolkit==1.0.14',
        'pyfiglet==0.7',
        'Pygments==2.8.0',
        'PyInquirer==1.0.3',
        'python-dateutil==2.8.1',
        'pytz==2021.1',
        'regex==2020.11.13',
        'requests==2.25.1',
        'six==1.15.0',
        'termcolor==1.1.0',
        'urllib3==1.26.3',
        'wcwidth==0.2.5'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7.9",
)