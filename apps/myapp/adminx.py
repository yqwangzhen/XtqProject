import xadmin
from myapp.models import User_table
from xadmin import views




class UserAdmin():
    list_display = [
        'username',
        'password',
        'email',

    ]

#将模型类对象添加到后台显示的，定制显示的类
xadmin.site.register(User_table,UserAdmin)