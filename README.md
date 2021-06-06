# IT-WebTech studio
## Requirements:
1) Python > 3.8 ([Installation guide](https://www.python.org/downloads/))
2) Installed `pip` ([Installation guide](https://pip.pypa.io/en/latest/installing/))
3) Installed `virtualenv` (command to install: `pip install virtualenv`)
4) Installed `git` ([Installation guide](https://www.linode.com/docs/guides/how-to-install-git-on-linux-mac-and-windows/))

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/DiZiNnEs/web-tech-studio-backend
$ cd web-tech-studio-backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/` (the page will be empty no big deal keep reading).

Admin panel `http://127.0.0.1:8000/admin`
and enter the name with the superuser password created earlier.

Next, create the data you need in the admin panel.
