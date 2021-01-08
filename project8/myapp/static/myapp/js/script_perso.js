$(document).ready(function() {
        // Navigation color change 
        $(window).scroll(function() {
        var nav_img = $('#carotte');
        if ($(document).scrollTop() < 90) {
            nav_img.attr("src", "static/myapp/assets/img/carotte_blanc.png");
        } else {
            nav_img.attr("src","static/myapp/assets/img/carotte_noir.png");
        }
        });
    });
