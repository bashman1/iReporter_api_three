[![Build Status](https://travis-ci.org/bashman1/bootcamp15iReporter.svg?branch=deploy)](https://travis-ci.org/bashman1/bootcamp15iReporter/tree/deploy)
[![Coverage Status](https://coveralls.io/repos/github/bashman1/bootcamp15iReporter/badge.svg?branch=deploy)](https://coveralls.io/github/bashman1/bootcamp15iReporter?branch=deploy)
[![Requirements Status](https://requires.io/github/bashman1/bootcamp15iReporter/requirements.svg?branch=deploy)](https://requires.io/github/bashman1/bootcamp15iReporter/requirements/?branch=deploy)
[![Maintainability](https://api.codeclimate.com/v1/badges/cd6d05aff72cc080560e/maintainability)](https://codeclimate.com/github/bashman1/bootcamp15iReporter/maintainability)

# bootcamp15iReporter
Corruption is a huge bane to Africa’s development. African countries must develop novel and  localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables  any/every citizen to bring any form of corruption to the notice of appropriate authorities and the  general public. Users can also report on things that needs government intervention 

## features
1. user registration 
2. user login
3. retreave all users
4. report a red-flag
5. retreave all red-flags
6. retreave a specific red-flag
7. delete a red-flag

## requirements
1. Working Computer with Windows, Mac, Linux OS and Python 3 Installed
2. Text Editor
3. Postman or Docker

## installation
Clone the project from [GitHub](https://github.com/bashman1/bootcamp15iReporter.git)
navigate to the project folder
```
$ mkvirtualenv venv
$ pip install -r requirements.txt
$ python run.py
```
## aPI endpoints

Prefix `/api/v1` to the endpoints

| METHOD   | URL  | ACTION |
|---|---|---|
| POST | `/api/v1/auth/signup` | user ragistration|
| POST | `/api/v1/auth/login`| user login|
| GET  | `/api/v1/users` | retreave all users|
| POST | `api/v1/red-flags`| reporting a red-flag|
| GET  | `/api/v1/red-flags`| retreaving all red-flags|
| GET  |  `/api/v1/red-flags/<int:redflag_id>`| retreave a specific red-flag|
| DELETE | `/api/v1/red-flags/<int:redflag_id>` | delete a specific red-flag |



## build with
*Python 3
*Flask

## tools
* vs code
* virtual envvironment
* Pylint
* Pytest

## Versioning
version 1 of the API

## author
Wamula Bashir Saidi