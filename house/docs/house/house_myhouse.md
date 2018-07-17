
### 我的房源接口


#### request 请求
    get /house/auth_myhouse

#### response 响应

##### 响应1：
    {
      "code": 200,
      "hlist_list":{
          "address": "\u9732\u5929",
          "area": "\u9526\u6c5f\u533a",
          "create_time": "2018-05-24 19:00:52",
          "id": 3,
          "image": "/static/upload/b1.jpg",
          "order_count": 0,
          "price": 100,
          "room": 1,
          "title": "\u8349\u623f"
          }
    }

##### 响应2：

    {'code': 2000, 'msg': '用户没有实名认证'}
