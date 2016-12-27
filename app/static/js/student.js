/**
 * Created by lvhuiyang on 16-12-27.
 */
$(document).ready(function () {
    // alert('123');
    $("#submit").click(function () {
        var stu_number = $('#stu_number').val();
        if (stu_number == '' || stu_number.length != 11) {
            alert("请输入11位学号进行查询")
        }
        else {
            var url = '/student_info?student_number=' + stu_number;
            $.get(url, function (data) {
                var data_json = eval(data);
                // alert(data_json['name']);
                $('table#stu_info').find('td').eq(0).html(data_json['number']);
                $('table#stu_info').find('td').eq(1).html(data_json['name']);
                $('table#stu_info').find('td').eq(2).html(data_json['sex']);
                $('table#stu_info').find('td').eq(3).html(data_json['year']);
                $('table#stu_info').find('td').eq(4).html(data_json['marjor']);
                $('table#stu_info').find('td').eq(5).html(data_json['class']);
                $('table#stu_info').find('td').eq(6).html(data_json['level']);
                $('table#stu_info').find('td').eq(7).html(data_json['length_of_schooling']);
                $('#stu_info').css({'display': 'block'});
            });
        }
    });
});