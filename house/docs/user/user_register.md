
### 注册接口

#### request请求
    post /user/regist/

##### params参数

    mobile str 电话号码
    password str 密码
    password2 str 确认密码

#### response响应

##### 响应1：
    {
    "code": 1000,
    "msg": "注册信息参数错误"
}

##### 响应2：
    {
    "code": 1002,
    "msg": "手机号码已经被注册"
}

##### 响应3：
    {
    "code": 1003,
    "msg": "两次密码不一致"
}

##### 响应4：
    {
    "code": 200,
    "msg": "请求成功"
}