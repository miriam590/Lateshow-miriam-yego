from flask import Flask
from extensions import db, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate.init_app(app, db)

# Import routes after db initialization
from routes import *

if __name__ == '__main__':
    app.run(port=5555, debug=True)
