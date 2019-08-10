import random

def ranstr(num):
    # 猜猜变量名为啥叫 H   wkz:hand??? 凡是能用键盘打出来的字符？？
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*-+,./;[]}{~!@#$%^&*()'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt