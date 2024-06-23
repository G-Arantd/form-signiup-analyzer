
from app import db

class Roles(db.Model):
    __tablename__ = "tb_roles"
    role_id: int = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role_name: str = db.Column(db.String(100), nullable=False)

    def __init__ (self, role_name: str):
        self.role_name: str = role_name

    def __repr__(self) -> str:
       return "{"+f"role_id:{self.role_id},role_name:{self.role_name}"+"}"