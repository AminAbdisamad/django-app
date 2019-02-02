# My Blog

This is a personal blog

## Project Requirements

Make sure you have **Python3** and **Django** Installed
check whether python3 is installed

```shell
python3 --version
```

check whether Django is installed

```shell
python3 -m django --version

```

## Installations

Install Python3 from the official website https://www.python.org/downloads/

## Setup Virtual Environment

install virtual environment using pip3

```shell
pip3 install pipenv
```

Activate virtual environment

```shell
pipenv shell
```

Install Django with pipenv

```shell
pipenv install django
```

After you make sure that Python and Django installed, to check the list of available commands type

```shell
django-admin
```

To start a new project

```shell
django-admin startproject blog
```

To run our Django server

## The development server

Let’s verify Our Django project works. Change into the outer mysite directory and run the following commands:

```shell
python manage.py runserver
```

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

#### Projects vs. apps

> What’s the difference between a project and an app? An app is a Web application
> that does something – e.g., a Weblog system, a database of public records or a
> simple poll app. A project is a collection of configuration and apps for a
> particular website. A project can contain multiple apps. An app can be in
> multiple projects.

To create your app, make sure you’re in the same directory as manage.py and type this command:

```shell
python manage.py startapp pages
```

### Contributors

Amin Abdisamad <theaminux@gmail.com>

### Copyright and License

© AMIN ABDISAMAD, ASAL SOLUTIONS
licensed under [MIT License](LICENSE)
