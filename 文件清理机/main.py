#coding:gbk     #因为在win10下执行程序乱码所以改成gbk格式
import os

#默认的清理目录
default_path = "D:\ACM-Program"

#清理的文件数量
clear_file_number = 0

#extensions代表指定要删除的文件扩展名
extensions = ('.exe', '.o')

#清屏
def clear_screen():
    os.system('cls')

#按任意键继续
def pause():
    os.system('pause')

#打印N个指定的字符
def print_char(count, c):
    for i in range(0,count):
        print c,

#返回指定目录下所有的文件和目录
def get_all_path(path):
    return os.listdir(path)

#获取文件的扩展名
def file_extension(path):
    return os.path.splitext(path)[1]

#清理文件
def clear_dir(root_path):

    clear_file_number = 0  #被清理的文件数量

    paths = get_all_path(root_path)   #得到目录下所有文件与目录

    for path in paths:
        full_path = os.path.join(root_path,path)   #得到完整的路径名
        if os.path.isdir(full_path):   #如果是目录的递归清理
            clear_file_number = clear_file_number + clear_dir(full_path)
        else:
            extension = file_extension(full_path)   #如果是文件的话获取文件扩展名
            if extension in extensions or '.' not in full_path:    #如果是要删除的文件则进行删除
                os.remove(full_path)
                clear_file_number = clear_file_number + 1  #被清理的文件数量+1
    return clear_file_number

#主菜单
def menu():
    print_char(20,' ')
    print "文件清理机"    #标题
    
    print_char(20,' ')  
    print "运行模式"
    
    print_char(15,' ')  #选项
    print "模式1、默认工作方式"

    print_char(15, ' ')
    print "模式2、由键盘输入要清理的文件目录"

    print_char(15,' ')
    print "模式3、查看要被清理的文件数量(默认文件夹)"

    print_char(15,' ')
    print "模式4、查看要被清理的文件数量并显示该文件(默认文件夹)"

    print_char(15,' ')
    print "选项0、退出"

#寻找共有多少个需要被清理的文件
#递归实现，与清理文件相似
def find_file_number(root_path, status):

    file_number = 0   #需要清理的文件数量
    
    paths = get_all_path(root_path)

    for path in paths:
        full_path = os.path.join(root_path, path)
        if os.path.isdir(full_path):
            file_number = file_number + find_file_number(full_path, status)
        else:
            extension = file_extension(full_path)
            if extension in extensions or '.' not in full_path:
                if status is True:
                    print full_path
                file_number = file_number + 1
    return file_number
            

#程序主要逻辑，完成文件清理工作
def run():
    while True:
        menu()
        clear_file_number = 0
        way = raw_input("请选择工作方式")
        if way == '1':
            clear_file_number = clear_dir(default_path)
            print "成功清理文件"+str(clear_file_number)+"个，请继续使用"
            pause()
        elif way == '2':
            root_path = raw_input("请输入要清理的文件目录")
            clear_file_number = clear_dir(root_path)
            print "成功清理文件"+str(clear_file_number)+"个，请继续使用"
            pause()
        elif way == '3':
            file_number = find_file_number(default_path, False)
            print "共发现"+str(file_number)+"个需要清理的文件"
            pause()
        elif way == '4':
            file_number = find_file_number(default_path, True)
            print "共发现"+str(file_number)+"个需要清理的文件"
            pause()
        elif way == '0':
            print "欢迎下次使用"
            break
        else:
            print "输入非法指令，请重新输入指令"
            pause()
        clear_screen()   #清屏

#如果作为主程序启动，开始执行代码
if __name__ == "__main__":
    run()
