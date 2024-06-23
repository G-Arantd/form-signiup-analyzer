from app import db

class Placeworks(db.Model):
    __tablename__ = "tb_placeworks"
    placework_id: int = db.Column(db.Integer, autoincrement=True, primary_key=True)
    placework_name: str = db.Column(db.String(100), nullable=False)

    def __init__ (self, placework_name: str):
        self.placework_name: str = placework_name

    def __repr__(self) -> str:
        return "{"+f"placework_id:{self.placework_id},placework_name:{self.placework_name}"+"}"