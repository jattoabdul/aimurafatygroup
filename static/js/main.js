jQuery(document).ready(function($) {

    'use strict';

    // PRELOADER      
    $(window).load(function() {
        $('#preloader').fadeOut('slow', function() {
            $(this).remove();
        });
    });

    // Init Material scripts for buttons ripples, inputs animations etc, more info on the next link https://github.com/FezVrasta/bootstrap-material-design#materialjs
    $.material.init();

    /*WOW js*/
    new WOW().init();

    // Sticky Navigation
    $("#sticky-nav").sticky({ topSpacing: 0 });
    /*Blog*/

    $('.blog .owl-carousel').owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        nav: false,
        responsive: {
            0: {
                items: 1
            },
            300: {
                items: 1
            },
            600: {
                items: 2
            },
            900: {
                items: 3
            },
            1200: {
                items: 3
            }
        }
    });

    // Reveiws

    $("#clients .owl-carousel").owlCarousel({
        loop: true,
        items: 1,
        dots: true,
    });

    $(".clients-logo .slider").owlCarousel({
        nav: false,
        dots: false,
        autoplayTimeout: 2000,
        items: 4,
        loop: true,
        responsive: {
            0: {
                items: 2,
                nav: false
            },
            600: {
                items: 3,
                nav: false
            },
            1000: {
                items: 4,
                nav: false,
                loop: true
            }
        }

    });

    // FORM VALIDATION

    $(".subscribe-form input").jqBootstrapValidation({
        preventSubmit: true,
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            $.ajax({
                success: function() {
                    $('#subscribe-success').html("<div class='alert alert-success'>");
                    $('#subscribe-success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#subscribe-success > .alert-success')
                        .append("<strong>Your message has been sent. </strong>");
                    $('#subscribe-success > .alert-success')
                        .append('</div>');
                }
            })

        }
    });

    // //porfolio mix it up
    // $('.portfolio-four-col').mixItUp();
});