# mephi_backend

# Чтобы запустить надо написать там где лежит весь проект:
```
python manage.py runserver
```

# Все что нужно поставить 

В лабе делалось с виртуальным окружением так что пусть будет с виртуальным

```
sudo apt install python3.10-venv
python -m venv .venv
. .venv/bin/activate
python -m pip install Django~=4.2
python -m pip install django-debug-toolbar
pip install psycopg2-binary
python -m pip install faker
pip install django-bootstrap5
python3 manage.py migrate
```
# Если траблы с постгрей при миграции то надо создать пользователя сделать его суперпользователем и создать бд:

To create a new user:
```
sudo -u postgres createuser --interactive
```
To reset the password for "mydatabaseuser":
```
sudo -u postgres psql
```
And then in the psql shell:

```
ALTER USER mydatabaseuser PASSWORD 'my_password';
```
Create DB
```
psql -U mydatabaseuser
CREATE DATABASE mydatabase;
```
Вроде все расписал если будут траблы можете конечно написать но не факт что я помню как они фиксились (еще вылетает ошибка в консоли по поводу favicon.ico на нее я забил хуй)

