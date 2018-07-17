
### 实名认证提交数据接口


#### request 请求

    put /user/auths/

#### params 参数

    id_name str 名字
    id_card int 身份证

#### response 响应

##### 响应1：

    {'code': 901, 'msg': '参数错误'}

##### 响应2：

    {'code': 900, 'msg': '数据库访问失败'}

##### 响应3：

    {'code': 1008, 'msg': '身份证已经被注册'}

##### 响应4：

    {'code': 200, 'msg': '请求成功'}