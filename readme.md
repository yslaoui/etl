
in posgresql make sure you create a database translation_db. create a user myuser with password mypassword and grant him all privileges to translation_db 

run redis
uvicorn app.main:app --reload


run the app

uvicorn app.main:app --reload














