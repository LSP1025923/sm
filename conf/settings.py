# -*- coding: utf-8 -*-
# @Time : 2023/7/31 18:57
# @Author : 4C69
"""
配置信息
"""

# 获取项目根目录
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)




CONFIG_PATH = os.path.join(
    BASE_DIR,'settings.ini'
)

# 获取USER_DADA路径

import configparser

config = configparser.ConfigParser()
config.read(CONFIG_PATH, encoding='utf-8-sig')
USER_DATA_DIR = config.get('path', 'USER_DATA_DIR')
if not os.path.isdir(USER_DATA_DIR):
    USER_DATA_DIR = os.path.join(
        BASE_DIR, 'db', 'user_data'
    )
