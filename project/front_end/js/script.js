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
