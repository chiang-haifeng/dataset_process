import os

def find_image_file(source_path, file_lst):
    """
    递归寻找 文件夹以及子目录的图片文件。
    :param source_path: 源文件夹路径
    :param file_lst: 输出 文件路径列表
    :return:
    """
    image_ext = ['.jpg', '.JPG', '.PNG', '.png', '.jpeg', '.JPEG', '.bmp']
    for dir_or_file in os.listdir(source_path):
        file_path = os.path.join(source_path, dir_or_file).replace("\\",'/')
        if os.path.isfile(file_path):  # 判断是否为文件
            file_name_ext = os.path.splitext(os.path.basename(file_path))  # 文件名与后缀
            if len(file_name_ext) < 2:
                continue
            if file_name_ext[1] in image_ext:  # 后缀在后缀列表中
                file_lst.append(file_path)
            else:
                continue
        elif os.path.isdir(file_path):  # 如果是个dir，则再次调用此函数，传入当前目录，递归处理。
            find_image_file(file_path, file_lst)
        else:
            print('文件夹没有图片' + os.path.basename(file_path))


if __name__ == '__main__':
    # 1.【输入】todo dir_path为数据集的目录
    dir_path = "D:/ubuntu_shared_folders/CASIA图像处理/Masks"

    # 文件路径 列表 【输出】
    file_path_list = []

    # 2.递归调用
    find_image_file(dir_path, file_path_list)  # 递归查看 文件夹内所有图片

    # 3.写入文件中（txt）todo bri_file_name为只包含文件名的图片路径，此处不需要完整的文件名称

    bri_file_name = os.path.join("D:/workspace/dataset_process", "pro_CASIA-Iris-Thousand.txt").replace("\\",'/')
    print('仅包含文件名的的txt文件为{}'.format(bri_file_name))
    #bri_file为只包含文件名的图片路径
    bri_file = open(bri_file_name, "w")
    #遍历原列表，写入文件
    for item in file_path_list:
        bri_file.write(item.split('/')[-1].split('_')[0] + '.jpg\n')
    print("共计{}张图片被读入".format(len(file_path_list)))
    bri_file.close()