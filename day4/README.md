                作业

需求：
     
功能模块：

1)注册

    函数获取前端一个参数(用户名)
	调用函数,遍历所有用户信息
	验证用户是否存在,有则返回True,否则返回false
	如果用户不存在,获取 用户名,密码，及重新输入密码，三个参数
	判断 密码及重新输入密码是否一致
	用户名密码写入文件
	
2)登录

      获取用户文件,所有信息
	  获取前端用户名，密码两个参数，判断用户名和密码是否正确
	  如果不正确，返回登录界面，如果正确，返回nginx日志html 界面
      
	
文件说明：
          
		  CMDB.py             #主程序
		  User_messages.txt   #用户名密码存储文件
		  static              #静态文件存放目录
		  templates           #html 文件存放目录

<center>login_register 流程图</center >     
                                          
![image](https://github.com/1032231418/python/blob/master/day4/liuchengtu.png)

<center>程序运行结果: </center >

![image](https://github.com/1032231418/python/blob/master/day4/yanshi.gif)

