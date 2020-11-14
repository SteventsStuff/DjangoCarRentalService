# Django Car Rental Service

## Short Description

This is my university project. The main purpose was - create web service with functionality for 
login/register and CRUD cars, divers functionality. 


## How to run it locally

1. Install MySQL DB and create DB with name 'rental_db';
2. Set up all ENV vars;
3. Install all necessary python libs: `pip3 install -e requirements.txt`;
4. Make all migrations: 
        ```
        python3 manage.py migrate rental
        python3 manage.py migrate users 
        ```;
5. Create admin for this service: `python manage.py createsuperuser`;
6. You good to go at this point, run django server:  `python3 manage.py runserver`;
7. Go to http://127.0.0.1:8000;
8. Have fun.

---
### ENV vars
```
DB_USER=username
DB_PASSWORD=password
SECRET_KEY=key
```

 