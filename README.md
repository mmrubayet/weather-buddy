# weather-buddy



### Clone this project:

```
git clone git@github.com:mmrubayet/weather-buddy.git
```

### Create Virtual Environment:

```commandline
python3.10 -m venv venv
source venv/bin/activate
```

#### Install requirements:

```commandline
pip install -r requirements.txt
```

### Create .env file and configure variables for database, email and others: 

```commandline
cp .env.example .env
```

#### Migrate database (Currently uses sqlite):

```commandline
python manage.py migrate
```


#### Create a superuser:

```commandline
python manage.py createsuperuser
```

### Run with:

```commandline
python manage.py runserver
```

### Run flake8 before commit:

```commandline
flake8
```

```commandline
isort . --interactive
```
