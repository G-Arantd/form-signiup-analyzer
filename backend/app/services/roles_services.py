from app.models.Roles import Roles, db

def read_role(id: int):
        try:
            role = Roles.query.filter_by(role_id=id).first()

            if not role:
                return False

            return {"role_id": role.role_id, "role_name": role.role_name}

        except Exception as err:
            raise ValueError("Não foi possível encontrar esse cargo")
    
def read_roles():
    try:
        roles = Roles.query.all()

        if not roles:
            return False
        
        roles_list = []

        if roles:

            for role in roles:
                roles_list.append({
                    "role_id": role.role_id,
                    "role_name": role.role_name
                })

        else:
            return roles_list

        return roles_list

    
    except Exception as err:
        raise ValueError("Não foi possível buscar informações no banco")
    
def create_role(data: dict):

    try:
        role  = Roles(data.get("role_name"))
        db.session.add(role)
        db.session.commit()

        return {"role_id": role.role_id, "role_name": role.role_name}
    
    except Exception as err:
        raise ValueError("Não foi possível salvar este cargo")
    
def delete_role(id: int):

    role = Roles.query.filter_by(role_id=id).first()

    if role:
        try:
            db.session.delete(role)
            db.session.commit()
            
            return True
            
        except Exception as e:
            
            db.session.rollback()
            raise ValueError("Não foi possível deletar este cargo")

    else:
        return False

def delete_all_roles():

    try:
        result = Roles.query.delete()
        
        if not result:
            return False
        
        db.session.commit()

        return True

    except Exception as err:
        raise ValueError("Não foi possível deletar todos os cargos")