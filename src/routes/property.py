from flask import Blueprint, jsonify
from models.property_model import PropertyModel
from flask import request
from models.entities.property import Property
import pickle
import numpy as np
from src.utils.validation import validate_data

ml_model = pickle.load(
    open("./src/ml-model/ml-model.pkl", "rb"))
main = Blueprint("property_blueprint", __name__)


# get methods
@main.route("/user/<user_id>")
def list_user_properties(user_id):
    try:
        # funcion que valida
        properties = PropertyModel.get_all_properties(user_id)
        return jsonify(properties)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/property/<property_id>")
def property_by_id(property_id):
    try:
        prop = PropertyModel.get_property_by_id(property_id)
        if prop != None:
            return jsonify(prop)
        return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/property")
def get_properties_by_barrio():
    user_id = request.args.get("user_id")
    barrio = request.args.get("barrio")
    try:
        properties = PropertyModel.get_property_by_barrio(user_id, barrio)
        return jsonify(properties)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


# post methods
@main.route("/add", methods=["POST"])
def add_property():
    data = request.json
    try:
        if validate_data(data) == True:
            prop = Property(
                data["id"],
                data["barrio"],
                data["estrato"],
                data["direccion"],
                data["nivel_propiedad"],
                data["antiguedad"],
                data["area_propiedad"],
                data["numero_habitaciones"],
                data["garage"],
                data["numero_banos"],
                data["numero_pisos"],
                data["tipo_cocina"],
                data["owner"],
            )
            affected_rows = PropertyModel.add_property(prop)
            if affected_rows == 1:
                return jsonify(prop.id)
            return jsonify({"message": "Error inserting property"}), 500
        return jsonify({"message": "Error with the data types"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/predict", methods=["POST"])
def predict_price():
    try:
        features = request.json
        features = np.array(list(features.values()))
        prediction = ml_model.predict(np.array(features).reshape(1, -1))
        print(prediction)
        return jsonify({"El precio es: ": prediction[0]}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


# patch method
@main.route("/update/<property_id>", methods=["PATCH"])
def update_property(property_id):
    data = request.get_json()
    try:
        prop = Property(
            property_id,
            data["barrio"],
            data["estrato"],
            data["direccion"],
            data["nivel_propiedad"],
            data["antiguedad"],
            data["area_propiedad"],
            data["numero_habitaciones"],
            data["garage"],
            data["numero_banos"],
            data["numero_pisos"],
            data["tipo_cocina"],
            data["owner"],
        )
        # FUNCION QUE VALIDA
        affected_rows = PropertyModel.update_property(prop)

        if affected_rows == 1:
            return jsonify(prop.id)
        return jsonify({"message": "Error updating property"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


# delete method
@main.route("/delete/<property_id>", methods=["DELETE"])
def delete_property(property_id):
    try:
        prop = Property(property_id)
        affected_rows = PropertyModel.delete_property(prop)

        if affected_rows == 1:
            return jsonify(prop.id)
        return jsonify({"message": "No property deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/otherFilter")
def get_property_by_estrato():
    user_id = request.args.get("user_id")
    estrato = request.args.get("estrato")
    try:
        properties = PropertyModel.get_property_by_estrato(user_id, estrato)
        return jsonify(properties)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
