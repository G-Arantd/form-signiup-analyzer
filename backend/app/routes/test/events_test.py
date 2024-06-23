from flask import jsonify
from app import app
from app.services.events_services import read_event, create_event, delete_all_event, delete_event

@app.route("/events-test", methods=["GET"])
def event_test():

    NAMES_ERROR = ["CREATE_EVENT", "READ_EVENT", "DELETE_EVENT"]

    error_list = []

    data_event = {"event_name": "Evento Teste"}

    event = create_event(data_event)

    if not event:
        error_list.append(NAMES_ERROR[0])
    
    event_read = read_event(event.get("event_id"))
    
    if event_read.get("event_id") != event.get("event_id"):
        error_list.append(NAMES_ERROR[1])

    event_delete = delete_event(event.get("event_id"))

    if not event_delete:
        error_list.append(NAMES_ERROR[2])

    if error_list:
        return jsonify({"errors": error_list})
    else:
        return jsonify({"message": "Foi realizado todos os procedimentos com sucesso"})