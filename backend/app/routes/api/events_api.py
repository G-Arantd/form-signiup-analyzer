from flask import request, jsonify
from app import app
from app.services.events_services import read_event, read_events, create_event, delete_event, delete_all_event

@app.route("/event/<int:id>", methods=["GET"])
def event_get(id):

    result = read_event(id)

    if result:
        return jsonify({"sucess":True, "data": result}), 200
    else:
        return jsonify({"sucess":True, "message": "Não existe o evento informado"}), 200

@app.route("/list/events", methods=["GET"])
def list_events():

    result = read_events()

    if result:
        return jsonify({"sucess":True, "data": result}), 200
    else:
        return jsonify({"sucess":True, "message": "Não existe eventos salvos"}), 200

@app.route("/event", methods=["POST"])
def event_create():

    data = request.json

    result = create_event(data)

    return jsonify({"sucess":True, "data": result, "message": "Evento criado com sucesso"}), 200

@app.route("/event/<int:id>", methods=["DELETE"])
def event_delete(id):

    result = delete_event(id)

    if result:
        message = "Evento deletado com sucesso"
    else:
        message = "Não existe evento para ser deletado"

    return jsonify({"sucess":True, "message": message}), 200

@app.route("/events/delete", methods=["DELETE"])
def events_all_delete():

    result = delete_all_event()

    if result:
        message = "Eventos deletados com sucesso"
    else:
        message = "Não existe eventos para serem deletados"

    return jsonify({"sucess":True, "message": message}), 200