
### 预定房屋页面信息提交接口

#### requset 请求

    post /order/

#### params 参数

    house_id int 房屋id
    start_time date 开始时间
    end_time date 结束时间

#### response 响应

##### 响应1：

    {'code': 200}

##### 响应2：

    {'code': 901, 'msg': '参数错误'}