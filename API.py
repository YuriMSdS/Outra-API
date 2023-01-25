from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Para criar a conexão com o banco de dados
engine = create_engine('postgresql://username:password@localhost:5432/database_name')
Session = sessionmaker(bind=engine)
session = Session()

#Adicionar um novo registro para a label
new_user = 'User'(name='Pedro Programas',email='pedrinho@email.com')
session.add(new_user)
session.commit()

#Para listar os registros da label
users = session.query("User").all()
for user in users:
    print(user.name, user.email)

#Para atualizar um registro
user_to_update = session.query('User').filter(User.name=='pedro').first()
user_to_update.email='pedroprog@email.com'
session.commit()

#Para deletar um registro
user_to_delete = session.query('User').filter(User.name=='pedro').first()
session.delete('user_to_delete')
session.commit()


#Para fechar a conexão
session.close