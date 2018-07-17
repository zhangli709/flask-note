function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


// 上传图片
$("#form-avatar").submit(function () {
    $(this).ajaxSubmit({
        url: '/user/profile/',
        type: 'PUT',
        data:{},
        dataType: 'json',
        success: function (data) {
            if (data.code == '200') {
                $('#user-avatar').attr('src', data.url)
                alert('头像上传成功！')
            }
        },
        error: function (data) {
            alert('上传头像失败')
        }
    });
    return false;
});



// 修改名字
$("#form-name").submit(function () {
    $('.error-msg').hide();
    var name = $("#user-name").val();
    $.ajax({
        url: '/user/profile/',
        type: 'PUT',
        data: {
            'name': name
        },
        dataType: 'json',
        success: function (data) {
            if (data.code == '200') {
                alert('用户名修改成功！')
            }else {
                $('.error-msg').html('<i class="fa fa-exclamation-circle">用户名已存在</i>');
                $('.error-msg').show();
            }

        },
        error: function (data) {
            alert(data)
        }
    });
    return false;
});




