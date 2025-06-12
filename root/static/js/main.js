/* main.js — объединённый и оптимизированный */

'use strict';

(function($) {

  // Простая debounce-обёртка
  function debounce(fn, ms) {
    let timer;
    return function(...args) {
      clearTimeout(timer);
      timer = setTimeout(() => fn.apply(this, args), ms);
    };
  }

  $(window).on('load', function() {
    /*------------------
        Preloader
    --------------------*/
    $(".loader").fadeOut();
    $("#preloder").delay(200).fadeOut("slow");

    /*------------------
        Background Set
    --------------------*/
    $(".set-bg").each(function() {
      const bg = $(this).data("setbg");
      if (bg) $(this).css("background-image", `url(${bg})`);
    });

    /*------------------
        MixItUp Filter
    --------------------*/
    const container = document.querySelector(".filter__gallery");
    if (container && typeof mixitup !== "undefined") {
      console.log("MixItUp INIT, total items:", container.querySelectorAll(".mix").length);

      // Инициализация миксера
      const mixer = mixitup(container, {
        selectors: { target: ".mix" },
        animation: {
          duration: 300,
          queue: true,
          queueLimit: 50   // вместительная очередь
        },
        callbacks: {
          onMixStart(state) {
            console.log("onMixStart — filter:", state.activeFilter.selector);
          },
          onMixEnd(state) {
            console.log("onMixEnd — visible:", state.totalShow);
          }
        }
      });

      // Debounce-обработчик кликов
      const handleFilter = debounce(function(filterValue) {
        mixer.filter(filterValue);
      }, 200);

      $(".filter__controls li").on("click", function(e) {
        e.preventDefault();
        $(".filter__controls li").removeClass("active");
        $(this).addClass("active");
        const f = $(this).data("filter");
        console.log("Requested filter:", f);
        handleFilter(f);
      });
    } else {
      console.warn("MixItUp not initialized");
    }

    /*------------------
        Search model
    --------------------*/
    $(".search-switch").on("click", () => $(".search-model").fadeIn(400));
    $(".search-close-switch").on("click", () => {
      $(".search-model").fadeOut(400, () => $("#search-input").val(""));
    });

    /*------------------
        Navigation
    --------------------*/
    $(".mobile-menu").slicknav({
      prependTo: "#mobile-menu-wrap",
      allowParentLinks: true
    });

    /*------------------
        Hero Slider
    --------------------*/
    $(".hero__slider").owlCarousel({
      loop: true, margin:0, items:1, dots:true, nav:true,
      navText:["<span class='arrow_carrot-left'></span>","<span class='arrow_carrot-right'></span>"],
      animateOut:"fadeOut", animateIn:"fadeIn", smartSpeed:1200,
      autoHeight:false, autoplay:true, mouseDrag:false
    });

    /*------------------
        Video Player
    --------------------*/
    new Plyr("#player", {
      controls:["play-large","play","progress","current-time","mute","captions","settings","fullscreen"],
      seekTime:25
    });

    /*------------------
        Niceselect
    --------------------*/
    $("select").niceSelect();

    /*------------------
        Scroll To Top
    --------------------*/
    $("#scrollToTopButton").click(() => {
      $("html,body").animate({ scrollTop:0 },"slow");
      return false;
    });

    /*------------------
        Highlight Active Menu Item
    --------------------*/
    const path = window.location.pathname;
    $(".header__menu a").each(function() {
      if ($(this).attr("href") === path) $(this).closest("li").addClass("active");
    });
  });

})(jQuery);
