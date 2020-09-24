// Functions related to the jobs displayed in the home page

function tooltips() {
  $('[data-toggle="tooltip"]').tooltip()
}



// Functions for the hyrer create new job form
function nodates() {
  $date1 = $("#startdate");
  $date2 = $("#enddate");
  $cb = $("#nodate");
  $cb.on('change', function() {
    if ($cb.is(':checked')) {
      $date1.prop('disabled', true);
      $date2.prop('disabled', true);
    } else {
      $date1.prop('disabled', false);
      $date2.prop('disabled', false);
    }
  });
}



function otherjobtype() {

  $typeselect = $("#jobtype");
  $typeWrite = $("#otherTypeinput");
  $cb = $("#othertypeofjob");
  $cb.on('change', function() {
    if ($cb.is(':checked')) {
      $typeselect.hide();
      $typeselect.prop('disabled', true);
      $typeWrite.prop('disabled', false);
      $typeWrite.prop('required', true);
      $typeWrite.show()


    } else {
      $typeselect.show();
      $typeselect.prop('disabled', false);
      $typeWrite.hide()
      $typeWrite.prop('disabled', true);
      $typeWrite.prop('required', false);
    }
  });

}

if ($(window).width() > 100) {
  $(window).scroll(function(){
     if ($(this).scrollTop() > 40) {
        $('#navbar_top').addClass("fixed-top");
        // add padding top to show content behind navbar
        $('body').css('padding-top', $('.navbar').outerHeight() + 'px');
      }else{
        $('#navbar_top').removeClass("fixed-top");
         // remove padding top from body
        $('body').css('padding-top', '0');
      }
  });
}