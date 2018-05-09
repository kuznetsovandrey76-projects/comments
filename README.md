1. В пустой дериктории 
	virtualenv env
2. cd env/Scripts
3. activate
4. Возвращаемся в основную директорию
5. pip install flask
6. touch project.py
7. mkdir templates 
8. touch templates/index.html
9. touch templates/sign.html
10. mkdir static # Добавляем в static папки css и js
11. touch static/css/style.css
12. pip install flask_sqlalchemy 
13. pip install psycopg2
14. Создаем новое приложени https://dashboard.heroku.com/apps
15. Заходим во вкладку Resources и добавляем Add-ons - Heroku Postgres
16. В https://data.heroku.com/ смотрим URI
17. Через cmd заходим в python
	from project import db (где project - название основного файла в директории (ex: project.py))
	db.create_all() (создает таблицу в базе данных - я использую pgAdmin 3)

18. touch Procfile
19. pip install gunicorn
20. pip freeze > requirements.txt