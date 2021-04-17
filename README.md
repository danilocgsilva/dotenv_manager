# Dotenv Manager

Manage environment variables groups - dev, prod, staging, etc...

## Prerequisites

* Python 3
* Pip 3

## Installation

Go to the project root directory and type:

```
pip install .
```

## Usage

(to be implemented)
```
demanager
```
List all commands for demanager

(to be implemented)
```
demanager -m :
```
List all environments variables groups

(to be implemented)
```
demanager -m groupenvironment:
```
List all variables from the `groupenvironment` group environment.

(to be implemented)
```
demanager -m groupenvironment:MYVARIABLE
```
Shows the variable value

(to be implemented)
```
demanager -m groupenvironment:MYVARIABLE variable_value
```
Sets a value for the variable `MYVARIABLE` from `groupenvironment`

(to be implemented)
```
demanage -m groupenvironment -f .env
```
Creates a group environment name `groupenvironment` based on `.env` file.

(to be implemented)
```
demanage -m groupenvironment -t .env
```
Creates a group environment *template*. Which means, you may have several projects with the same variables groups.
