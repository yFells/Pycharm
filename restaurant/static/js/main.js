$('head').append('<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,300" rel="stylesheet" type="text/css">');

$('input').focus(function(event) {
  $(this).closest('.float-label-field').addClass('float').addClass('focus');
})

$('input').blur(function() {
  $(this).closest('.float-label-field').removeClass('focus');
  if (!$(this).val()) {
    $(this).closest('.float-label-field').removeClass('float');
  }
});