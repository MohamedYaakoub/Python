eel.expose(post_job);

function post_job(company, title, description, id) {
    let para = document.createElement("P");                 // Create a <p> element
    para.innerHTML = "<div class=\"card\" id=\"idn" + id + "\" style=\"width: 100%;\">\n" +
        "  <div class=\"card-body\">\n" +
        "    <h5 class=\"card-title\">" + company + "</h5>\n" +
        "    <h6 class=\"card-subtitle mb-2 text-muted\">" + title + "</h6>\n" +
        "    <p class=\"card-text\">" + description + "</p>\n" +
        "    <a href=\"#\" onclick=\"acceptJob(" + id + ")\" class=\"card-link\">Accept</a>\n" +
        "    <a href=\"#\" onclick=\"rejectJobCheck(" + id + ",'" + title + "','" + company + "')\" class=\"card-link\">Reject</a>\n" +
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


function login() {
    const email = document.getElementById('LoginEmail').value;
    const password = document.getElementById('LoginPassword').value;
    eel.log_in(email, password);

}

eel.expose(login_accepted);
function login_accepted() {
    window.location.replace('/main.html');
}
