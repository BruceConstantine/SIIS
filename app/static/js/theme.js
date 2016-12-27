//theme controller
$(document).ready(function () {
    $("div>button").click(function () {
        var theme = $(this).parent('div').attr('class');
        var url1 = $("#img-url1").text();
        var url2 = $("#img-url2").text();
        var url3 = $("#img-url3").text();

        if (theme == 'theme1') {
            // alert(url1);
            document.getElementById("body").style.background = url1;
        }
        else if (theme == 'theme2') {
            alert(theme);
            $(document).css({'background': 'url("../img/blue_background.jpg") no-repeat;'});
        }
        else if (theme == 'theme3')
            $("body").css({'background': 'url("../img/green_background.jpg") no-repeat;'});
        else
            ;
    });
});