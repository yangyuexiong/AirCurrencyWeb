# -*- coding: utf-8 -*-
# @Time    : 2019-11-05 18:27
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : bp_register.py
# @Software: PyCharm


from app.controllers.show_reports.module_1 import route_module_01


def register_bp(app):
    """蓝图注册"""

    app.register_blueprint(route_module_01, url_prefix="/v1")
