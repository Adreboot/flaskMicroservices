from . import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    author = db.Column(db.String(50))
    overview = db.Column(db.String(200))
    image = db.Column(db.String(200))
    url = db.Column(db.String(100))

    def toDict(self):
        return dict(id=self.id, title=self.title, author=self.author, overview=self.overview, image=self.image, url=self.url)