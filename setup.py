import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ponyup',
    version='0.0.1',
    author='Hao Tian',
    author_email='haot@smu.edu',
    description="Python project exmaple template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/smu-tao-group/py_package_example',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    license='GPLv3',
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
