# dataset_process
PicTure Sytem for Iris Recognition  
注：只需要修改每个文件夹中todo部分  
get_All_Images.py 用于获取文件夹中的全部文件,并写入到txt中，其中包含两个txt文件，带有前缀full的是完整路径，不带full的为文件名  
trans_New_Folder.py 用于打开txt文件,并将txt中的图片路径转换到一个新的文件夹，文件夹只包含图片，不存在子文件夹结构
check_by_txt.py 用于打开txt文件，检查经过OSIRISV4.1处理后，失效的图片名称（暂时用处不大）
