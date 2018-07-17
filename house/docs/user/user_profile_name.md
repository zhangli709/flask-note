
### 个人信息上传名字接口


#### request请求

    post /user/profile/


##### params参数

    name str 名字


#### response响应

##### 响应1：

    {'code': 1007, 'msg': '用户已存在'}

##### 响应2：

    {'code': 200, 'msg': '请求成功'}

##### 响应3：

    {'code': 900, 'msg': '数据库访问失败'}

##### 响应4：

    {'code': 901, 'msg': '参数错误'}

