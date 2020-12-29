#coding:gbk
'''
算法：找到一个目录,把该目录下的子目录下的所有文件全部移动到该目录下
第一步：遍历所有子目录
第二步：找到所有的文件
第三步：将文件移动到指定目录下
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
    
