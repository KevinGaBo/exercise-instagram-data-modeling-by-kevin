import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    profile = relationship('Profile', back_populates = 'user', uselist=False)


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False, nullable=False)
    nick_name = Column(String(80), unique=False, nullable=False)
    posts = Column(String(80), unique=False, nullable=False)
    follows = Column(String(80), unique=False, nullable=False)
    followers = Column(String(80), unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='profile')
    history = relationship('History', back_populates='profile')
    post = relationship('Post', back_populates='profile')


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    history_photo = Column(String(120), unique=True, nullable=False)
    history_reel = Column(String(80), unique=False, nullable=False)
    history_link = Column(String(80), unique=False, nullable=False)
    history_tag = Column(String(80), unique=False, nullable=False)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    profile = relationship('Profile', back_populates='history')
    post = relationship('Post', back_populates='history')
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    photo = Column(String(120), unique=True, nullable=False)
    reel = Column(String(80), unique=False, nullable=False)
    likes = Column(String(80), unique=False, nullable=False)
    comments = Column(String(80), unique=False, nullable=False) 
    profile_id = Column(Integer, ForeignKey('profile.id'))
    profile = relationship('Profile', back_populates='post')
    history = relationship('History', back_populates='post')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
