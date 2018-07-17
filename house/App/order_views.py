from datetime import datetime
from flask import Blueprint, request, render_template, jsonify, session

from App.models import Order, House
from utils import status_code
from utils.status_code import OK

order_blueprint = Blueprint('order', __name__)


# 把预定的房屋信息和时间，保存再数据库里
@order_blueprint.route('/', methods=['POST'])
def order():

    order_dict = request.form

    house_id = order_dict.get('house_id')
    start_time = datetime.strptime(order_dict.get('start_time'), '%Y-%m-%d')
    end_time = datetime.strptime(order_dict.get('end_time'), '%Y-%m-%d')

    if not all([house_id, start_time, end_time]):
        return jsonify(status_code.PARAMS_ERROR)

    if start_time > end_time:
        return jsonify(status_code.ORDER_START_TIME_GT_END_TIME)

    order = Order()
    house = House.query.get(house_id)

    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = start_time
    order.end_date = end_time
    order.days = (end_time - start_time).days + 1
    order.house_price = house.price
    order.amount = order.house_price * order.days

    try:
        order.add_update()
        return jsonify(code=status_code.OK,)
    except:
        return jsonify(status_code.PARAMS_ERROR)


@order_blueprint.route('/order/', methods=['GET'])
def orders():
    return render_template('orders.html')


# 获取当前用户的所有订单，我的订单
@order_blueprint.route('/allorders/', methods=['GET'])
def all_orders():
    user_id = session['user_id']
    order_list = Order.query.filter(Order.user_id == user_id)
    order_list2 = [order.to_dict() for order in order_list]

    return jsonify(code=OK, order_list=order_list2)


# 客户订单
@order_blueprint.route('/lorders/', methods=['GET'])
def lorders():

    return render_template('lorders.html')


# 展示客户订单里的所有房子
@order_blueprint.route('/fd/', methods=['GET'])
def lorders_fd():

    # 查询房东房屋的id,查询当前用户拥有的房子
    houses = House.query.filter(House.user_id == session['user_id'])
    houses_ids = [house.id for house in houses]
    # 通过房屋的id找订单，查看这些房子是否被预定 ，需要显示当前登录的用户拥有的房子，被预定的信息。
    orders = Order.query.filter(Order.house_id.in_(houses_ids)).order_by(Order.id.desc())
    order_list = [order.to_dict() for order in orders]

    return jsonify(olist=order_list, code=status_code.OK)


# 接单，拒单的接口
@order_blueprint.route('/order/<int:id>/', methods=['PATCH'])
def order_status(id):
    status = request.form.get('status')

    order = Order.query.get(id)
    order.status = status

    if status == 'REJECTED':
        comment = request.form.get('comment')
        order.comment = comment
    try:
        order.add_update()
        return jsonify(status_code=OK)
    except:
        return jsonify(status_code.DATABASE_ERROR)

