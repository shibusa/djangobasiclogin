# Django Basic Login

Barebones standard login registration page written in Python with Django framework. Login/Registration/Logout html are templated allowing them to be embedded in other pages as needed.

### Requirements:
- Django 1.11.3
- [Supported Python version](https://docs.djangoproject.com/en/1.11/faq/install/#faq-python-version-support)

### Demo Purposes:
1. Install dependencies found in 'requirements.txt'
```
pip install -r requirements.txt
```
2. Make migrations
```
./manage.py makemigrations
./manage.py migrate
```
3. Start server
```
./manage.py runserver
```
4. Visit 127.0.0.1:8000 in a web browser

### Installation:
1. Install dependencies found in 'requirements.txt'
```
pip install requirements.txt
```
2. Move login app to your base project folder housing manage.py and sub project folder
3. Add app to 'INSTALLED_APPS = []' section of {sub project folder}/settings.py
4. Adjust routes accordingly in {sub project folder}/urls.py
5. Adjust paths accordingly in login/views.py
6. Adjust paths accordingly in login/templates/login/{htmlpage}.html
