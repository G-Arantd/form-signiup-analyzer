from app.models.Events import Events, db

def read_event(id: int):
        try:
            event = Events.query.filter_by(event_id=id).first()

            if not event:
                return False

            return {"event_id": event.event_id, "event_name": event.event_name}

        except Exception as err:
            raise ValueError("Não foi possível encontrar esse evento")
        
def read_events():
    try:
        events = Events.query.all()

        if not events:
                return False
        
        events_list = []

        if events:

            for event in events:
                events_list.append({
                    "event_id": event.event_id,
                    "event_name": event.event_name
                })

        else:
            return events_list

        return events_list

    
    except Exception as err:
        raise ValueError("Não foi possível buscar informações no banco")
    
def create_event(data):

    if not data.get("event_name"):
        raise ValueError("Parametros JSON para criação incorretos")

    try:
        event = Events(data.get("event_name"))
        db.session.add(event)
        db.session.commit()

        return {"event_id": event.event_id, "event_name": event.event_name}
    
    except Exception as err:
        raise ValueError("Não foi possível salvar este evento")
    
def delete_event(id: int):

    event = Events.query.filter_by(event_id=id).first()

    if event:
        try:
            db.session.delete(event)
            db.session.commit()
            
            return True
        
        except Exception as e:
            
            db.session.rollback()
            raise ValueError("Não foi possível deletar este evento")
    
    else:
        return False

def delete_all_event():

    try:
        result = Events.query.delete()
        
        if not result:
            return False

        db.session.commit()
        
        return True

    except Exception as err:
        raise ValueError("Não foi possível deletar todos os eventos")
