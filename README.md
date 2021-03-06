# Clara Bootstrap Scripts for python and Java

A collection of scripts to help the CLARA services developers to only worry about programming the algorithms and to not care about project structures, dependencies or go through installation processes.

## System Requirements

* Gradle (For java scaffolding)
* Python pip

## Installation

Install the scripts requirements

```sh
$ pip install -r requirements.txt
```

And then simply run in the terminal the **setup.py** script with the install argument

```sh
$ ./setup.py install
```

## How to Use

Once that the scripts are properly installed in your system, the only script that you need to
run in the command line is **clara**, following the form:

```sh
$ clara <bootstrap-option> [<OPTIONAL ARGUMENTS>]
```

| Command  | Arguments             | Description                                                                                                                                                                                                  |
|----------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scaffold | LANGUAGE PROJECT_NAME | creates the CLARA Service skeleton in Python simply run in the command  line, the following command,replace the **PROJECT_NAME** with your desired name for the project. Supports Java and Python languages. |
|  install | LANGUAGE              |  installs clara and all of its dependencies, Supports python                                                                                                                                                 |                         |                                                                                                                                                                         |


## How to Contribute

* Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
* Fork the [repository](https://github.com/royarzun/clara-bootstrap) on GitHub to start making your changes to the **master** branch (or branch off of it).
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request and bug the maintainer until it gets merged and published.
