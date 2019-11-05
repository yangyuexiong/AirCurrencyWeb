# -*- coding: utf-8 -*-
# @Time    : 2019-11-05 18:32
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : module_1.py
# @Software: PyCharm


from flask import Blueprint, render_template
from config.config import app_conf, config_obj

route_module_01 = Blueprint('module_01', __name__)

R = config_obj[app_conf()].R

exchange = 'bitfinex'
exchange_key = 'exchange:%s' % exchange
R.hgetall(exchange_key).items()


@route_module_01.route('/index', methods=["GET", "POST"])
def index():
    context = R.hgetall(exchange_key).items()
    return render_template('index.html', context=context)


@route_module_01.route('/rp_list', methods=["GET", "POST"])
def report_list():
    return render_template('测试报告_2019-11-05 15_57_14_.html')
