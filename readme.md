

## Postgresql 
- In PostgreSQL make sure you create a database called translation_db.
- create a user myuser with password mypassword and grant him all privileges to translation_db database

## Redis

install dependencies

```bash
pip install -r requirements.txt

```


run redis
```bash
sudo service redis-server start
```

## Fastapi

```
uvicorn app.main:app --reload
```

## Postman
test endpoints


in postman send a POST request to
```
http://127.0.0.1:8000/translate
```
using a raw body such as 
```
{
  "text": "Félicitations"
}
```
use any word from the mock json translation file mock_translation.db














