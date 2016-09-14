$(document).ready(function ($) {

  $('.my-slider').unslider();

  $('.ui.accordion')
    .accordion({
      selector: {
        trigger: '.title'
      }
    })
  ;

  // open second modal on first modal buttons
  $('.success.story.modal')
    .modal('attach events', '.sucess.story.button')
  ;

  $('.ui.dropdown').dropdown();

});
