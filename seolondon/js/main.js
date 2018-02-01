$(document).ready(function ($) {

  $('.slider').unslider({
    animation: 'horizontal'
  });

  $('.ui.accordion')
    .accordion({
      selector: {
        trigger: '.title'
      }
    });

  $('.menu .item')
    .tab()
  ;

  $('.success.story.button').click(function() {
    var storyId = $(this).data('story');
    $('.success.story.modal.'+storyId).modal('show');
  });

  $('.apply-button').click(function() {
    $('.apply.modal').modal('show');
  });

  // open second modal on first modal buttons
  let $donateEl = $('.donate.modal');

if ($donateEl.length) {
    $donateEl.modal('attach events', '.donate-modal.button');
}

  // $('.ui.dropdown').dropdown();

/** Eligibility checker **/
  var eligibilityBackground = 0;
  var eligibilityArea = 0;
  var selectionBackground = 0;

  var eligibilityBools = [
    // Discipline | Investment Banking| Corporate Law | Consulting |Corp & Tech| Eng | Civil Service| City Solicitors Horizons
    [true, true, true, true, true, true, true], // Undergraduate (in any year of study) with min.
    [true, false, true, true, true, true, true], // Undergraduate (in any year of study) with min. 300 UCAS points
    [false, false, false, true, false, false, false], // Undergraduate (in any year of study) with min. 240 UCAS points
    [false, true, true, true, true, true, false], // Graduated with a 2:1 or higher and min. 320 UCAS points
    [false, false, true, true, true, true, false], // Graduated with a 2:1 or higher and min. 300 UCAS points
    [false, false, false, true, false, true, false] // Graduated with a 2:1 or higher and min. 240 UCAS points
  ];


  $('.ui.dropdown.eligibility.test').dropdown(
    {
      action: 'activate',
      onChange: function(value) {
        eligibilityBackground = value;
      }
    }
  );

  $('.ui.dropdown.eligibility.area').dropdown(
    {
      action: 'activate',
      onChange: function(value) {
        eligibilityArea = value;

          if (eligibilityBools[eligibilityBackground][eligibilityArea]) {

            $('.eligible--true').removeClass('hidden');
            $('.eligible--false').addClass('hidden');
          } else {
            $('.eligible--true').addClass('hidden');
            $('.eligible--false').removeClass('hidden');
          }
      }
    }
  );

  $('.ui.dropdown.selection.background').dropdown(
    {
      action: 'activate',
      onChange: function(value) {
        $('*[data-selection-process="'+selectionBackground+'"]').hide();
        selectionBackground = value;
        $('*[data-selection-process="'+selectionBackground+'"]').show();
      }
    }
  );

  $('#navigation-bar li li.child:contains("FAQ")').css("border-top", "3px solid #105f9b");

  $('#navigation-bar li a:contains("About Us")').parent().append(
    "<ul>" +
    "<li class='child'><a href='/about-us/#our-story'>Our Story</a></li>" +
    "<li class='child'><a href='/about-us/#today'>Today</a></li>" +
    "<li class='child'><a href='/about-us/#team'>Team</a></li>" +
    "<li class='child'><a href='/about-us/#board'>Board</a></li>" +
    "<li class='child'><a href='/about-us/#alumni-board'>Alumni Advisory Board</a></li>" +
    "<li class='child'><a href='/about-us/#join'>Join The Team</a></li>" +
    "<li class='child'><a href='/about-us/#contact'>Contact Us</a></li>" +
    "</ul>"
  );

  $("#scroll-to-top").click(function(e) {
    e.preventDefault();
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
  });

  $("#footer .dropdown.column .title").click(function(ev){
    ev.preventDefault();
    var $dropdownColumn = $(ev.target).parent('.dropdown.column');
    var $content = $(ev.target).next('.content');
    if ($dropdownColumn.hasClass('open')){
      $dropdownColumn.removeClass('open');
    }
    else if ($content.is(':hidden')){
      $dropdownColumn.addClass('open');
    }

  });

  $(window).scroll(function() {
    if ($(window).scrollTop() > 200)  {
      $("#scroll-to-top").addClass('visible');
    } else {
      $("#scroll-to-top").removeClass('visible');
    }
  });

  $(
    '.job-list__filter__select-input__label-container > input'
  ).on('change', function(){
    $('#job-list__filter__form').submit();
  });

  var elems = $('.job-list__filter__select-input__group');
  if (elems.length > 0) {
    var jobListFilterUpdateActiveStatus = function (mql){
      elems.each(function(idx, elem){
        var $elem = $(elem);
        var targets = $elem.find(
          '.job-list__filter__select-input__title,'+
          '.job-list__filter__select-input__content'
        );
        var selected = $elem.find('input[checked]:not([value=""])').length > 0;
        if (selected) {
          targets.addClass('active');
        }
        else if (mql.matches) {
          targets.addClass('active');
        }
        else {
          targets.removeClass('active');
        }
      })
    }
    var mediaQueryList = window.matchMedia("only screen and (min-width: 992px)");
    mediaQueryList.onchange = jobListFilterUpdateActiveStatus;
    jobListFilterUpdateActiveStatus(mediaQueryList);
  }

});



