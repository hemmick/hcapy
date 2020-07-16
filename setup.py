import setuptools

with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
        name="hcapy-hemmick",
        version="0.0.1",
        author="hemmick",
        author_email="john.hemmick@silabs.com",
        description="HCA(Py) the z-ware hcapi wrapped in python",
        long_description=long_desc,
        long_description_content_type="text/markdown",
        url="https://github.com/hemmick/hcapy",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU GPLv3",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6'
)
