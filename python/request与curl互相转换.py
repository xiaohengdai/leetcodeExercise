#curl与request互相转换：https://www.likecs.com/show-305752107.html

import  curlify
import requests

req=requests.get("https://ww.baidu.com")
ret1=curlify.to_curl(req.request)
print(ret1)