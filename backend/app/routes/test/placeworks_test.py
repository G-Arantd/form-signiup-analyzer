from flask import jsonify
from app import app
from app.services.placeworks_services import read_placework, create_placework, delete_all_placeworks, delete_placework 

@app.route("/placeworks-test", methods=["GET"])
def placeworks_test():

    NAMES_ERROR = ["CREATE_PLACEWORK", "READ_PLACEWORK", "DELETE_PLACEWORK"]

    error_list = []

    data_placework = {"placework_name": "Local Teste"}

    placework = create_placework(data_placework)

    if not placework:
        error_list.append(NAMES_ERROR[0])
    
    placework_read = read_placework(placework.get("placework_id"))
    
    if placework_read.get("placework_id") != placework.get("placework_id"):
        error_list.append(NAMES_ERROR[1])

    placework_delete = delete_placework(placework.get("placework_id"))

    if not placework_delete:
        error_list.append(NAMES_ERROR[2])

    if error_list:
        return jsonify({"errors": error_list})
    else:
        return jsonify({"message": "Foi realizado todos os procedimentos com sucesso"})