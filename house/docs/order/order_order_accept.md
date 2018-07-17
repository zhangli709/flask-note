
### 接单的接口

#### request 请求

    patch /order/order/<int:id>/

#### params 参数

    order_id id 订单id

#### response 响应

##### 响应1：

    {'code': 200}

##### 响应2：

    {'code': 900, 'msg': '数据库访问失败'}