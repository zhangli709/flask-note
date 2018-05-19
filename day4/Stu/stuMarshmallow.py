from utils.function import ma


# 序列化，配合restful使用，返回数据，按照我们这设置的规则展示
class StuMarsh(ma.Schema):

    class Meta:
        # 筛选，修饰
        fields = ('s_name', 's_age')


stumarsh = StuMarsh()