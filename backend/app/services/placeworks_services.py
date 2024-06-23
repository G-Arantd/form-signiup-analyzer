from app.models.Placeworks import Placeworks, db

def read_placework(id: int):
        try:
            placework = Placeworks.query.filter_by(placework_id=id).first()

            if not placework:
                return False

            return {"placework_id": placework.placework_id, "placework_name": placework.placework_name}

        except Exception as err:
            raise ValueError("Não foi possível encontrar esse local de trabalho")
    
def read_placeworks():
    try:
        placeworks = Placeworks.query.all()

        if not placework:
            return False
        
        placeworks_list = []

        if placeworks:

            for placework in placeworks:
                placeworks_list.append({
                    "placework_id": placework.placework_id,
                    "placework_name": placework.placework_name
                })

        else:
            return placeworks_list

        return placeworks_list

    
    except Exception as err:
        raise ValueError("Não foi possível buscar informações no banco")
        
def create_placework(data: dict):

    try:
        placework  = Placeworks(data.get("placework_name"))
        db.session.add(placework)
        db.session.commit()

        return {"placework_id": placework.placework_id, "placework_name": placework.placework_name}
    
    except Exception as err:
        raise ValueError("Não foi possível salvar este local de trabalho")
    
def delete_placework(id: int):

    placework = Placeworks.query.filter_by(placework_id=id).first()

    if placework:
        try:
            db.session.delete(placework)
            db.session.commit()

            return True
        
        except Exception as e:
            
            db.session.rollback()
            raise ValueError("Não foi possível deletar este local de trabalho")
    
    else:
        return False

def delete_all_placeworks():

    try:
        result = Placeworks.query.delete()
        
        if not result:
            return False
        
        db.session.commit()

        return True

    except Exception as err:
        raise ValueError("Não foi possível deletar todos os locais de trabalho")