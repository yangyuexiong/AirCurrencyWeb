# -*- coding: utf-8 -*-
# @Time    : 2019-11-05 18:32
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : module_1.py
# @Software: PyCharm

import os

from flask import Blueprint, render_template, request
from config.config import app_conf, config_obj, redis_obj

route_module_01 = Blueprint('module_01', __name__)

R = config_obj[app_conf()].R


@route_module_01.route('/dev/index', methods=["GET", "POST"])
@route_module_01.route('/dev/index/<ex>', methods=["GET", "POST"])
def index(ex=None):
    """

    :param ex:
    :return:
    """
    R = redis_obj(0)
    path_1 = os.getcwd().split('AirCurrencyWeb')[0]  # 系统目录
    path_2 = 'AirCurrencyWeb/app/static'
    report_dir = path_1 + path_2

    lists = os.listdir(report_dir)  # 报告列表
    lists = [i for i in lists if 'pro' not in i]
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + '/' + fn))  # 排序
    # lists = lists[1:11]
    lists.reverse()
    print(lists)

    env_path = request.path
    if ex == 'okex':
        print('okex')
        exchange = 'okex'
        exchange_key = 'exchange:%s' % exchange
        context = R.hgetall(exchange_key).items()
        return render_template('index.html', context=context, r_list=lists, ex=ex, env_path=env_path)

    if ex == 'bitfinex':
        print('bitfinex')
        exchange = 'bitfinex'
        exchange_key = 'exchange:%s' % exchange
        context = R.hgetall(exchange_key).items()
        return render_template('index.html', context=context, r_list=lists, ex=ex, env_path=env_path)

    if ex == 'huobi':
        print('huobi')
        exchange = 'huobi'
        exchange_key = 'exchange:%s' % exchange
        context = R.hgetall(exchange_key).items()
        return render_template('index.html', context=context, r_list=lists, ex=ex, env_path=env_path)

    else:
        print('all')
        R.keys('exchange*')
        print(R.keys('exchange*'))
        all_err_exchang = {}
        for i in R.keys('exchange*'):
            all_err_exchang.update(R.hgetall(i))
        context = all_err_exchang.items()
        return render_template('index.html', context=context, r_list=lists, env_path=env_path)


@route_module_01.route('/pro/index', methods=["GET", "POST"])
@route_module_01.route('/pro/index/<ex>', methods=["GET", "POST"])
def pro(ex=None):
    R = redis_obj(1)
    path_1 = os.getcwd().split('AirCurrencyWeb')[0]  # 系统目录
    path_2 = 'AirCurrencyWeb/app/static'
    report_dir = path_1 + path_2

    lists = os.listdir(report_dir)  # 报告列表
    lists = [i for i in lists if 'dev' not in i]
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + '/' + fn))  # 排序
    # lists = lists[1:11]
    lists.reverse()
    print(lists)

    env_path = request.path
    if ex == 'okex':
        print('okex')
        exchange = 'okex'
        exchange_key = 'exchange:%s' % exchange
        context = R.hgetall(exchange_key).items()
        return render_template('index.html', context=context, r_list=lists, ex=ex, env_path=env_path)

    if ex == 'bitfinex':
        print('bitfinex')
        exchange = 'bitfinex'
        exchange_key = 'exchange:%s' % exchange
        context = R.hgetall(exchange_key).items()
        return render_template('index.html', context=context, r_list=lists, ex=ex, env_path=env_path)

    if ex == 'huobi':
        print('huobi')
        exchange = 'huobi'
        exchange_key = 'exchange:%s' % exchange
        context = R.hgetall(exchange_key).items()
        return render_template('index.html', context=context, r_list=lists, ex=ex, env_path=env_path)

    else:
        print('all')
        R.keys('exchange*')
        print(R.keys('exchange*'))
        all_err_exchang = {}
        for i in R.keys('exchange*'):
            all_err_exchang.update(R.hgetall(i))
        context = all_err_exchang.items()
        return render_template('index.html', context=context, r_list=lists, env_path=env_path)
