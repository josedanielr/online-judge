## Docker

- Build: `docker-compose build`
- Run: `docker-compose up -d`
- First time initialization of DB: `docker-compose exec site ./init_db.sh`

Keep in mind that when DB is initialized, a default superuser account is created with a username and password of `admin`.
