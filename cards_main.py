# shebang
#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import cards_tools
# infinite loop, 由用户主动推出循环
while True:


    cards_tools.show_menu()


    action_str = input("Please choose the operation you want to execute:")
    print("The operation has been chosen is [%s]" % action_str)


    # Operations include 1, 2, 3 and quit(0)
    if action_str in ["1", "2", "3"]:
        #新增名片
        if action_str == "1":
            cards_tools.new_card()
        #显示全部
        elif action_str == "2":
            cards_tools.show_all()

        elif action_str == "3":
            cards_tools.search_card()
        
    elif action_str == "0":

        print("Welcome to use this App again!")

        break
        # 如果在开发程序时，不希望立刻编写分支内部代码
        # 可使用pass关键字，表示一个占位符，能够保证程序代码的结构正确
        # 程序运行时，pass不会执行任何操作
        #pass
    # else, there needs a reminder to inform the error
    else:
        print("Error!")
