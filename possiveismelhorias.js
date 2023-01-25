//para tratar erros
User.create({
    name: 'John Doe',
    email: 'johndoe@example.com',
  }).then(() => {
    // Recuperar todos os registros de uma tabela
    User.findAll().then((users) => {
      users.forEach((user) => {
        console.log(user.name, user.email);
      });
    }).catch(err => console.log(err))
    // Atualizar um registro
    User.update({ email: 'johndoe2@example.com' }, {
      where: { name: 'John Doe' },
    }).catch(err => console.log(err))
    // Deletar um registro
    User.destroy({
      where: { name: 'John Doe' },
    }).catch(err => console.log(err))
  }).catch(err => console.log(err))



  //para validação de dados
  const { check, validationResult } = require('express-validator');

app.post('/users', [
  check('name').isLength({ min: 3 }),
  check('email').isEmail()
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() });
  }
  User.create({
    name: req.body.name,
    email: req.body.email,
  }).then(() => res.status(201).json({ message: 'User created' }))
    .catch(err => res.status(500).json({ errors: err }));
});



//abstração de códigos
const createUser = (user) => {
    return User.create(user)
  }
  const getUsers = () => {
    return User.findAll()
  }
  const updateUser = (email, name) => {
    return User.update({ email }, {
      where: { name }
    })
  }
  const deleteUser = (name) => {
    return User.destroy({
      where: { name }
    })
  }

  

  sequelize.transaction(t => {
    return User.create({
      name: 'John Doe',
      email: 'johndoe@example.com',
    }, {transaction: t}).then(() => {
      return User.findAll({transaction: t});
    }).then(users => {
      return User.update({ email: 'johndoe2@example.com' }, {
        where: { name: 'John Doe' },
      }, {transaction: t});
    }).then(() => {
      return User.destroy({
        where: { name: 'John Doe' },
      }, {transaction: t});
    });
})
