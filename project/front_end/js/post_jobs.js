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

eel.expose(post_active_job)
function post_active_job(company, title, description, id) {
    $('#alert-changed-profile').removeClass("show");
    let para = document.createElement("P");                 // Create a <p> element
    para.innerHTML = "<div class=\"card color3\" id=\"idn" + id + "\" style=\"width: 100%;\">\n" +
        "  <div class=\"card-body\">\n" +
        "    <h5 class=\"card-title\"  >" + company + "</h5>\n" +
        "    <h6 class=\"card-subtitle mb-2 \" >" + title + "</h6>\n" +
        "    <p class=\"card-text\">" + description + "</p>\n" +
        "    <button type=\"button\" onclick=\"cancelJobCheck(" + id + ",'" + title + "','" + company + "')\" class=\"btn btn-outline-light\">Cancel</button>" +
        "  </div>\n" +
        "</div>";                // Insert text
    document.getElementById("JobsOffer").appendChild(para);
}

eel.expose(post_accepted_job)
function post_accepted_job(company, title, description, id) {
    $('#alert-changed-profile').removeClass("show");
    let para = document.createElement("P");                 // Create a <p> element
    para.innerHTML = "<div class=\"card color3\" id=\"idn" + id + "\" style=\"width: 100%;\">\n" +
        "  <div class=\"card-body\">\n" +
        "    <h5 class=\"card-title\"  >" + company + "</h5>\n" +
        "    <h6 class=\"card-subtitle mb-2 \" >" + title + "</h6>\n" +
        "    <p class=\"card-text\">" + description + "</p>\n" +
        "    <button type=\"button\" onclick=\"rejectJobCheck(" + id + ",'" + title + "','" + company + "')\" class=\"btn btn-warning\">Contact Hyree</button>" +
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

function cancelJobCheck(id, title, company) {
    $('#ModalRejectJobTitle').text('Cancel ' + title + ' job')
    $('#ModalRejectJobBody').html('Are you sure you want to cancel the <b>' + title + '</b> job request?')
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

eel.expose(postNewJob)
function postNewJob(){
    const job_type = $("#jobtype").val()
    const job_other_type = $("#otherTypeinput").val()
    const job_description = $("#description").val()
    const job_offer = $("#offer").val()
    const start_date = $("#startdate").val()
    const end_date = $("#enddate").val()

    eel.get_new_job_data(job_type, job_other_type, job_description, job_offer, start_date, end_date);
}

function job_successfully_created(){
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('new_job') === 'True'){
        $('.alert').show();
        setTimeout(function () {
        $('.alert').hide();
    }, 4000);

    }

}