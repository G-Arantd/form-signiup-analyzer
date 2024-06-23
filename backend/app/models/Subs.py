from app import db

class Subs(db.Model):
    __tablename__ = "tb_subs"
    subs_id: int = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fullname: str = db.Column(db.String(100), nullable=False)
    cpf: str = db.Column(db.String(14), nullable=False)

    subs_event_id = db.Column(db.Integer, db.ForeignKey('tb_events.event_id'))
    
    event = db.relationship('Events', foreign_keys=[subs_event_id])

    def __init__ (self, fullname: str, cpf: str, subs_event_id:int):
        self.fullname: str = fullname
        self.cpf: str = cpf
        self.event_id: int = subs_event_id

    def __repr__(self) -> str:
        return "{"+f"subs_id:{self.subs_id},full_name:{self.fullname},cpf:{self.cpf},event_id:{self.subs_event_id}"+"}"