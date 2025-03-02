from setuptools import setup, find_packages

setup(
    name="linux-command-describer",
    version="0.1.0",
    packages=find_packages(),
    description="A Python utility that converts Linux commands into human-readable descriptions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="nonbios-1",
    author_email="nonbios-1@nonbios.ai",
    url="https://github.com/nonbios-1/linux-command-describer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
