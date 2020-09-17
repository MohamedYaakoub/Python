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

eel.expose(accept_hyree);
function accept_hyree() {
    window.location.replace('/hyreeDashboard.html');
}

eel.expose(accept_hyrer);
function accept_hyrer() {
    window.location.replace('/hyrerDashboard.html');
}

eel.expose(register);
function register(){
    email = document.getElementById('RegisterEmail').value;
    password = document.getElementById('RegisterPassword').value;
    passwordRepeat = document.getElementById('RegisterPasswordRepeat').value;
    userType = document.querySelector('input[name="userType"]:checked').value;
    eel.register(email, password, passwordRepeat, userType);

}

function openTab(evt, tabName) {
    console.log(evt)
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("registerTabContent");
    for (i=0; i<tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i=0; i<tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += "active";
}