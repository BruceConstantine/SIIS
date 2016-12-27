/**
 * Created by lvhuiyang on 16-12-27.
 */
$(document).ready(function () {
    $('.form_area>form').submit(function () {
        var stu_number = $('#stu_number').val();
        var password1 = $('#password1').val();
        var password2 = $('#password2').val();
        if (stu_number == '') {
            alert("学号不能为空");
        }
        else {
            if (password1 == '' || password2 == '')
                alert("两次密码必须全部填写");
            else {
                var number_reg = /^\d{11}$/;
                if (number_reg.test(stu_number)) {
                    //number OK，判断密码
                    if (password1.length < 6)
                        alert("输入的密码小于6位");
                    else if (password1 == password2) {
                        alert("注册成功,即将跳转到首页");
                        window.location.href = "/";
                    }
                    else
                        alert("两次密码不一致");
                }
                else
                    alert("输入的学号不符合规范");
            }
        }
        // alert("123");
        return false;
    });
});