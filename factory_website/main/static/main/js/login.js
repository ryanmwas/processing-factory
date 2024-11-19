const validCredentials = {
    username: 'user',
    password: 'password'
};

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === validCredentials.username && password === validCredentials.password) {
        window.location.href = 'index.html';
    } else {
        document.getElementById('error-message').innerText = 'Invalid credentials';
    }
}