'use strict';

$(document).ready(function () {
    $('table').on('click', '.day', function (event) {
        let target = event.target;
        $.ajax( {
            url: "/temperature/" + target.innerText + "/",

            success: function (data) {
                $('.abc').html(data.result);
                console.log('success');
            }
        })
        event.preventDefault();
    });

    $('.search').on('click', function (event) {
        let target = document.getElementById('nameFind');
        $.ajax( {
            url: "/search/" + target.value + "/",

            success: function (data) {
                $('table').html(data.result);
            }
        })
        event.preventDefault();
    })
})