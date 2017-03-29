# Pgcrypto Avast!

## A case-study in Django's password hashers

This repository is meant to be a companion to my talk entitled _Pgcrypto Avast! A case-study in Django's password hashers._ It contains example code and data that are referenced in the presentation, as well as a sample Django project for demonstration purposes.

### Contents

- ./hashes
    - Example md5 and md5crypt hashed passwords.
- ./python
    - Python scripts for various hashing/cracking activities.
- ./rainbow-tables
    - A generated md5 rainbow table for all 4 character alphanumeric passwords.
- ./sample_django_project
    - An example Django project.
- ./sql
    - SQL scripts used in the demo.


### Running the sample Django project

- Use Python 3
- Install dependencies (in virtualenv): `pip install requirements.txt`
- Configure your Postgres database in an env variable
    - `export DATABASE_URL=postgres://[user]:[pwd]@[host]:[port]/[dbname]`
- Run database migration: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Run it: `python manage.py runserver`
- Open http://localhost:8000/admin/ in browser


### Helpful Resources


#### PostgreSQL links

- [Pgcrypto cryptographic functions for PostgreSQL](https://www.postgresql.org/docs/current/static/pgcrypto.html)



#### Django links

- [Writing an authentication backend](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#writing-an-authentication-backend)
- [Writing your own hasher](https://docs.djangoproject.com/en/1.11/topics/auth/passwords/#writing-your-own-hasher)


#### Cracking passwords

- [John the Ripper password cracker](http://www.openwall.com/john/)
- [Getting Started Cracking Password Hashes With John the Ripper](https://www.tunnelsup.com/getting-started-cracking-password-hashes/)
- [Brute force calculator](http://calc.opensecurityresearch.com/)
