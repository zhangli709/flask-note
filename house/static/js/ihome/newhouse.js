function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// 将该区域通过ajax动态的渲染出来。
$(document).ready(function(){
    $.get('/house/area_facility/', function(data){
        var area_list_html = '';
        for(var i=0; i<data.area_list.length; i++){
            var area_html = '<option value="' + data.area_list[i].id + '">'+data.area_list[i].name+'</option>';
            area_list_html += area_html
        }
        $('#area-id').html(area_list_html);


        var facility_html_list = '';
        for(var i=0; i<data.facility_list.length; i++){
            var facility_html = '<li><div class="checkbox"><label>';
            facility_html += '<input type="checkbox" name="facility" value="'  + data.facility_list[i].id +'">' + data.facility_list[i].name;
            facility_html += '</label></div></li>';
            facility_html_list += facility_html
        }
        $('.house-facility-list').html(facility_html_list)
    });
});


// 5-23 新知识，参数的传输，多参数传输
$('#form-house-info').submit(function () {
    // alert($(this).serialize());
    $.post('/house/newhouse/', $(this).serialize(), function (data) {
        if(data.code=='200'){
            $('#form-house-info').hide();
            $('#form-house-image').show();
            $('#house-id').val(data.house_id);
        }
    });
    return false;
});


$('#form-house-image').submit(function () {
    $(this).ajaxSubmit({
        url: '/house/images/',
        type: 'post',
        dataType: 'json',
        success:function (data) {
            if(data.code=='200'){
                $('.house-image-cons').append('<img src="' + data.image_url + '">')
            }
        },
        error:function () {
            alert('上传房屋图片失败')
        }
    });
    return false;
});