//$(document).ready(function() {
//    alert('Hello, world!');
//});

$(document).ready(function() {

    $('#about-btn').click(function() {
        alert('Your clicked the button using JQuery !!!!');
        msgStr = $('#msg').html();
        msgStr = msgStr + ' ooo, fancy!';
        $('#msg').html(msgStr);
    })

    $('p').hover(
        function() {
            $(this).css('color', 'red');
        },
        function() {
            $(this).css('color', 'black');
        }
    );


})


