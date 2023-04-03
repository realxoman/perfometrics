from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='perfometrics',
    version='0.0.3',
    author="Ali Esmaeili",
    author_email='hi@aliesm.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/realxoman/perfometrics',
    keywords=["performance", "metrics", "testing", "speed test"],
    project_urls={
        "Bug Tracker" : "https://github.com/realxoman/perfometrics/issues",
        "Documentation" : "https://perfometrics.readthedocs.io/en/latest/",
    },
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.0.0",
        "pycurl>=7.0.0",
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    
)