from app import db
from sqlalchemy.dialects.postgresql import JSON

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body=db.Column(db.String(1000))
    date=db.Column(db.Date)
    featured=db.Column(db.Boolean())
    links_rel = db.relationship('Links', backref='owner')
    tags = db.relationship('Tags', backref='owner1')

    def __init__(self, title, body,date=None):
        self.title=title
        self.body=body
        self.date=date
        self.featured=False

class Links(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    urlTitle= db.Column(db.String(120))
    url= db.Column(db.String(120))
    owner_links_id = db.Column(db.Integer, db.ForeignKey('news.id'))

    def __init__(self, urlTitle,url,owner1):
        self.url=urlTitle
        self.url=url
        self.owner=owner

class Tags(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    tagTitle= db.Column(db.String(120), unique=True)
    owner_tags_id=db.Column(db.Integer, db.ForeignKey('news.id'))

    def __init__(self, tagTitle,owner):
        self.tagTitle=tagTitle
        self.owner=owner

class ContactForm(Form):
    name = StringField('Name (required): ', [validators.DataRequired('Please enter your name')])
    email = StringField('Email (required): ',[validators.Email('Please enter a valid email')])
    subject = StringField('Subject (Optional): ')
    message =  TextAreaField('Message (required): ',[validators.DataRequired('Please enter a message')])
    submit= SubmitField('Submit')
