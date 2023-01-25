from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields
          
# Criar uma conexão com o banco de dados
engine = create_engine('postgresql://username:password@localhost:5432/database_name')
Session = sessionmaker(bind=engine)
session = Session()

class UserSchema(Schema):
    name = fields.Str(required=True, min=3)
    email = fields.Email(required=True)

user_schema = UserSchema()

def create_user(user_data):
    errors = user_schema.validate(user_data)
    if errors:
        return errors
    else:
        new_user = User(name=user_data['name'], email=user_data['email'])
        session.add(new_user)
        session.commit()
        return "Usuário criado com sucesso"

def get_all_users():
    return session.query(User).all()

def update_user(user_data):
    user_to_update = session.query(User).filter(User.name==user_data['name']).first()
    user_to_update.email = user_data['email']
    session.commit()
    return "Usuário atualizado com sucesso"

def delete_user(user_data):
    user_to_delete = session.query(User).filter(User.name==user_data['name']).first()
    session.delete(user_to_delete)
    session.commit()
    return "Usuário deletado com sucesso"

try:
    # Adicionar um registro a uma tabela
    user_data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
    print(create_user(user_data))

    # Listar todos os registros de uma tabela
    users = get_all_users()
    for user in users:
        print(user.name, user.email)

    # Atualizar um registro
    user_data = {'name': 'John Doe', 'email': 'johndoe2@example.com'}
    print(update_user(user_data))

    # Deletar um registro
    user_data = {'name': 'John Doe'}
    print(delete_user(user_data))

except Exception as e:
    print(e)

finally:
    # Fechar a conexão
    session.close()
