#coding=utf-8
from test.order import CreatOrder
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
try:
    yongche=CreatOrder()
    yongche.open_yongche()
    yongche.login_yongche()
    yongche.jump_handler()
    yongche.find_user()
    yongche.create_order()
    '''
    #判断函数返回结果，如果为True,则退出程序
    result=yongche.choose_driver()
    while result:
        exit()#退出程序
    '''
    '''
    #判断函数返回结果，如果为真就继续调用下一个函数，为假则关闭浏览器
    yongche.choose_driver()
    if yongche.choose_driver()==True:
        yongche.cancle_order()
    else:
        print ("No driver found")
    '''
    yongche.send_order_to_alldrivers()
    yongche.cancle_order()
    yongche.quit_browser()
except Exception as e:
    print ('Exception found',format(e))
    #yongche.quit_browser()