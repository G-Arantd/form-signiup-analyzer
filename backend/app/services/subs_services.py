from flask import jsonify
from app.models.Subs import Subs, db
from app.services.events_services import read_event

import pandas as pd
import os

def read_sub(id: int):
        try:
            sub = Subs.query.filter_by(subs_id=id).first()

            if not sub:
                return False

            return {"subs_id": sub.subs_id, "fullname": sub.fullname, "cpf": sub.cpf, "event": sub.event.events_name}

        except Exception as err:
            raise ValueError("Não foi possível encontrar essa inscrição")

def read_subs():
    try:
        subs = Subs.query.all()

        if not subs:
            return False
        
        subs_list = []

        if subs:

            for sub in subs:
                subs_list.append({
                    "subs_id": sub.subs_id,
                    "fullname": sub.fullname,
                    "cpf": sub.cpf,
                    "event_id": sub.subs_event_id
                })

        else:
            return subs_list

        return subs_list

    
    except Exception as err:
        raise ValueError("Não foi possível buscar informações no banco")
    
def create_subs(data):

    file_path = data.get("file_path")
    event_id = data.get("event_id")

    if not file_path or not os.path.exists(file_path):
        raise ValueError("Arquivo não existe ou não encontrado")
    
    if event_id:
        find_event = read_event(event_id)

        if not find_event:
            raise ValueError("Evento informado não existe no sistema")

    df = pd.read_csv(file_path)

    data_list = []
    
    for i in range(0, df.shape[0]):
    
        data_json = {
            "date": df["Carimbo de data/hora"].tolist()[i],
            "terms": df["Você está de acordo com os termos de uso:"].tolist()[i],
            "fullname": df["Nome Completo:"].tolist()[i],
            "cpf": df["CPF:"].tolist()[i],
            "phone": df["Telefone:"].tolist()[i],
            "placework": df["Local de Trabalho:"].tolist()[i],
            "role": df["Qual seu Cargo:"].tolist()[i]
        }

        data_list.append(data_json)

        print(data_list)

    return {"Importação csv feita com sucesso"}
    
    try:
        subs = [Subs(json_data.get("fullname"), json_data.get("cpf"), json_data.get("event_id")) for json_data in json_datas]
        db.session.bulk_save_objects(subs)
        db.session.commit()

    
    except Exception as err:
        db.session.rollback()
        raise ValueError("Não foi possível salvar as inscrições")
    
def delete_sub(id: int):

    sub = Subs.query.filter_by(subs_id=id).first()

    if sub:
        try:
            db.session.delete(sub)
            db.session.commit()
            
            return True
        
        except Exception as e:
            
            db.session.rollback()
            raise ValueError("Não foi possível deletar este inscrição")
    
    else:
        return False

def delete_all_subs():

    try:
        result = Subs.query.delete()
        
        if not result:
            return False
        
        db.session.commit()

        return True

    except Exception as err:
        db.session.rollback()
        raise ValueError("Não foi possível deletar todas as inscrições")