from project import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Profession(db.Model):
    __tablename__ = 'Profession'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    campaignId = db.Column(db.Integer)

    def __init__(self, name, campaignid):
        self.name = name
        self.campaignId = campaignid        

class SpecialtyGroup(db.Model):
    __tablename__ = 'SpecialtyGroup'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    campaignId = db.Column(db.Integer)

    def __init__(self, name, campaignid):
        self.name = name
        self.campaignId = campaignid                

class GeoRegions(db.Model):
    __tablename__ = 'GeoRegion'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    campaignId = db.Column(db.Integer)

    def __init__(self, name, campaignid):
        self.name = name
        self.campaignId = campaignid                        

class Segment(db.Model):
    __tablename__ = 'Segment'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    campaignId = db.Column(db.Integer)

    def __init__(self, name, campaignid):
        self.name = name
        self.campaignId = campaignid                        