function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function () {
        setTimeout(function () {
            $('.popup_con').fadeOut('fast', function () {
            });
        }, 1000)
    });
}


// $(document).ready(function () {
//
//     var id_name = $('#real-name').val();
//     var id_card = $('#id-card').val();
//     $("#form-auth").submit(function () {
//         $.ajax({
//             url: '/user/auth/',
//             type: 'POST',
//             data: {'id_name': id_name, 'id_card': id_card},
//             dataType: 'json',
//             success: function(msg){
//                 alert(22);
//                 if (msg.code.code == '200') {
//                     alert(11);
//                     $('#input1').parentNode.delete();
//                     $('#real-name').attr(value, msg.real_name);
//                     $('#id-card').attr(value, msg.user_id)
//                 }
//             },
//             error: function (data) {
//                 alert(data)
//             }
//         })
//     });
// }

// 判断是否有值，已经填写
$(document).ready(function () {
    $.get('/user/auths/',function(data){
        if(data.code == '200'){
            $('#real-name').val(data.id_name);
            $('#id-card').val(data.id_card);
            // 判断数据库里的值是否存在，以此来判断是否展示添加按钮
            if(data.id_card == '' | data.id_card == null){
                $('.btn-success').show();
            }else{
                $('.btn-success').hide()
            }
        }
    });
});


// 提交值
$('#form-auth').submit(function(){

    $.ajax({
        url: '/user/auths/',
        type: 'PUT',
        dataType: 'json',
        data: {
            id_name:$('#real-name').val(),
            id_card:$('#id-card').val()
        },
        success:function(data){
            if(data.code == '200'){
                $('.btn-success').hide();
                $('.error-msg').hide()
            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle">参数错误</i>');
                $('.error-msg').show()
            }
        },
        error:function(data){
            alert('请求失败！')
        }
    });
    return false;
});





