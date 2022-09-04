# -*- coding: utf-8 -*-
import shutil
from tqdm import tqdm

#file_path 打开的txt文件地址
#img_newfolder 图片存放的新文件夹地址
def copy_img(file_path, img_newfolder):
    # 将txt中的内容写入到列表中
    txt_path_list = []
    for i in open(file_path, 'r'):
        txt_path_list.append(i.replace('\n', ''))
    print('{}张图片开始移动到新的文件夹'.format(len(txt_path_list)))
    # 指定存放图片的目录
    index = 0
    for path in tqdm(txt_path_list):
        shutil.copy(path, img_newfolder)
        index = index + 1
    print('{}张图片成功移动到{}\n'.format(index, img_newfolder))

if __name__ == '__main__':
    # 1.【输入】todo
    file_path = "D:/workspace/dataset_process/CASIA-Iris-Thousand.txt"
    img_newfolder = "D:/workspace/dataset_process/img_dataset"
    # 2.调用函数, 将txt中的图片复制到新的文件夹
    copy_img(file_path, img_newfolder)

