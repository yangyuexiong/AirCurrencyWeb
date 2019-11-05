# -*- coding: utf-8 -*-
# @Time    : 2019-11-05 18:21
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : config.py
# @Software: PyCharm


from datetime import timedelta
import os

import redis


def app_conf():
    config_key = 'development'

    if os.environ.get('FLASK_ENV') == 'development':
        config_key = 'development'
        # print('开发环境:%s' % config_key)
        return config_key

    elif os.environ.get('FLASK_ENV') == 'production':
        config_key = 'production'
        # print('生产环境:%s' % config_key)
        return config_key
    else:
        config_key = 'production'
        # print('生产环境:%s' % config_key)
        return config_key


class BaseConfig:
    """配置基类"""
    # SECRET_KEY = os.urandom(24)
    SECRET_KEY = 'ShaHeTop-Almighty-ares'  # session加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)  # 设置session过期时间
    DEBUG = True
    # SERVER_NAME = 'example.com'
    RUN_HOST = '0.0.0.0'
    RUN_PORT = 9999

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    """开发环境"""

    """Redis"""
    # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    REDIS_PWD = 123456
    POOL = redis.ConnectionPool(host='localhost', port=6379, password=REDIS_PWD, decode_responses=True, db=0)
    R = redis.Redis(connection_pool=POOL)


class ProductionConfig(BaseConfig):
    """生产环境"""
    DEBUG = False
    RUN_PORT = 5000

    """Redis"""
    # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    REDIS_PWD = 123456
    POOL = redis.ConnectionPool(host='localhost', port=6379, password=REDIS_PWD, decode_responses=True, db=0)
    R = redis.Redis(connection_pool=POOL)


config_obj = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

if __name__ == '__main__':
    cof = app_conf()
    print(cof)
