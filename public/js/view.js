
const _form = $('#login-form');

_form.submit((e) => {
    e.preventDefault();
    var email = _form.find('input[name="email"]').val();
    var pwd = _form.find('input[name="pwd"]').val();
    console.log(email,pwd)
    model.login(email,pwd).then((user) => {
        console.log(user)
    })
})

