
### 个人信息上传头像接口


#### request请求

    post /user/profile/

##### params参数

    avatar file 头像

#### response响应

##### 响应1：

    {
    "code": 200,
    "url": "/static/upload/a7.jpg"
}

##### 响应2:

    {
    'code': 1006,
    'msg': '图片不符合标准'
    }

##### 响应3:

    {'code': 900, 'msg': '数据库访问失败'}

##### 响应4:

    {'code': 901, 'msg': '参数错误'}




