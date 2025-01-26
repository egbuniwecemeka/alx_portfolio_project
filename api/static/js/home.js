/* global $ */
$(document).ready(() => {
    $('.darkmode').click(function() {
        if ($('body').hasClass('dark')) {
            /* revert it back to normal mode */
            $('body').removeClass('dark');
            $('body').css('background-color', '#FFFFFF');
            $('h1, h2').css('color', '#FFFFFF');
            $('.darkmode').text('Dark Mode');
        } else {
            /* switch to dark mode */
            $('body').addClass('dark');
            $('body').css('background-color', '#000000');
            $('h1, h2, .question-text').css('color', '#FFFFFF');
            $('.darkmode').text('Light Mode');
        }
    });
});