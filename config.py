import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123$%^aSF#!__(&^^&*)'
    DATABASE =os.path.join(basedir, 'configurations.db')

