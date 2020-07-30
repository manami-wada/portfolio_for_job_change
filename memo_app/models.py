from app import db

class Memo(db.Model):
    __tablename__ = 'memos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    detail = db.Column(db.String(255))

    def __init__(self, title, detail):
        self.title = title
        self.detail = detail

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'title': self.title,
            'detail': self.detail
        }