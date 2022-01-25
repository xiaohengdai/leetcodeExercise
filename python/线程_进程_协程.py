# Python之协程:https://www.cnblogs.com/russellyoung/p/python-zhi-xie-cheng.html

#-*- coding:utf8 -*-
import gevent

def test(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

if __name__ == '__main__':
    g1 = gevent.spawn(test, 3)
    g2 = gevent.spawn(test, 3)
    g3 = gevent.spawn(test, 3)

    g1.join()
    g2.join()
    g3.join()
