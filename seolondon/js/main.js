$(document).ready(function ($) {

  $('.my-slider').unslider();

  $('.ui.accordion')
    .accordion({
      selector: {
        trigger: '.title'
      }
    })
  ;

});
