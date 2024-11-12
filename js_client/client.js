const loginForm = document.getElementById('loginform');
const baseEndpoint = "http://localhost:8000/api";


if (loginForm){
    loginForm.addEventListener('submit', handleLogin);
}

function handleLogin(event){
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;

    let loginFormData = new FormData(loginForm);
    
    let loginObjectData = Object.fromEntries(loginFormData)
    
    let bodyJasonData = JSON.stringify(loginObjectData)
    
    // console.log(loginObjectData);
    // console.log(bodyJasonData);
    const options = {
        method : 'POST',
        headers : {
            "Content-Type": "application/json"
        },
        body : bodyJasonData
    }
    fetch(loginEndpoint, options)
    .then(response => {
        console.log(response);
        return response.json();
    })
    .then(x => {
        console.log(x);
    })
    .catch(err => {
        console.log('error', err);
    })
}