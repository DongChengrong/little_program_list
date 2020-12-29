#coding:gbk
'''
�㷨���ҵ�һ��Ŀ¼,�Ѹ�Ŀ¼�µ���Ŀ¼�µ������ļ�ȫ���ƶ�����Ŀ¼��
��һ��������������Ŀ¼
�ڶ������ҵ����е��ļ�
�����������ļ��ƶ���ָ��Ŀ¼��
'''

import os,shutil

def get_all_path(path):
    return os.listdir(path)

def move_file(root_path):
    paths = get_all_path(root_path)
    for path in paths:
        full_path = os.path.join(root_path,path)
        if os.path.isdir(full_path):
            move_file(full_path)
        else:
            shutil.move(full_path, "D:\\ACM-Program\\UVA")

def run():
    root_path = "D:\\ACM-Program\\UVA"
    paths = get_all_path(root_path)
    for path in paths:
        full_path = os.path.join(root_path,path)
        if os.path.isdir(full_path):
            move_file(full_path)
        
if __name__ == "__main__":
    run()
    
