#!/usr/bin/env pytthon
# -*- coding: utf8 -*-
__author__ = 'Eagle'
import sys
secret = 50
count_num = 0
print ('-----------I love Python-------') 
while  count_num < 3 :
    temp = int(input('不妨猜一下，我心里想的哪个数字：'))
    try:
        guess = int(temp)
    except  Exception,e:
        print "输入错误"
        sys.exit()
        if  isinstance(guess, int ):
            
            if guess == secret:
                print("卧槽，这你都能猜到！")
                break 
            else:
                count_num += 1
                if guess > secret:
                    print ('哥，大了，大了')
                else:
                    print ('嘿，哥，小了，小了')
        else:
            print  "请输入正确的数字"
    print ("哼，不给你玩了")
