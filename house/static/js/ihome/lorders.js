//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);
    $(".order-accept").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-accept").attr("order-id", orderId);
    });
    $(".order-reject").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-reject").attr("order-id", orderId);
    });


    // 填充信息
    $.get('/order/fd/', function(data){
        if(data.code=='200'){

            // 渲染页面
            var lorders_html = template('lorders_list', {orders: data.olist});
            $('.orders-list').html(lorders_html);
            // 给按钮绑定属性
            $('.order-accept').click(function(){
                var order_id = $(this).parents('li').attr('order-id');
                $('.modal-accept').attr('order-id', order_id)
            });
            // 给按钮绑定属性
            $('.order-reject').click(function(){
                var order_id = $(this).parents('li').attr('order-id');
                $('.modal-reject').attr('order-id', order_id)
            });
            // 绑定方法
            $('.modal-accept').click(function(){
                var order_id = $(this).attr('order-id');
                $.ajax({
                    url: '/order/order/'+ order_id+ '/',
                    type: 'PATCH',
                    data: {status:'WAIT_PAYMENT'},
                    dataType: 'json',
                    success: function(data){
                        if(data.code='200'){
                            $('.order-operate-'+order_id).hide();
                            $('#accept-modal').modal('hide');
                            $('#order_id_'+ order_id).html('待支付');
                        }
                    },
                    error: function(data){
                        alert('修改订单状态失败')
                    }
                })
            });
            // 绑定方法
            $('.modal-reject').click(function(){
                var order_id = $(this).attr('order-id');
                var comment = $('#reject-reason').val();
                $.ajax({
                    url: '/order/order/'+ order_id+ '/',
                    type: 'PATCH',
                    data: {status:'REJECTED',comment:comment},
                    dataType: 'json',
                    success: function(data){
                        if(data.code='200'){
                            $('.order-operate-'+order_id).hide();
                            // modal 点击显示，再点击隐藏
                            $('#reject-modal').modal('hide');
                            $('#order_id_'+ order_id).html('已拒单');

                            //
                            // $("body").attr('class','');
                            // $('#accept-modal').attr('class', 'modal fade');
                            // $('.modal-backdrop').hide();
                        }
                    },
                    error: function(data){
                        alert('修改订单状态失败')
                    }
                })
            });
        }
    });
});