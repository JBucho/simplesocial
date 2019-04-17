# simplesocial

Simplesocial is a project created for training Django framework purpose.

It allows visitors to:
- create user account,
- see the groups and posts in it.

Groups might be created for certain topics their content would be about.

After signing in User is allowed to:
- join/leave the groups of User's interests,
- create new group with unique name if the group of certain interest doesn't exist
- write new posts in group of choice
- read/write comments to post

Visit: https://jbb.pythonanywhere.com/ to check it by yourself

NOTE: There is no email veryfication when creating account (on purpose).

## Installation

First, clone the repository:

```sh
git clone https://github.com/JBucho/simplesocial.git
```


Create new virtual environment:

e.g., using Conda environments
```sh
conda create -n newenv pip
```

Go to project directory:
```sh
cd .../simplesocial
```


Activate your newly created environment and run:
```sh
pip install -r requirements.txt
```

Once installation of the dependencies is finished:

NOTE: There is not `db.sqlite3` file attached, so what is needed to do next is to make migration.

```sh
python manage.py migrate
```
During migration there will be .secret_key file created.
This file will be storing your unique SECRET_KEY value to use it in settings.py


(This step will let you to Log In without going through "Sign Up" form and will create
account with administrator privileges)
Create superuser:
```sh
python manage.py createsuperuser
```

After having superuser created the last step is to runserver:
```sh
python manage.py runserver
```

Only thing left to do is to open `http://127.0.0.1:8000/` in your browser.

## License
[MIT]https://github.com/JBucho/simplesocial/blob/master/LICENSE
