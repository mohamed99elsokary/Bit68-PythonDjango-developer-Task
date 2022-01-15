# Bit68 Python/Django developer Task


<br />
<br />

## Setup Project

<br />

### This project needs `python 3` and `PostgreSql` be installed before start the setup guide 
<br />

### Use the project virtual environment for windows via `venv` 
```bash
$ env\Scripts\activate.bat
```

<br />

### Use the project virtual environment for Linux or MacOS via `venv` 
```bash
$ source env/Scripts/activate
```

<br />

### Or create a new env via `venv` and install the requirements libraries via `PIP` 

```bash
$ python -m venv env
$ env\Scripts\activate.bat
$ pip install -r requirements.txt
```

<br />

### Edit `postgresql` database in the `DATABASES` setting of the project `settings.py` 

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "database_name",
        "USER": "username",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

<br />

### Make migrations for database.
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
<br />

### Run the project test cases.


```bash
$ python manage.py test
```

<br />

### Run the project.

```bash
$ python manage.py runserver
```

<br />

### Import Postman collection and give it a try using Postman.

