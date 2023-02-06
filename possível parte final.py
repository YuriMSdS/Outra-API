import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields, ValidationError
Session = sessionmaker()
session = Session

logging.basicConfig(filename='error.log', level=logging.ERROR)

class Database:
    def __init__(self, url):
        self.engine = create_engine(url)
        self.session_factory = sessionmaker(bind=self.engine)

    def create_session(self):
        return self.session_factory()

class user:
    def __init__(self, name, email,age):
        self.name = name
        self.email = email
        self.age = age

user = [];

<<<<<<< HEAD
print('Informe seu nome:')
name = input();

print('Informe seu email')
email = input();

print('informe sua idade:')
=======
print(‘Informe seu nome:‘)
name = input();

print(‘Informe seu email:‘)
email = input();

print(‘informe sua idade:‘)
>>>>>>> e75dfe1a33ca4aedae4297c376f055e22479d047
age = int(input());

person = user(name, email, age);
print(person.name);
print(person.email);
print(person.age);

class UserSchema(Schema):
    name = fields.Str(required=True, min=3)
    email = fields.Email(required=True)

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_data):
        errors = UserSchema().validate(user_data)
        if errors:
            return errors
        else:
            with self.db.create_session() as session:
                new_user = user(name=user_data['name'], email=user_data['email'])
                session.add(new_user)
                session.commit()
                return "Usuário criado com sucesso"

    def get_all_users(self):
        with self.db.create_session() as session:
            return session.query(user).all()

    def update_user(self, user_data):
        errors = UserSchema().validate(user_data)
        if errors:
            return errors
        else:
            with self.db.create_session() as session:
                user_to_update = session.query(user).filter(user.name==user_data['name']).first()
                if user_to_update:
                    user_to_update.email = user_data['email']
                    session.commit()
                    return "Usuário atualizado com sucesso"
                else:
                    return "Usuário não encontrado."

    def delete_user(self, user_data):
        with self.db.create_session() as session:
            user_to_delete = session.query(user).filter(user.name==user_data['name']).first()
            if user_to_delete:
                session.delete(user_to_delete)
                session.commit()
                return "Usuário deletado com sucesso"
            else:
                return "Usuário não encontrado."

if __name__ == "__main__":
    try:
        db = Database('postgresql://username:password@localhost:5432/database_name')
        user_repo = UserRepository(db)
    
    finally:
        session.close()
