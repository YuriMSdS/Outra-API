import logging
import re

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

user = []

name = input("Informe seu nome: ")
informaçoes_validas = False

while not informaçoes_validas:
    if len(name) >= 3 and len(name) <= 100:
        informaçoes_validas = True
    else:
        print("As informações inseridas são inválidas. Por favor, insira novamente")
        name = input("Informe seu nome: ")


informaçoes_validas = False
while not informaçoes_validas:
    email = input("Informe seu email: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        informaçoes_validas = True
    else:
        print("Email inválido! Por favor, informe um email válido.")

informaçoes_validas = False
while not informaçoes_validas:
    try:
        age = int(input("Informe sua idade: "))
        if age > 14 and age < 99:
            informaçoes_validas = True
        else:
            print('Idade inválida! Por favor, informe uma idade válida.')
    except ValueError:
        print('Idade inválida! Por favor, informe uma idade válida.')

person = user(name, email, age)
print(person.name)
print(person.email)
print(person.age)

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
