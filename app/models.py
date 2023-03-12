from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    desc = db.Column(db.Text())
    bedsno = db.Column(db.Integer)
    bathsno = db.Column(db.Integer)
    price = db.Column(db.String(30))
    propertytype = db.Column(db.String(20))
    location = db.Column(db.String(200), unique=False)
    pic = db.Column(db.String())

    def __init__(self, title, desc, bedsno, bathsno, price, propertytype, location, pic):
        self.title = title
        self.desc = desc
        self.bedsno = bedsno
        self.bathsno = bathsno
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.pic = pic

    def __repr__(self):
        return '<Property %r>' % (self.title)