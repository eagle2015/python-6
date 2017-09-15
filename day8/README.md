第7天作业

作业：

       用户 登录, 注册, 修改, 删除，UI 进行优化，套模板

1.项目分析：

       1).用户管理
	   
	         *.个人中心
			 
			        * 显示个人信息，以及可以，修改个人信息，及添加用户
				
	         *. 用户列表
			 
			        * 显示所有已添加用户信息，可以对用户进行，增加，删除，修改
			
	   2).资产管理	
	   
             *.服务器管理
			 
			     * 显示已添加主机列表，可以对主机，进行，增加，删除，修改
	       
	 

	  
2.项目功能分析:
            
		 1).用户管理相关功能函数:
		 
		       用户登录：login(),获取前端用户输入的账号密码，进行查库判断
                         正确跳转 darshboard()函数返回控制台界面，否则返回错误信息
						 
		       仪表盘: darshboard() 显示后台管理页面
			   
		       用户注册: register(),获取前端用户输入的账号密码信息，进行注册
             
		       用户信息修改: update(),获取用户id，根据用户提交信息进行更新
            
		       用户删除：delete(),获取想要删除的用户id，执行删除操作			
			   
		       个人中心: center(),获取登录用户名，个人中心列表显示该客户个人信息
			   
		       用户列表: userlist(),返回所有用户列表，该功能只有管理员才能查看
			   
		       用户退出: loginout(),退出当前用户，删除session
			   
				  
				  
				  
		 2).资产管理相关功能函数:
		       
		       主机管理列表：hosts(),从数据库读取所有主机信息，渲染到表格显示
			   
		       主机添加: addhost(),获取前端用户输入的主机信息，进行添加
             
		       主机信息修改: updatehost(),获取主机id，根据用户提交信息进行更新
            
		       主机删除：deletehost(),获取想要删除的用户id，执行删除操作	

	 
<center>3.流程图</center > 

![image](https://github.com/1032231418/python/blob/master/day7/liucheng.png)

<center>4.演示</center > 

![image](https://github.com/1032231418/python/blob/master/day7/zy.gif)

<center>5.目录结构</center > 

![image](https://github.com/1032231418/python/blob/master/day7/mulu.png)




