from django.contrib import admin

# Register your models here.

# users/adminx.py

import xadmin

from .models import EmailVerifyRecord, Banner
from xadmin import views


# 创建xadmin的最基本管理器配置，设置基础和全局配置
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "大数据智能选课平台"  #设置头部显示
    site_footer = "NBA.com"
    menu_style = "accordion"        #菜单折叠
    apps_icons = {"appname":"icon"}  #设置app的显示图


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

