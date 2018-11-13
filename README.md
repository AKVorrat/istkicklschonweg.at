# istkicklschonweg.at

## Project Structure

```
istkicklschonweg.at/
├── django/         <- django root
│   ├── settings/       <- django settings
│   ├── templates/
│   ├── manage.py
│   └── urls.py         <- root url configuration
├── configs/        <- misc configs (nginx, etc.)
├── scripts/        <- helper scripts
├── run/
│   ├── static/          <- live static files
│   └── db.sqlite        <- dev database
└── README.md       <- this file
```

## Development

Initial Setup:

```bash
> git clone git@github.com:???
> cd istkicklschonweg.at/

> virtualenv .env
> source .env/bin/activate

> pip install -r requirements.txt

# You can add this to your .env/bin/activate script
# if you want it to persist
> export DJANGO_SETTINGS_MODULE=settings.dev

> cd django/

# Migrate 
> python ./manage.py migrate

# Create an admin account
> python ./manage.py createsuperuser
```

Running:

```bash

> python ./manage.py runserver

```

## Production Setup

Initially, just like the development setup although `DJANGO_SETTINGS_MODULE` will be provided by the `start_gunicorn.sh` script.

### TODO:
 - Test Nginx Config
 - Systemd?

## Strings

- EMail
    - Confirm
        - Subject
        - Body
    - Thanks ?

- Petition
    - Call to petition
    - Thanks

- Sündenliste