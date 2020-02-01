

class User(db.Model):
    id = db.Column(db.Integer.primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"Usernam={self.username},email={self.email}"
    


class Item(db.Model):
    id = db.Column(db.Integer.primary_key = True)
    image_file = db.Column(db.String(30), unique = True, nullable = False)