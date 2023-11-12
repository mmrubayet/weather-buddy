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

#### Import District Data:

```commandline
python manage.py collectstatic
```
```commandline
python manage.py shell
```
Inside shell:
```commandline
from utilities import import_districts
```
```commandline
import_districts()
```
```commandline
exit()
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

### API Documentation:

#### API Endpoints:
| HTTP Verbs | Endpoints                                                            | Action                                                                                                  |
|------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| GET        | /api/v1/districts/                                                   | List and Create district.                                                                               |
| GET        | /api/v1/districts/<int:dist_id>/                                     | Retrieve, Update and Destroy district.                                                                  |
| GET        | /api/v1/districts/weather/temperature/                               | Returns Temperature at 2PM for 7 days 64 districts.                                                     |
| GET        | /api/v1/districts/weather/cool-ten/                                  | Returns Top Ten Cool Districts Based on Weather for an average of Next 7 Days at 2PM for 64 Districts.  |
| GET        | /api/v1/districts/travel/cool/?from_id=1&to_id=60&date=2023-11-12    | Takes Current and Desired Location with date and Returns the Desired is Cooler or Not.                  |
| GET        | /api/v1/districts/travel/cool/rt/?from_id=1&to_id=60&date=2023-11-12 | Takes Current and Desired Location with date and Returns the Desired is Cooler or Not. Without caching. |
| 