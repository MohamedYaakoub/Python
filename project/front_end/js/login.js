function login() {
    const email = document.getElementById('LoginEmail').value;
    const password = document.getElementById('LoginPassword').value;
    eel.log_in(email, password);
}


function change_fields() {
    if (document.getElementById('createPersonal').checked) {
        document.getElementById('personalFields').style.display = 'block';
        document.getElementById('companyFields').style.display = 'none';
    } else {
        document.getElementById('personalFields').style.display = 'none';
        document.getElementById('companyFields').style.display = 'block';
    }
}

eel.expose(register_hyree)
function register_hyree() {
    firstName = document.getElementById('RegisterFirstName').value;
    lastName  = document.getElementById('RegisterLastName').value;
    email     = document.getElementById('RegisterEmail').value;
    password1 = document.getElementById('RegisterPassword1').value;
    password2 = document.getElementById('RegisterPassword2').value;
    eel.hyree_register(firstName, lastName, email, password1, password2);
}

eel.expose(hyreeRegisterAccepted)
function hyreeRegisterAccepted() {
    window.location.href = 'hyreeChoosePreferences.html';
}


eel.expose(hyreeRegisterRejected)
function hyreeRegisterRejected() {
    $('#alert-rejected-register').addClass("show")
    setTimeout(function () {
        $('#alert-rejected-register').removeClass("show");
    }, 4000);
}


eel.expose(register_hyrer)
function register_hyrer() {
    firstName = document.getElementById('HyrerFirstName').value;
    lastName  = document.getElementById('HyrerLastName').value;
    companyName = document.getElementById('HyrerCompanyName').value;
    email     = document.getElementById('HyrerEmail').value;
    password1 = document.getElementById('HyrerPassword1').value;
    password2 = document.getElementById('HyrerPassword2').value;
    if (document.getElementById('createPersonal').checked) {
        eel.hyrer_register([firstName, lastName], email, password1, password2);
    } else {
        eel.hyrer_register(companyName, email, password1, password2);
    }
}

eel.expose(hyrerRegisterAccepted)
function hyrerRegisterAccepted() {
    window.location.href = 'hyrerDashboard.html'
}

eel.expose(hyrerRegisterRejected)
function hyrerRegisterRejected() {
    $('#alert-rejected-register').addClass("show")
    setTimeout(function () {
        $('#alert-rejected-register').removeClass("show");
    }, 4000);
}


function tooltips() {
  $('[data-toggle="tooltip"]').tooltip()
}

function choose_preferences() {
    let preferences = [];
    if (document.getElementById('defaultCheck1').checked) {
        preferences.push(document.getElementById('defaultCheck1').value);
    }
    if (document.getElementById('defaultCheck2').checked) {
        preferences.push(document.getElementById('defaultCheck2').value);
    }
    if (document.getElementById('defaultCheck3').checked) {
        preferences.push(document.getElementById('defaultCheck3').value);
    }
    if (document.getElementById('defaultCheck4').checked) {
        preferences.push(document.getElementById('defaultCheck4').value);
    }
    eel.choose_preferences(preferences);
}

eel.expose(preferences_accepted)
function preferences_accepted() {
    window.location.href = 'hyreeLocation.html';
}

eel.expose(preferences_rejected)
function preferences_rejected() {
    $('#alert-rejected-preferences').addClass("show")
    setTimeout(function () {
        $('#alert-rejected-preferences').removeClass("show");
    }, 4000);
}

function get_location() {
    x = document.getElementById('test');
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser...";
    }
}

eel.expose(location_accepted)
function location_accepted() {
    window.location.href = 'hyreeDashboard.html';
}

eel.expose(location_rejected)
function location_rejected() {
    $('#alert-rejected-location').addClass("show")
    setTimeout(function () {
        $('#alert-rejected-location').removeClass("show");
    }, 4000);
}

function showPosition(position) {
    eel.save_position(position.coords.longitude, position.coords.latitude);
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



function hyrerRegister(){
    location.href = 'register.html'+'?saved_item_id='+'hyrer';
}

//
function checkIfHyrer(){
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('saved_item_id') === 'hyrer'){
        document.getElementById("hyrertab").click();
    } else{
        document.getElementById("defaultOpen").click();
    }

}