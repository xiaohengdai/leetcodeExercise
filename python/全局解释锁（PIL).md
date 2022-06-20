#因为python的内存管理是通过引用计数的，这个引用计数变量需要在两个线程同时增加或减少时从竞争条件中得到保护。如果发生了这种情况，可能会导致泄露的内存永远不会被释放，抑或更严重的是当一个对象的引用仍然存在的情况下错误地释放内存。这可能会导致Python程序崩溃或带来各种诡异的bug。
#什么是python的全局解释锁（GIL）?：https://blog.csdn.net/Beyond_F4/article/details/79951226
python 解释器是非完全线程安全的。为了支持多线程，python有一个全局锁，叫GIL(Global Interpreter Lock) or GIL, 这个锁必须为当前线程所拥有来操作python对象。
解决多线程效率低的方法:
1、多进程 + 多线程 的方式 来弥补这一短板上的问题，通过多进程在每个 CPU 跑道上执行任务，并且每个进程的跑道上再去执行多个线程。 ，让它们在各自的时间片上去运行。
2、用其它python解释器（CPython会有GIL）
GIL的设计以是为了避免“竞争危害”以保证线程安全
【Python】到底什么是全局解释器锁（GIL）？：https://zhuanlan.zhihu.com/p/493266886