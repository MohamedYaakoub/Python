function login() {
    const email = document.getElementById('LoginEmail').value;
    const password = document.getElementById('LoginPassword').value;
    eel.log_in(email, password);

}

eel.expose(register_hyree)
function register_hyree() {
    console.log("BOOP")
    firstName = document.getElementById('RegisterFirstName').value;
    lastName  = document.getElementById('RegisterLastName').value;
    email     = document.getElementById('RegisterEmail').value;
    password1 = document.getElementById('RegisterPassword1').value;
    password2 = document.getElementById('RegisterPassword2').value;
    eel.hyree_register(firstName, lastName, email, password1, password2);
}

eel.expose(hyreeRegisterAccepted)
function hyreeRegisterAccepted() {
    window.location.href = 'hyreeChoosePreferences.html'
}


eel.expose(hyreeRegisterRejected)
function hyreeRegisterRejected() {
    $('#alert-rejected-register').addClass("show")
    setTimeout(function () {
        $('#alert-rejected-register').removeClass("show");
    }, 4000);
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

function openTab(evt, tabName) {
    console.log(tabName);
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
    evt.currentTarget.className += " active";
}

