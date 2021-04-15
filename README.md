## Description

This is a tiny (no, really tiny) wrapper for app authentication and vacancy search API on Russian hr site hh.ru.

## Installation
1. Install from PYPI: `pip install headpy`
2. Clone this repository to local machine and build it:
	1. Clone it: `git clone https://github.com/retardigrade/headpy.git`
	2. Update build: `python -m pip install --upgrade build`
	3. Build package: `python -m build`
	4. Install package wheel from dist/ with `python -m pip install dist\headpy-0.0.1-py3-none-any.whl`
	
## NB
Due to limitations of API, maximal number of vacancies you can get is 2000. Anyway, you can separate requests dy specifying publish dates and get all, though it can possibly be discouraged by hh.ru API authors.
