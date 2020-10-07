## Usage

* Virtualenv

```
pyenv virtualenv 3.8.0 django-to-do
pyenv activate django-to-do
```

* Project

```
pip install -r requirements.txt 
python todo/manage.py migrate
python todo/manage.py runserver
```

* Playwright

```
pip install playwright
python -m playwright install
```

* Run tests

```
python todo/manage.py test tasks.tests
```
