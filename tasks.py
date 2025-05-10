from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.dbtasks'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(300))
    date_of_visit = db.Column(db.String(300))

    def __repr__(self):
        return f'Product{self.city_name}: {self.date_of_visit}'


@app.route('/')
def main():
    cities = City.query.all()
    return render_template('tasks.html', cities_list=cities)


@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    city = City(**data)
    db.session.add(city)
    db.session.commit()
    return 'OK'

@app.route('/delete', methods=['delete'])
def delete_product():
    db.session.query(City).delete()
    db.session.commit()
    return '', 204



with app.app_context():
    db.create_all()
app.run(debug=True)