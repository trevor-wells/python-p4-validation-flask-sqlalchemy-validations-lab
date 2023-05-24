from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("You must enter a name!")
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) != 10:
            raise ValueError("Phone number must be exactly 10 digits!")
        return number
    
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise IntegrityError("You must have a title!")
        return title
    
    @validates('content')
    def validate_post_content(self, key, text):
        if len(text) < 250:
            raise ValueError("Post content must be at least 250 characters long!")
        return text
    
    @validates('summary')
    def validate_post_summary(self, key, text):
        if len(text) > 250:
            raise ValueError("Post summary must be 250 characters or less!")
        return text
    
    @validates('category')
    def validate_category(self, key, cat):
        if cat != 'Fiction' or cat != 'Non-Fiction':
            raise ValueError("Category must be 'Fiction' or 'Non-Fiction'")
        return cat
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
