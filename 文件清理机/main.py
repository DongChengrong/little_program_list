#coding:gbk     #��Ϊ��win10��ִ�г����������Ըĳ�gbk��ʽ
import os

#Ĭ�ϵ�����Ŀ¼
default_path = "D:\ACM-Program"

#������ļ�����
clear_file_number = 0

#extensions����ָ��Ҫɾ�����ļ���չ��
extensions = ('.exe', '.o')

#����
def clear_screen():
    os.system('cls')

#�����������
def pause():
    os.system('pause')

#��ӡN��ָ�����ַ�
def print_char(count, c):
    for i in range(0,count):
        print c,

#����ָ��Ŀ¼�����е��ļ���Ŀ¼
def get_all_path(path):
    return os.listdir(path)

#��ȡ�ļ�����չ��
def file_extension(path):
    return os.path.splitext(path)[1]

#�����ļ�
def clear_dir(root_path):

    clear_file_number = 0  #��������ļ�����

    paths = get_all_path(root_path)   #�õ�Ŀ¼�������ļ���Ŀ¼

    for path in paths:
        full_path = os.path.join(root_path,path)   #�õ�������·����
        if os.path.isdir(full_path):   #�����Ŀ¼�ĵݹ�����
            clear_file_number = clear_file_number + clear_dir(full_path)
        else:
            extension = file_extension(full_path)   #������ļ��Ļ���ȡ�ļ���չ��
            if extension in extensions or '.' not in full_path:    #�����Ҫɾ�����ļ������ɾ��
                os.remove(full_path)
                clear_file_number = clear_file_number + 1  #��������ļ�����+1
    return clear_file_number

#���˵�
def menu():
    print_char(20,' ')
    print "�ļ������"    #����
    
    print_char(20,' ')  
    print "����ģʽ"
    
    print_char(15,' ')  #ѡ��
    print "ģʽ1��Ĭ�Ϲ�����ʽ"

    print_char(15, ' ')
    print "ģʽ2���ɼ�������Ҫ������ļ�Ŀ¼"

    print_char(15,' ')
    print "ģʽ3���鿴Ҫ��������ļ�����(Ĭ���ļ���)"

    print_char(15,' ')
    print "ģʽ4���鿴Ҫ��������ļ���������ʾ���ļ�(Ĭ���ļ���)"

    print_char(15,' ')
    print "ѡ��0���˳�"

#Ѱ�ҹ��ж��ٸ���Ҫ��������ļ�
#�ݹ�ʵ�֣��������ļ�����
def find_file_number(root_path, status):

    file_number = 0   #��Ҫ������ļ�����
    
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
            

#������Ҫ�߼�������ļ�������
def run():
    while True:
        menu()
        clear_file_number = 0
        way = raw_input("��ѡ������ʽ")
        if way == '1':
            clear_file_number = clear_dir(default_path)
            print "�ɹ������ļ�"+str(clear_file_number)+"���������ʹ��"
            pause()
        elif way == '2':
            root_path = raw_input("������Ҫ������ļ�Ŀ¼")
            clear_file_number = clear_dir(root_path)
            print "�ɹ������ļ�"+str(clear_file_number)+"���������ʹ��"
            pause()
        elif way == '3':
            file_number = find_file_number(default_path, False)
            print "������"+str(file_number)+"����Ҫ������ļ�"
            pause()
        elif way == '4':
            file_number = find_file_number(default_path, True)
            print "������"+str(file_number)+"����Ҫ������ļ�"
            pause()
        elif way == '0':
            print "��ӭ�´�ʹ��"
            break
        else:
            print "����Ƿ�ָ�����������ָ��"
            pause()
        clear_screen()   #����

#�����Ϊ��������������ʼִ�д���
if __name__ == "__main__":
    run()
