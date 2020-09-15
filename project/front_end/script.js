// Functions related to the jobs displayed in the home page

eel.expose(post_job)
function post_job(company, title, description, id) {
    $('#alert-changed-profile').removeClass("show");
    let para = document.createElement("P");                 // Create a <p> element
    para.innerHTML = "<div class=\"card color3\" id=\"idn" + id + "\" style=\"width: 100%;\">\n" +
        "  <div class=\"card-body\">\n" +
        "    <h5 class=\"card-title\"  >" + company + "</h5>\n" +
        "    <h6 class=\"card-subtitle mb-2 \" >" + title + "</h6>\n" +
        "    <p class=\"card-text\">" + description + "</p>\n" +
        "    <button type=\"button\" onclick=\"acceptJob(" + id + ")\" class=\"btn btn-warning\">Accept</button>" +
        "    <button type=\"button\" onclick=\"rejectJobCheck(" + id + ",'" + title + "','" + company + "')\" class=\"btn btn-outline-light\">Reject</button>" +
        "  </div>\n" +
        "</div>";                // Insert text
    document.getElementById("JobsOffer").appendChild(para);
}


eel.expose(post_old_jobs)
function post_old_jobs(company, title, description, id) {
    $('#alert-changed-profile').removeClass("show");
    let para = document.createElement("P");                 // Create a <p> element
    para.innerHTML = "<div class=\"card color3\" id=\"idn" + id + "\" style=\"width: 100%;\">\n" +
        "  <div class=\"card-body\">\n" +
        "    <h5 class=\"card-title\"  >" + company + "</h5>\n" +
        "    <h6 class=\"card-subtitle mb-2 \" >" + title + "</h6>\n" +
        "    <p class=\"card-text\">" + description + "</p>\n" +
        "  </div>\n" +
        "</div>";                // Insert text
    document.getElementById("JobsOffer").appendChild(para);
}

function acceptJob(id) {
    const divid = "idn" + id;
    document.getElementById(divid).style.display = "none";

}

function rejectJobCheck(id, title, company) {
    $('#ModalRejectJobTitle').text('Reject offer by ' + company)
    $('#ModalRejectJobBody').html('Are you sure you want to reject the <b>' + title + '</b> job at <b>' + company + '</b> ?')
    $('#ModalRejectJob').modal('show')
    $("#modalConfirmRejectbtn").attr("onclick", "rejectJob(" + id + ")");

}

function rejectJob(id) {
    const divid = "idn" + id;
    $('#ModalRejectJob').modal('hide')
    document.getElementById(divid).style.display = "none";

}

eel.expose(printNoJobs)
function printNoJobs() {
    var x = document.getElementById("no-jobs-yet");
    x.style.display = "block"
}


// Login related functions

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


function changeProfile() {
    const email = document.getElementById('UserEmail').value;
    const password = document.getElementById('UserPassword').value;
    const location = document.getElementById('UserLocation').value;
    //eel.change_profile(email, password, location);
    $('#alert-changed-profile').addClass("show")
    setTimeout(function () {
        $('#alert-changed-profile').removeClass("show");
    }, 4000);
}


