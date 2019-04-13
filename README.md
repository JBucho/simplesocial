# simplesocial

Simplesocial is a project created for training Django framework purpose.

It allows visitors to:
- create user account,
- see the groups and posts in it.

Groups might be created for certain topics their content is about.

After signing in User is allowed to:
- join/leave the groups of User's interests,
- create new group with unique name if the group of certain interest doesn't exist
- write new posts in group of choice

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

Activate your newly created environment and run:
```sh
pip install -r requirements.txt
```

Once installation of the dependencies is finished:

```sh
python manage.py runserver
```

The last thing is to open `http://127.0.0.1:8000/` in your browser.

## License
[MIT]https://github.com/JBucho/simplesocial/blob/master/LICENSE