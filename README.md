
# 项目名称：MxOnline

---
Big-data Management System
大数据平台智能选课平台


# 项目开发
---
### 项目所依赖的包，启动报错可尝试执行下面的命令
 ```
pip install -r ./requirements.txt
 ```
 
### 启动服务
 ```
 - 启命动令：python ./manage.py runserver
 - 访问地址：http://127.0.0.1:8000/admin/
 - 登陆密码：admin/admin
```

# Django相关资料
---

- 官方文档: https://docs.djangoproject.com/zh-hans/2.2/
- 入门教程: https://www.django.cn/course/show-16.html
- 创建一个django项目: django-admin.py startproject project_name
- 创建应用或功能模块: python manage.py startapp sms 
- 反向生成models: python manage.py inspectdb --database DATABASE > models.py


# xadmin相关资料
---

- xadmin介绍: http://sshwsfc.github.io/xadmin/
- xadmin进阶开发： https://blog.csdn.net/weixin_35705390/article/details/79343376

# 案例：https://blog.csdn.net/qq_34964399/article/details/80303544
- adminx 模块设置
```
    - list_display 控制列表展示的字段
    - search_fields 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
    - list_filter 可以进行过滤操作的列
    - ordering 默认排序的字段
    - readonly_fields 在编辑页面的只读字段
    - exclude 在编辑页面隐藏的字段
    - list_editable 在列表页可以快速直接编辑的字段
    - show_detail_fileds 在列表页提供快速显示详情信息
    - refresh_times 指定列表页的定时刷新
    - list_export 控制列表页导出数据的可选格式
    - show_bookmarks 控制是否显示书签功能
    - data_charts 控制显示图标的样式
    - model_icon 控制菜单的图标
```
- 左侧菜单栏图标的样式列表：
```
    - 图标样式名称：http://fontawesome.dashgame.com/
    - 修改图标方法: model类对应类中添加:model_icon = 'fa fa-user'，即'fa fa-'+icon名
```

