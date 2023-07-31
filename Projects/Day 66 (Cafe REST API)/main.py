from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """
        :param self:
        :return: dict
        This function return a dictionary with all information about a Cafe data as a dictionary
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    all_cafes_json = {}
    i = 0
    for cafe in all_cafes:
        all_cafes_json[i] = cafe.to_dict()
        i += 1
    return jsonify(all_cafes_json)


@app.route("/search", methods=["GET"])
def search_cafe():
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    search_cafes = result.scalars().all()
    if search_cafes:
        search_cafes_json = {}
        i = 0
        for cafe in search_cafes:
            search_cafes_json[i] = cafe.to_dict()
            i += 1
        return jsonify(search_cafes_json)
    return jsonify(
        error={
            "Not Found": "Sorry, we don't have a cafe at that location"
        }
    )


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    cafe_to_update.coffee_price = request.args.get("new_price")
    db.session.commit()
    return jsonify(response={"success": "Successfully updated he coffee's price."}), 200


@app.route("/delete/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    user_api_key = request.args.get("api_key")
    reference_api_key = "TopSecretApiKey"
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    if user_api_key == reference_api_key:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully delete the cafe."})
    else:
        return jsonify(error={"Not Authorized": "ApiKey not authorized to perform deletion"}), 403


if __name__ == '__main__':
    app.run(debug=True)
