eel.expose(writeUserInformation)
function writeUserInformation(email, password, location) {
    document.getElementById('UserEmail').removeAttribute('readonly');
    document.getElementById('UserPassword').removeAttribute('readonly');
    document.getElementById('UserLocation').removeAttribute('readonly');
    document.getElementById('UserEmail').value = email;
    document.getElementById('UserPassword').value = password;
    document.getElementById('UserLocation').value = location;
    $('#alert-profile-multi').removeClass("show");
}

eel.expose(updateUserInformation)
function updateUserInformation() {
    new_email = document.getElementById('UserEmail').value;
    new_password = document.getElementById('UserPassword').value;
    new_location = document.getElementById('UserLocation').value;
    eel.update_user_information(new_email, new_password, new_location);
}

eel.expose(updateAccepted)
function updateAccepted() {
    document.getElementById('profile-alert-text').innerHTML = "<strong>Success!</strong> Your changes were saved.";
    $('#alert-profile-multi').addClass("show");
    setTimeout(function () {
        $('#alert-profile-multi').removeClass("show");
    }, 4000);
}

eel.expose(updateRejected)
function updateRejected() {
    document.getElementById('profile-alert-text').innerHTML = "<strong>Oops!</strong> Your changes were not saved.";
    $('#alert-profile-multi').addClass("show");
    setTimeout(function () {
        $('#alert-profile-multi').removeClass("show");
    }, 4000);
}