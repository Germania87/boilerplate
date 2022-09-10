Boilerplate Flask Final

Entorno virtual

Creación

python -m venv venv



Activar

source venv/Scripts/activate -> Windows
source venv/bin/activate -> Linux / MacOS



Dependencias




Crear requirements (Ejecutar siempre que se instale una dependencia)

pip freeze > requirements.txt



Variables de Entorno

FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_DEBUG=true

DATABASE_URI='postgresql://postgres:mysql@localhost:5432/flask_boilerplate'

Migración

flask db init -> Iniciamos nuestras migraciones (una sola vez)



flask db migrate -m "Comentario" -> De esta manera creamos nuestras migraciones



flask db upgrade -> Ejecutar las migraciones


Flask Restx

Validar y documentar los query params, headers y form data


https://flask-restx.readthedocs.io/en/latest/parsing.html



Validar y documentar los request body


https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html



Configuración de JWT


https://flask-jwt-extended.readthedocs.io/en/stable/options/#general-options


Tipos de datos en los Modelos (SQLAlchemy)


https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=true # cifrado de correo
MAIL_USERNAME='germaniatoro87@gmail.com'
MAIL_PASSWORD='pzdvcujgxwailhvc'