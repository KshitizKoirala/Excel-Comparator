$(document).ready(function () {
  var pathname = window.location.pathname;
  $('a[href="' + pathname + '"]').addClass("active");
});
