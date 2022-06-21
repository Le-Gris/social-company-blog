from social_company_blog import db

class User():

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    email = None
    pass


class BlogPost():
    pass