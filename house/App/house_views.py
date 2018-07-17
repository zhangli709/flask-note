import os


from flask import Blueprint, render_template, session, jsonify, request
from sqlalchemy import or_

from App.models import User, House, Area, Facility, HouseImage, Order
from utils import status_code
from utils.function import is_login
from utils.settings import UPLOAD_DIRS

house_blueprint = Blueprint('house', __name__)


# 我的房源
@is_login
@house_blueprint.route('/myhouse/', methods=['GET'])
def my_house():
    return render_template('myhouse.html')


# 将我的房源的信息展示出来
@is_login
@house_blueprint.route('/auth_myhouse/', methods=['GET'])
def auth_myhouse():

    user = User.query.get(session['user_id'])
    if user.id_card:
        # 按照id从大到小排序，时间顺序
        houses = House.query.filter(House.user_id == user.id).order_by(House.id.desc())
        hlist_list = []
        # 此处重点，如何将数据库里的内容，转换为我们需要的json格式
        for house in houses:
            hlist_list.append(house.to_dict())
        return jsonify(hlist_list=hlist_list, code=status_code.OK)
    else:

        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


# 新房源 展示页面
@is_login
@house_blueprint.route('/newhouse/', methods=['GET'])
def newhouse():
    return render_template('newhouse.html')


# 将新房源的具体信息，通过ajax加载出来
@is_login
@house_blueprint.route('/area_facility/', methods=['GET'])
def area_facility():
    # 获取区域和设施的信息
    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    facilitys = Facility.query.all()
    facility_list = [facility.to_dict() for facility in facilitys]
    # 返回json,给ajax,然后渲染出来
    return jsonify(area_list=area_list, facility_list=facility_list)


# 房源的文字信息提交
@is_login
@house_blueprint.route('/newhouse/', methods=['POST'])
def user_newhouse():

    # 前端提交了一个表单给我们，我们可以直接解析表单form
    house_dict = request.form.to_dict()
    # 获取重复的设施
    facility_ids = request.form.getlist('facility')

    house = House()
    house.user_id = session['user_id']
    house.title = house_dict.get('title')
    house.price = house_dict.get('price')
    house.area_id = house_dict.get('area_id')
    house.address = house_dict.get('address')
    house.root_count = house_dict.get('root_count')
    house.acreage = house_dict.get('acreage')
    house.unit = house_dict.get('unit')
    house.capacity = house_dict.get('capacity')
    house.beds = house_dict.get('beds')
    house.deposit = house_dict.get('deposit')
    house.min_days = house_dict.get('min_days')
    house.max_days = house_dict.get('max_days')

    # 保存到数据库
    if facility_ids:
        # 所有设施的列表
        facilitys = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        house.facilities = facilitys
        # house.facilities.append(1) 原先做法，一个一个加，现在直接加列表，一次加一个列表
    try:
        house.add_update()
        # 将房屋id，一并传过去使用
        return jsonify(code=status_code.OK, house_id=house.id)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 新房源的图片提交
@is_login
@house_blueprint.route('/images/', methods=['POST'])
def newhouse_images():
    # 获取上传的图片
    images = request.files.get('house_image')
    house_id = request.form.get('house_id')

    # 保存图片到指定位置
    url = os.path.join(UPLOAD_DIRS, images.filename)
    images.save(url)

    # 再数据库里保存路径
    image_url = os.path.join(os.path.join('/static/upload/'), images.filename)
    house_image = HouseImage()
    house_image.house_id = house_id
    house_image.url = image_url

    try:
        house_image.add_update()
    except:
        return jsonify(status_code.DATABASE_ERROR)

    house = House.query.get(house_id)

    # 如果为空,用处，将图片的第一张图绑定在房屋上，可以少访问一次图片库
    if not house.index_image_url:
        # image_url = '/static/upload/' + images.filename
        house.index_image_url = image_url
        try:
            house.add_update()
        except:
            return jsonify(status_code.DATABASE_ERROR)

    return jsonify(code=status_code.OK, image_url=image_url)


# 展示房源的详细页面
@is_login
@house_blueprint.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


# 通过ajax,展示房源的具体信息
@is_login
@house_blueprint.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):

    house = House.query.get(id)

    # 获得详情
    facility_list = house.facilities
    facility_dict_list = [facility.to_dict() for facility in facility_list]

    # booking用来判断是否是房东登录
    booking = 1
    if 'user_id' in session:
        house.user_id = session['user_id']
        booking = 0
    return jsonify(house=house.to_full_dict(),
                   facility_list=facility_dict_list,
                   booking=booking,
                   code=status_code.OK)


# 展示预定页面
@is_login
@house_blueprint.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')


# 返回首页
@house_blueprint.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')


# ajax请求页面信息的接口
@house_blueprint.route('/hindex/', methods=['GET'])
def house_index():

    user_name = ''

    # 用户
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        user_name = user.name

    # 房子信息
    houses = House.query.order_by(House.id.desc()).all()[0:5]
    hlist = [house.to_dict() for house in houses]

    # 区域
    areas = Area.query.all()
    alist = [area.to_dict() for area in areas]

    return jsonify(code=status_code.OK,
                   user_name=user_name,
                   hlist=hlist,
                   alist=alist)


@house_blueprint.route('/search/', methods=['GET'])
def search():

    return render_template('search.html')


@house_blueprint.route('/allsearch/', methods=['GET'])
def house_search():

    # 如果没有值，就显示全部的没有被预定的房屋，
    # 如果有值，就显示对应区域的没有被预定的房屋
    search_dict = request.args

    area_id = search_dict.get('aid')
    start_date = search_dict.get('sd')
    end_date = search_dict.get('ed')
    # 排序
    sort_key = search_dict.get('sk')

    # 房屋信息
    houses = House.query.filter(House.area_id==area_id)

    # 对房屋进行查询，处理
    # orders = Order.query.filter(or_(Order.begin_date > end_date, Order.end_date < start_date))

    orders1 = Order.query.filter(Order.begin_date >= start_date, Order.end_date <= end_date)
    orders2 = Order.query.filter(Order.begin_date <= end_date, Order.end_date >= end_date)
    orders3 = Order.query.filter(Order.begin_date <= start_date, Order.end_date >= start_date)
    orders4 = Order.query.filter(Order.begin_date <= start_date, Order.end_date >= end_date)

    orders_list1 = [o1.house_id for o1 in orders1]
    orders_list2 = [o2.house_id for o2 in orders2]
    orders_list3 = [o3.house_id for o3 in orders3]
    orders_list4 = [o4.house_id for o4 in orders4]

    orders_list = orders_list1 + orders_list2 + orders_list3 + orders_list4
    orders_list = list(set(orders_list))
    houses = houses.filter(House.id.notin_(orders_list))

    if sort_key:
        if sort_key == 'booking':
            sort_key = House.room_count.desc()
        if sort_key == 'price-inc':
            sort_key = House.price.asc()
        if sort_key == 'price-des':
            sort_key = House.price.desc()
    else:
        sort_key = House.id.desc()

    houses = houses.order_by(sort_key)

    hlist = [house.to_dict() for house in houses]

    # 地区信息
    areas = Area.query.all()
    alist = [area.to_dict() for area in areas]

    return jsonify(code=status_code.OK,
                   hlist=hlist,
                   alist=alist)