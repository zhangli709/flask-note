
### 预定房屋页面信息获取接口

#### request 请求

    get /house/detail/<int:id>/

#### params 参数

    id int 房屋id

#### response 响应

    {
  "booking": 0,
  "code": 200,
  "facility_list": [
    {
      "css": "wirelessnetwork-ico",
      "id": 1,
      "name": "\u65e0\u7ebf\u7f51\u7edc"
    },
    {
      "css": "shower-ico",
      "id": 2,
      "name": "\u70ed\u6c34\u6dcb\u6d74"
    },
    {
      "css": "aircondition-ico",
      "id": 3,
      "name": "\u7a7a\u8c03"
    },
    {
      "css": "heater-ico",
      "id": 4,
      "name": "\u6696\u6c14"
    },
    {
      "css": "smoke-ico",
      "id": 5,
      "name": "\u5141\u8bb8\u5438\u70df"
    },
    {
      "css": "brush-ico",
      "id": 7,
      "name": "\u7259\u5177"
    },
    {
      "css": "slippers-ico",
      "id": 9,
      "name": "\u62d6\u978b"
    },
    {
      "css": "towel-ico",
      "id": 11,
      "name": "\u6bdb\u5dfe"
    },
    {
      "css": "icebox-ico",
      "id": 13,
      "name": "\u51b0\u7bb1"
    },
    {
      "css": "pet-ico",
      "id": 17,
      "name": "\u5141\u8bb8\u5e26\u5ba0\u7269"
    }
  ],
  "house": {
    "acreage": 35,
    "address": "\u9752\u7f8a\u533a\u95e8\u524d\u5927\u6865\u4e0b",
    "beds": "2x1.8",
    "capacity": 2,
    "deposit": 500,
    "facilities": [
      {
        "css": "wirelessnetwork-ico",
        "id": 1,
        "name": "\u65e0\u7ebf\u7f51\u7edc"
      },
      {
        "css": "shower-ico",
        "id": 2,
        "name": "\u70ed\u6c34\u6dcb\u6d74"
      },
      {
        "css": "aircondition-ico",
        "id": 3,
        "name": "\u7a7a\u8c03"
      },
      {
        "css": "heater-ico",
        "id": 4,
        "name": "\u6696\u6c14"
      },
      {
        "css": "smoke-ico",
        "id": 5,
        "name": "\u5141\u8bb8\u5438\u70df"
      },
      {
        "css": "brush-ico",
        "id": 7,
        "name": "\u7259\u5177"
      },
      {
        "css": "slippers-ico",
        "id": 9,
        "name": "\u62d6\u978b"
      },
      {
        "css": "towel-ico",
        "id": 11,
        "name": "\u6bdb\u5dfe"
      },
      {
        "css": "icebox-ico",
        "id": 13,
        "name": "\u51b0\u7bb1"
      },
      {
        "css": "pet-ico",
        "id": 17,
        "name": "\u5141\u8bb8\u5e26\u5ba0\u7269"
      }
    ],
    "id": 1,
    "images": [
      "\\static\\upload\\a7.jpg",
      "\\static\\upload\\a7.jpg",
      "\\static\\upload\\a2_RscLA9J.jpg"
    ],
    "max_days": 0,
    "min_days": 2,
    "order_count": 0,
    "price": 198,
    "room_count": 1,
    "title": "\u5355\u8eab\u516c\u5bd3",
    "unit": "\u4e00\u5ba4\u4e00\u536b",
    "user_avatar": "/static/upload/a2.jpg",
    "user_name": "zz"
  }
}




