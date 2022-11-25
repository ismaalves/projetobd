import os

SECRET_KEY = 'teste'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql+psycopg2',
        usuario = 'qivwowphbqoskt',
        senha = 'f3a71db6832d18c702e3a8ffc7982beec2f2494c28fc178c965c683b2c15e1c0',
        servidor = 'ec2-18-209-78-11.compute-1.amazonaws.com',
        database = 'db2t6gb1jdbstc'
    )