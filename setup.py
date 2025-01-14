
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setup(
	name='trainingaidhanis',
	version='0.1',
	author="Dhaniswara Wiradharma",
	author_email="dhaniswarawiradharma@bgmail.com",
	description="An AI package 2025 for fucntion and constanta",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/dhaniswaraW/trainingaidhanis/",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		],
	install_requires=[],
	entry_points={
        "console_scripts": ['trainingaidhanis=trainingaidhanis.main:welcome']
    },
 )