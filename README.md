## Description

This is a tiny (no, really tiny) wrapper for app authentication and vacancy search API on Russian hr site hh.ru.
https://pypi.org/project/headpy/0.0.1/

## Installation
1. Install from PYPI: `pip install headpy`
2. Clone this repository to local machine and build it:
	1. Clone it: `git clone https://github.com/retardigrade/headpy.git`
	2. Update build: `python -m pip install --upgrade build`
	3. Build package: `python -m build`
	4. Install package wheel from dist/ with `python -m pip install dist\headpy-0.0.1-py3-none-any.whl`
	
## Usage
1. Import package
2. Create 'credentials' directory in directory where your script lies
3. Place https://github.com/retardigrade/headpy/blob/main/credentials/app_credentials file in credentials directory
4. Fill it with appropriate values (if you don't have client id and secret yet, first create hh app at https://api.hh.ru)
	
## NB
Due to limitations of API, maximal number of vacancies you can get is 2000. Anyway, you can separate requests dy specifying publish dates and get all, though it can possibly be discouraged by hh.ru API authors.
