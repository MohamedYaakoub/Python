function login() {
    const email = document.getElementById('LoginEmail').value;
    const password = document.getElementById('LoginPassword').value;
    eel.log_in(email, password);

}


eel.expose(login_rejected)
function login_rejected() {

    $('#alert-rejected-login').addClass("show")
    setTimeout(function () {
        $('#alert-rejected-login').removeClass("show");
    }, 4000);
}

function removeRejectAlert() {
    $('#alert-rejected-login').removeClass("show");
}

eel.expose(login_accepted);
function login_accepted() {
    window.location.replace('/hyreeDashboard.html');
}

eel.expose(register);
function register(){
    email = document.getElementById('RegisterEmail').value;
    password = document.getElementById('RegisterPassword').value;
    passwordRepeat = document.getElementById('RegisterPasswordRepeat').value;
    userType = document.querySelector('input[name="userType"]:checked').value;
    eel.register(email, password, passwordRepeat, userType);

}