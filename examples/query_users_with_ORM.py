'''
Use ORM to query users within an activate application context

See:

https://flask-sqlalchemy.readthedocs.io/en/stable/queries/
https://docs.sqlalchemy.org/en/14/orm/queryguide.html#select-statements
'''

from invenio_accounts.models import User
from invenio_db import db
from invenio_factory_patch.factory import create_app

app = create_app()

with app.app_context():
    results = db.session.execute(db.select(User.username, User.email)).all()

for result in results:
    print(f"username: {result[0]}, email: {result[1]}")

    


    


