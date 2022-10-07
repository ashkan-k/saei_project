#### to create permissions
```bash
./manage.py init_permissions
```

#### to create default roles and sync their permissions
```bash
./manage.py init_roles
```

#### to create default settings and statics
```bash
./manage.py init_settings
```


```bash test database
$ sudo su - postgres
$ psql

CREATE DATABASE sae_project_testdb;
CREATE USER sae_project_testuser WITH PASSWORD 'sae_project_password';
ALTER ROLE sae_project_testuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE sae_project_testuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sae_project_testdb TO sae_project_testuser;
ALTER USER sae_project_testuser WITH SUPERUSER;

\q

exit;