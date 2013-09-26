### Install basic packages with ArchLinux

pacman packages: 
``` shell
git postgresql postgis nodejs ipython \
python{,-{django,south,psycopg2,virtualenv,numpy,scipy,matplotlib}}
```
node packages:

* coffee-script
```
sudo npm -g install coffee-script
~> mkdir venv
~> virtualenv --system-site-packages venv/geoagg
~> . ~/venv/geoagg/bin/activate.fish
(geoagg)~> pip install gunicorn
(geoagg)~> deactivate

# Setup postgres and postgis
systemd-tmpfiles --create postgresql.conf
mkdir /var/lib/postgres/data
chown -c -R postgres:postgres /var/lib/postgres

su - postgres
initdb -D '/var/lib/postgres/data'
createuser -s --interactive 
exit
createdb geoaggregate
psql -c 'CREATE EXTENSION postgis;' geoaggregate
systemctl enable postgresql
systemctl start postgresql

~> cd projects
~/projects> git clone https://github.com/abresee/geoaggregate.git 
~/projects> cd geoaggregate
~/projects/geoaggregate> . ~/venv/geoagg/bin/activate.fish
cake tiger
python manage.py syncdb
python manage.py shell
%run tiger/load.py
exit


```
now, to run the demo, 
```
cd projects/geoaggregate
. ~/venv/geoagg/bin/activate.fish
python manage.py runserver
```