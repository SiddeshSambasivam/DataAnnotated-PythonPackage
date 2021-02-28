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
    classifiers=[
        "Programming Language :: Python :: 3.7.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7.9",
)