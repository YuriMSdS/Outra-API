const Sequelize= require('sequelize')

// Criar uma conexão com o banco de dados
const sequelize = new Sequelize('database_name', 'username', 'password', {
    host: 'localhost',
    dialect: 'postgres',
  });

// Define o modelo do usuário
const User = sequelize.define('user', {
  name: {
    type: Sequelize.STRING,
  },
  email: {
    type: Sequelize.STRING,
  },
});

// Sincronizar o modelo com a tabela do banco de dados
User.sync().then(() => {
    // Adicionar um registro a uma tabela
    User.create({
      name: 'John Doe',
      email: 'johndoe@example.com',
    }).then(() => {
      // Recuperar todos os registros de uma tabela
      User.findAll().then((users) => {
        users.forEach((user) => {
          console.log(user.name, user.email);
        });
      });
      // Atualizar um registro
      User.update({ email: 'johndoe2@example.com' }, {
        where: { name: 'John Doe' },
      });
      // Deletar um registro
      User.destroy({
        where: { name: 'John Doe' },
      });
    });
  });