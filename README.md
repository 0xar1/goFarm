# WebApp
 To install the requirments:
    
```bash
pip3 install -r requirements.txt
```
 To run the project: 

```bash
python3 main.py
```
OR to run using flask run, 
On Windows:

```bash
SET FLASK_APP=main.py
##for development purpose add SET FLASK_DEBUG=TRUE
flask run
```
On Linux:

```bash
EXPORT FLASK_APP=main.py
##for development purpose add EXPORT FLASK_DEBUG=TRUE
flask run
```
## Viewing The App

Go to `http://127.0.0.1:5000`

After making changes in the db 
```bash
##only first flask db init
flask db migrate -m "Changed"
flask db upgrade 
flask db downgrade
```
SQLAlchemy add to db
```bash
##only first flask db init
a = User(email='a@mail.com',password='123')
db.session.add(a)
db.session.commit()
```