// init create Account
const createAccount = document.querySelector('#create-account');
// Hide Create account
createAccount.style.display = 'none';
// init login account
const loginAccount = document.querySelector('#login');

const createAccountLink = document.querySelector('#create-AccountLink');
// handling when user clicks create account
createAccountLink.addEventListener('click', hideLoginShowCreateAccount);

// init login link
const loginLink = document.querySelector('#login-Link');
// handling when user clicks Login
loginLink.addEventListener('click', hideCreateAccountShowLogin);

function hideLoginShowCreateAccount(e) {
  e.preventDefault;
  loginAccount.style.display = 'none';
  createAccount.style.display = 'block';
}

function hideCreateAccountShowLogin(e) {
  e.preventDefault;
  createAccount.style.display = 'none';
  loginAccount.style.display = 'block';
}
