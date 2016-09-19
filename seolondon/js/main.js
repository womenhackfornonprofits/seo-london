$(document).ready(function ($) {
  $('.my-slider').unslider();

  $('.ui.accordion')
    .accordion({
      selector: {
        trigger: '.title'
      }
    });

  // open second modal on first modal buttons
  $('.success.story.modal')
    .modal('attach events', '.sucess.story.button');

  $('.ui.dropdown').dropdown();

  $('a[href*="#"]:not([href="#"])').click(function (e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');

      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top - 50
        }, 500);

        e.preventDefault();
      }
    }
  });
});
