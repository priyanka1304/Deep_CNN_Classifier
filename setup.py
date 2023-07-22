import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.1"

REPO_NAME = "DEEP_CNN_CLASSIFIER"
ATHOUER_USER_NAME = "priyanka1304"
SRC_REPO="deepClassifier"
AUTHOR_EMAIL = "priyankasingh131313@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=ATHOUER_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{ATHOUER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": "https://github.com/{ATHOUER_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)

    