# -*- coding: utf-8 -*-

# @Time    : 2020/3/7 18:43
# @Author  : focksor
# @Email   : focksor@outlook.com
import os
from hdfs import Client, InsecureClient

if __name__ == '__main__':
    hdfs_ip = "192.168.146.133"
    hdfs_version = 3
    hdfs_root = "~/test"
    filepath = r"C:\Users\daqige\PycharmProjects\newLeetCode\convert.py"
    hdfs_addr = "http://" + hdfs_ip + ":" + str(9870 if
                                                (hdfs_version == 3) else 90070)

    client = Client(hdfs_addr)

    # print("创建文件夹")
    # client.makedirs(hdfs_root)
    # print(client.list("/"))
    #
    # print("上传文件")
    # client.upload(hdfs_root, filepath)
    # print(client.list(hdfs_root))
    #
    # print("修改文件名")
    # client.rename(hdfs_root + "/convert.py", hdfs_root + "/ubuntu.py")
    # print(client.list(hdfs_root))

    print("下载文件")
    client.download(hdfs_root + "/ubuntu.py", ".")
    print(os.listdir("."))

    print("删除文件")
    client.delete(hdfs_root + "/ubuntu.py")
    print(client.list(hdfs_root))
