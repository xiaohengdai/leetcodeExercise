1、Android四大组件
活动/内容/服务/提供广播接收器
2、活动的五种生命周期状态
启动/运行/暂停/停止/销毁

3、Android中Service的生命周期与启动方法有什么区别？
●startService()：开启Service，调用者退出后Service仍然存在。
●bindService()：开启Service，调用者退出后Service也随即退出。

Service生命周期：

●只是用startService()启动服务：onCreate() -> onStartCommand() -> onDestory
●只是用bindService()绑定服务：onCreate() -> onBind() -> onUnBind() -> onDestory
●同时使用startService()启动服务与bindService()绑定服务：onCreate() -> onStartCommand() -> onBind() -> onUnBind() -> onDestory
