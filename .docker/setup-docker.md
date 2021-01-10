## Docker

- Place the file `local_settings.py` in `dmoj/`. You can make a copy [of this sample settings file](https://github.com/DMOJ/docs/blob/master/sample_files/local_settings.py) and modify it. Take into account that many default values won't work with this docker setup.
- Build: `docker-compose build`
- Run: `docker-compose up -d`
- First time initialization of DB: `docker-compose exec site ./init_db.sh`

Keep in mind that when DB is initialized, a default superuser account is created with a username and password of `admin`.
