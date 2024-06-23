from app import db

class Events(db.Model):
    __tablename__ = "tb_events"
    event_id: int = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_name: str = db.Column(db.String(100), nullable=False)

    def __init__ (self, event_name: str):
        self.event_name: str = event_name

    def __repr__(self) -> str:
        return "{"+f"event_id:{self.event_id},event_name:{self.event_name}"+"}"