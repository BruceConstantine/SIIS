//theme controller
$(document).ready(function () {
    $("div>button").click(function () {
        var theme = $(this).parent('div').attr('class');
        var url1 = $("#img-url1").text();//default
        var url2 = $("#img-url2").text();//blue
        var url3 = $("#img-url3").text();//green

        if (theme == 'theme1') {
            // alert(url1);
            $("body").attr('background', url1);
            $("button").attr('class', 'button button button-3d button-action button-pill button-large');
        }
        else if (theme == 'theme2') {
            $("body").attr('background', url2);
            $("button").attr('class', 'button button-glow button-border button-rounded button-primary button-large');
        }
        else if (theme == 'theme3') {
            // alert(theme);
            $("body").attr('background', url3);
            $("button").attr('class', 'button button-primary button-rounded button-large');
        }
        else
            ;
    });
});