# Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/DaniilLevchenko/REST_API.git
cd rest_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
python -m venv venv
cd venv/scripts
.\activate
cd ..
cd ..
```

Then install the dependencies:
```sh
pip install -r requirements.txt
```

Once pip has finished downloading the dependencies:
```sh
python manage.py runserver
```
