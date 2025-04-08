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
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)
