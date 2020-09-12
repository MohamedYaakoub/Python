eel.expose(post_job);
function post_job(company,title,description,id) {
    var para = document.createElement("P");                 // Create a <p> element
    para.innerHTML = "<div class=\"card\" id=\"idn"+id+"\" style=\"width: 100%;\">\n" +
        "  <div class=\"card-body\">\n" +
        "    <h5 class=\"card-title\">" + company + "</h5>\n" +
        "    <h6 class=\"card-subtitle mb-2 text-muted\">"+title+ "</h6>\n" +
        "    <p class=\"card-text\">"+description+"</p>\n" +
        "    <a href=\"#\" onclick=\"acceptJob("+id+")\"class=\"card-link\">Accept</a>\n" +
        "    <a href=\"#\" class=\"card-link\">Reject</a>\n" +
        "  </div>\n" +
        "</div>";                // Insert text
    document.getElementById("JobsOffer").appendChild(para);
}


function acceptJob(id) {
    var divid = "idn"+ id;
    document.getElementById(divid).style.display="none";

}

function login() {
    var email = document.getElementById('LoginEmail').value;
    var password = document.getElementById('LoginPassword').value;
    eel.log_in(email,password);

}

eel.expose(login_accepted);
function login_accepted(){
    // alert("Hi");
    window.location.replace('/main.html');
}
