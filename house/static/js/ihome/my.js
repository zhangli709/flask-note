function logout() {
    $.get('/user/logout/', function(data){
        if (data.code=='200') {
            location.href = "/user/login/";
        }
    })
}

// 修改页面中的信息，将页面的名字，电话，头像显示出来
$(document).ready(function(){
    $.get('/user/user/', function(data){
        if(data.code == '200'){
            $('#user-mobile').html(data.user.phone);
            $('#user-name').html(data.user.name);
            $('#user-avatar').attr('src', data.user.avatar)
        }
    })
})