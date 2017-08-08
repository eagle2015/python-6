#!/usr/bin/env python
#_*_ coding:utf-8 _*_

def User_lockd(Username):
    #1. 判断用户是否锁定
    user_locked  = file('user_lockd.txt')
    for  lines in  user_locked.readlines():
        if  Username  in  lines:
            return 'locked'

def User_empty(Username):
    #2. 判断用户名是否为空
    empty = False
    if len(Username) == 0:
        print "用户名不能为空，请重新输入！"
        empty = True
    return empty



def User_already_exists(Username):
    #3. 判断用户名是否存在
    Usr_messages = file('user_messages.txt', 'rb')
    match_flag = False
    for line in Usr_messages.readlines():
        user, passwd  = line.strip(' ').split()
        if Username == user :
            match_flag = True
    Usr_messages.close()
    return  match_flag

def Password_length(Password):
    #4. 判断密码长度
    Short = False
    if len(Password) > 6  and  len(Password) != 0:
        Short = False
    else:
        print "Password  so Short"
        Short = True
    return  Short

def  User_password_authentication(Username,Password):
    #5. 判断用户名密码是否正确
    user_messages = file('user_messages.txt','rb')
    match_flag = False
    for line in user_messages.readlines():
        user, passwd  = line.strip(' ').split()
        if Username == user and Password == passwd:
            match_flag = True
    user_messages.close()
    return  match_flag

def lock_Username(Username):
    #6. 锁定用户
    print "The  User %s  is  locked" % (Username)
    rw_user_lockd = file('user_lockd.txt', 'ab')
    rw_user_lockd.write(Username)
    rw_user_lockd.write("\n")
    rw_user_lockd.close()

def  write_User_messages(Username,Password):
    #7. 写入注册用户名密码
    messages_file = open('user_messages.txt', 'a+')
    messages_file.write("%s %s\n" % (Username, Password))
    messages_file.close()
    print  "恭喜你已经注册成功"


def login():
    counts =0
    Username = raw_input('Please input Username:')

    while counts < 3:
	        #  调用函数，判断用户名是否为空
        if User_empty(Username)  == True:
            break
        #  如果调用函数返回locked 说明用户被锁定，打印消息并退出
        if User_lockd(Username) == 'locked':
            print "The  User %s  is  locked" % (Username)
            break

        else:
            Password = raw_input('Please input Password:')


            # 判断函数返回True还是False,如果返回True 则密码太短，否则就是符合长度
            if  Password_length(Password) == True :
                counts += 1
            else:

                # 调用函数，判断用户名密码是否正确，如果错误记录次数
                if  User_password_authentication(Username, Password) != True:
                    counts += 1
                    print 'User name or password Error'
                else:

                    # 正确就返回欢迎信息
                    print "####Wlcome  %s login####" % (Username)
                    break
    else:

        # 将输入密码错误三次的用户锁定
        lock_Username(Username)




def  register():

    counts = 0
    Username = raw_input('Please input Username:').strip()
    while counts < 3:
        # 调用函数,判断用户名是否为空
        if User_empty(Username)  == True:
            break
        else:
            # 调用函数,判断用户是否被锁定
            if User_lockd(Username) == 'locked':
                print "The  User %s  is  locked" % (Username)
                break
            # 调用函数,判断用户是否存在
            if User_already_exists(Username) == True:
                print "该用户已经存在"
                break

            else:
                # 输入两次密码
                Password = raw_input('Please input Password:').strip()
                Repeat_Password = raw_input('Please Repeat input  Password:').strip()
                # 调用函数,判断密码长度
                if  Password_length(Password) == True :
                    counts += 1
                else:
                    if  Password != Repeat_Password :
                        print "两次密码输入有误"
                        counts += 1
                        continue
                    else:
                        # 用户名密码符合要求，调用函数，写入文件
                        write_User_messages(Username, Password)
                        break


if __name__ == '__main__':
    while True:
        try:
            login_or_register = int(raw_input( '请输入数字:' '注册/1,登录/2:>').strip())
            #判断类型错误
        except ValueError,e:
            print '输入的不是数字！'
        else:
            #输入1，调用注册函数，输入 2调用登录函数,输入其他，不合法
            if login_or_register == 1:
                register()
            elif login_or_register == 2:
                login()
            else:
                print '输入不合法！'