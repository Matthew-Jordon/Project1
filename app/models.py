from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'property'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    beds = db.Column(db.Integer())
    baths = db.Column(db.Integer())
    type = db.Column(db.String(10))
    location = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer())
    pic = db.Column(db.String(80))

    def __init__(self, title, beds, baths, type, location, price, description, pic):
        self.title = title
        self.beds = beds
        self.baths = baths
        self.location = location
        self.price = price
        self.description = description
        self.pic = pic
        self.type = type

    def __repr__(self):
        return '<ID %r>' % (self.id)
