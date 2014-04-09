/* sticky anchors menu */
$(function () {
    var menu = $('.resume-menu');

    menu.find('a').on('click', function (e) {
        menu.find('a').removeClass('active');
        $(this).addClass('active');
    });

    if (!! menu.offset()) {
        var stickyTop = menu.offset().top;

        $(window).scroll(function () {
            var windowTop = $(window).scrollTop();

            if (stickyTop < windowTop) {
                menu.css({position: 'fixed', top: 0});
            } else {
                menu.css('position', 'static');
            }
        });
    }
});
