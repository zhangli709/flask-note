
### 登录接口

#### request请求
    post /user/login/

##### params参数

    mobile str 电话号码
    password str 密码

#### response响应

##### 响应1：
    {
    "code": 901,
    "msg": "参数错误"
}

##### 响应2：
    {
    "code": 1001,
    "msg": "注册信息手机号不符合规则"
}

##### 响应3：
{
    "code": 1004,
    "msg": "用户不存在"
}

##### 响应4：
    {
    "code": 1005,
    "msg": "用户密码错误"
}

##### 响应5：
    {
    "code": 200,
    "msg": "请求成功"
}
