第8天作业

作业：

       CMDB 进阶，对已知CMDB 界面进行扒取，并完成对应功能

1.项目分析：

       1).用户管理
	   
	         *.个人中心
			 
			        * 显示个人信息，以及可以，修改个人信息，及添加用户
				
	         *. 用户列表
			 
			        * 显示所有已添加用户信息，可以对用户进行，增加，删除，修改
			
	   2).资产管理	
	   
             *.机房管理
			 
			        * 显示已添加机房信息，可以对机房信息，进行，增加，删除，修改
			 
	         *.机柜管理
			 
			        * 显示已添加机柜列表，可以对机柜，进行，增加，删除，修改
				 
             *.服务器管理
			 
			        * 显示已添加主机列表，可以对主机，进行，增加，删除，修改				 
	  3).工单系统
	            
             *.工单申请
				
			        * 提交新工单
				
             *.申请列表
				
			        * 显示已提交，未完成工单,可对工单状态，工单信息进行修改
					
             *.历史工单
				
			        * 可以看到，已提交所有工单，可以查看工单详情
				
			
	          

	  
2.项目功能分析:

       1).用户管理
	   
	       *.用户登录/退出 
		   
		        函数文件: login.py 
			   
			          login()            获取前端输入账号密码，进行判断是否正确,用户是否锁定
			          loginout()         用户退出
                      
	       *.个人中心
		   
		        函数文件:  user.py
			   
			          center()           用户个人中心，显示已登录用户个人信息
			          chpwdoneself()     修改个人密码
			          chmessageoneself() 修改个人资料
			   
		   *. 用户列表
		       
			     函数文件： userlist.py
				
			          userlist()         用户列表，显示已添加用户列表
			          update()           更新用户信息
			          add()              添加新用户
			          delete()           删除用户
			
	   2).资产管理

             *.机房管理
			     
			     函数文件：idc.py
				      
			          idc()             显示已添加 idc列表
			          idcadd()          添加机房
				      idcupdate()       修改机房信息
			          idcdelete()       删除机房
		
	         *.机柜管理
                  
                 函数文件： cabinet.py
                       
 			          cabinet()         机柜列表，显示已添加机柜信息
			          cabinetadd()      添加新机柜
			          cabinetupdate()   机柜信息修改
			          cabinetdelete()   删除机柜
				 
	         *.服务器管理
         	    
                 函数文件: server.py
				 
 			          server()          显示已添加机服务器列表
 			          serveradd()       添加新服务器
 			          serverupdate()    更新服务器信息
 			          serverdelete()    删除服务器
		                               
	  3).工单系统
	          
                 函数文件：  job.py
            	  
            *.工单申请
			    
 			          jobadd()          添加新工单
				
            *.申请列表
				
 			          joblist()         工单列表
 			          jobupdate()       更新工单信息
 			          jobdetail()       查看工单详情
				     
            *.历史工单
			    
 			          jobhistory() 历史工单列表
				
 				
	

	 
<center>3.流程图</center > 

![image](https://github.com/1032231418/python/blob/master/day8/naotu.png)


<center>4.演示 </center > 


![image](https://github.com/1032231418/python/blob/master/day8/yanshi.gif)

<center>5.目录结构</center > 

![image](https://github.com/1032231418/python/blob/master/day8/jiegou.PNG)