/**
 * JavaScript for the header and navigation
 * @class Header
 */
class Header {
  constructor(navbarId, headerId) {
    this.$navbar = $(navbarId);
    this.$header = $(headerId);
    this.$mobileToggle = this.$navbar.find('.mobile.toggle a');
    this.$mobileMenu = this.$navbar.children('.ui.mobile.container');
    this.$window = $(window);
    this.scrolling = false;
    this.lastScrollPosition = 9999999;
    this.menuLastToggled = new Date(0);

    this.bind();
    if (this.$window.scrollTop() >= 200) {
      this.$navbar.addClass('slide-down');
    }
  }

  /**
   * Bind the header to scroll and toggle events
   */
  bind() {
    //this.$window.scroll(this.scroll.bind(this));

    this.$window.resize(() => {
      if (this.$navbar.hasClass('mobile open') && this.$window.width() >= 768) {
        this.closeMobileMenu();
      }
    });

    this.$mobileToggle.click(this.toggleMobileMenu.bind(this));

    this.$mobileMenu.find('.menu-item-has-children').click((e) => {
      const $link = $(e.target).closest('.menu-item-has-children');
      const $menu = $link.children('ul');

      if (!$menu.hasClass('open')) {
        this.$mobileMenu.find('.menu-item-has-children ul').not($menu).slideUp(300).removeClass('open');
        $menu.slideDown(300).addClass('open');
        e.preventDefault();
      }
    });
  }
  /**
   * Show/hide the mobile menu
   */
  toggleMobileMenu() {
    const now = new Date();

    // debouncing
    if (now.getTime() - 700 < this.menuLastToggled.getTime()) {
      return false;
    } else {
      this.menuLastToggled = new Date();
    }

    // toggling
    if (this.$navbar.hasClass('mobile open')) {
      this.closeMobileMenu();
    } else {
      this.openMobileMenu();
    }
  }

  /**
   * Open the mobile menu and handle animations
   */
  openMobileMenu() {
    $('.mobile.slice').addClass('active');
    this.$navbar.addClass('mobile open');
    $('body').addClass('mobile open');

    setTimeout(() => {
      this.$navbar.find('.ui.mobile.container').fadeIn(350);
    }, 300);
  }

  /**
   * Close the mobile menu, handling animations
   */
  closeMobileMenu() {
    this.$mobileMenu.find('.menu-item-has-children ul').slideUp(300).removeClass('open');
    this.$navbar.find('.ui.mobile.container').fadeOut(300);
    $('body').removeClass('mobile open');

    setTimeout(() => {
      this.$navbar.removeClass('mobile open');
      $('.mobile.slice').removeClass('active');
    }, 300);
  }
}

$(document).ready(() => new Header('#navigation-bar', '#masthead'));
