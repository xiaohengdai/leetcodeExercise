Linux awk 命令:https://m.runoob.com/linux/linux-comm-awk.html
xargs就是可以将管道｜的参数的数据转换成命令行参数，就是相当于一个过滤器，组合多个命令的一个小工具。



如果这个有一系列进程出来，如何用shell解析出一串进程id？
ps -ef|grep python|awk '{print $2}'

Linux中批量杀掉100个Java进程
ps -ef | grep java | grep -v grep | awk '{print $2}' | xargs kill -9