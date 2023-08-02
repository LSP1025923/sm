# -*- coding: utf-8 -*-
# @Time : 2023/7/31 18:28
# @Author : 4C69
"""
用户相关接口
"""

from db import db_handler


# 注册接口
def register_interface(username, password, is_admin=False, balance=0):
    """

    :param username: 用户名 str
    :param password: 密码 str
    :param is_admin: 是否是管理员，boolean
    :param balance: 初始余额 int
    :return:(boolean, str)
    """
    # 1、调用接口层的查询功能，查询用户名是否已存在
    if db_handler.select_data(username, False):
        return False,'\n用户名已存在！'
    # 2、组织用户字典
    user_data = {
        'username': username,
        'password': password,
        'balance': balance,
        'shopping_cart': [],
        'flow': [],
        'is_admin': is_admin,
        'locked': False,
    }

    # 3、调用数据处理层，保存用户数据
    db_handler.save(user_data)

    return True, f'\n用户：{username}注册成功!'