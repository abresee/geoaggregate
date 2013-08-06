Geoaggregate is based on GeoDjango and PostGIS, and is developed with the
intention of using a Python 3 interpreter (python 2 is going away!). So, to use
Geoaggregate, you need a few things:
* __Postgresql__
* __PostGIS__
* __Python 3__
* __Django 1.5__ or greater (since 1.5's python 3 support is experimental, as soon
as 1.6 is released it will be the base version)
* __psycopg__ (to allow python to talk to postgres)
* __numpy__, __scipy__, __matplotlib__, and __ipython__ are used for interactive
work and scientific processing

The simplest way to get all this stuff working is to use [[virtualenv]] (and,
if you're in an environment where bash is available [Apple's OS X, GNU/Linux (or
whatever), Windows via Cygwin], [[virtualenvwrapper]]).

# Installation Instructions
Instructions are provided for Ubuntu and Arch Linux right now (since that's what
I have available -- more will come later!)

###Install basic packages!
Install __PostgreSQL__, __PostGIS__, __Python 3__, __psycopg2__, __virtualenv__,__numpy__, __scipy__, __matplotlib__ and optionally __virtualenvwrapper__ if 
you're using an environment that supports it. 
####Ubuntu:  
TODO: command to install that stuff under ubuntu -- off the top of my head, it's 
``` shell
sudo apt-get install postgresql postgis python3-{dev,psycopg2,virtualenv} \
virtualenvwrapper
```
... but that's probably off and I just need to sit down for a second at an ubuntu
machine (i.e. get a virtual one installed already sheesh)
####Arch Linux:

``` shell
sudo pacman -S postgresql postgis \
python{,-{psycopg2,virtualenv,virtualenvwrapper,numpy,scipy,matplotlib}}
```

TODO: I've had issues with Arch's package of postgis version 2.0.3. Need to 
investigate if this issue still exists, and if it does, provide instructions for
using the Arch Rollback Machine to install 2.0.2 (it's not hard)

### Setup a project environment!
There's definitely a more convenient way to have this rigged up, but this is the 
process I have for now (hint hint let's make this less bad soon)
right now I'm assuming you have virtualenvwrapper because like why wouldn't you.
If you're on windows without cygwin I'm not gonna be able to help you (yet!).

You need to define the shell variable `PROJECT_HOME` to point to a directory 
where you're keeping your project(s). I use `$HOME/projects`, so I have a line 
in my `.zshrc`:

``` shell
export PROJECT_HOME=$HOME/projects
```

with that variable defined, just do:

``` shell
~ $ mkproject --system-site-packages geoagg -p `which python3`
``` 
You can name the project whatever you want, doesn't need to be geoagg.

if you're on Arch, or if you otherwise have a system where `python` refers to 
python 3, everthing after `geoagg` is unecessary (but couldn't hurt really!). 
the `--system-site-packages` bit is there because I've had issues with getting
all the required python subpackages to install nicely all inside the virtualenv,
so I use the system packages for everything except django and ipython (installed
in my case via Arch's __pacman__).

### Clone the repo!
Now that you have a python 3 virtualenv with a project folder, clone the repo!
``` shell
~ $ git clone https://github.com/abresee/geoaggregate.git $PROJECT_HOME/geoagg
```

That will clone into the project dir from before. use a different second arg to
`git clone` if you need a different location.

now, install the submodules you need! __Django__ is all you need, but i like to
have my ipython installed in my env too (rather than installed on system-wide).
You can actually install this as a system level package if you want, but since
__Django__ is critical and a new release is coming soon it makes more sense to 
me to have as a virtualenv package.
``` shell
(geoagg) $ pip install django
``` 
