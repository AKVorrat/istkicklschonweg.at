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

???

### TODO:
 - Test Nginx Config
 - Systemd?

## Colors
- Red
    - #FF2833
    - #CC252F
    - #D6222B

- Grey
    - #F0F0F0
    - #232323

- Text
    - #F0F0F0 (on red or dark grey)
    - #A3A3A3 (on light grey)

## Strings
- Unterüberschrift?

- EMail
    - Confirm
        - Subject
        - Body
    - Thanks ?

- Petition
    - Einleitender Text
    - Danke
    - Bestätigung (S)

- Sündenliste
    - Einleitender Text
    - Die Liste
