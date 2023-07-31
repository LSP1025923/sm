# -*- coding: utf-8 -*-
# @Time : 2023/7/31 18:25
# @Author : 4C69
"""
用户视图层
"""


# 0、退出
def sign_out():
    print('\n感谢使用，欢迎下次光临!')
    exit()


# 1、注册功能
def register():
    while True:
        # 1、让用户输入用户名和密码
        print('\n注册')
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        is_register = input('按任意键确认/n退出：').lower()

        # 2、进行简单的逻辑判断
        # 2.1、判断用户是否想要退出
        if is_register == 'n':
            break

        # 2.2、判断两次输入密码是否一致
        if password != re_password:
            print('\n两次输入的密码不一致！')
            continue

        import re
        # 2.3、校验用户名是否合法



# 2、登录功能
def login():
    print('登录功能')


# 3、充值功能
def recharge():
    print('充值功能')


# 4、转账功能
def transfer():
    print('转账功能')


# 5、提现功能
def withdraw():
    print('提现功能')


# 6、查看余额
def check_balance():
    print('查看余额')


# 7、查看流水
def check_flow():
    print('查看流水')


# 8、购物功能
def shopping():
    print('购物功能')


# 9、查看购物车
def check_shopping_cart():
    print('查看购物车')


# 10、退出账号
def login_out():
    print('退出功能')


# 11、管理员功能
def admin():
    print('管理员功能')

#函数字典
func_dic = {
    '0': ('退出', login_out),
    '1': ('注册功能', register),
    '2': ('登录功能', login),
    '3': ('充值功能', recharge),
    '4': ('转账功能', transfer),
    '5': ('提现功能', withdraw),
    '6': ('查看余额', check_balance),
    '7': ('查看流水', check_flow),
    '8': ('购物功能', shopping),
    '9': ('查看购物车', check_shopping_cart),
    '10': ('退出账号', login_out),
    '11': ('管理员功能', admin),
}


#主程序
def main():
    while True:
        print('购物管理系统'.center(20, '='))
        for num in func_dic:
            print(f'{num} {func_dic.get(num)[0]}'.center(20, ' '))

        print('我是有底线的'.center(20, '='))
        opt = input('请输入功能编号：').strip()
        if opt not in func_dic:
            print('此功能不存在')
            continue
        func_dic.get(opt)[1]()