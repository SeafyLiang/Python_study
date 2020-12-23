# coding=utf-8
# @Time : 2020/12/23 09:52 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : mycode.py
# @desc :

class A(object):
    """
    Description
    """

    def __init__(self, x, y, default=None):
        self.z = x + y
        self.default = default

    def name(self):
        return 'No Name'


def always():
    return True


if __name__ == '__main__':
    num = 1
    a = A(num, 999, 100)
    print(a.name())
    always()