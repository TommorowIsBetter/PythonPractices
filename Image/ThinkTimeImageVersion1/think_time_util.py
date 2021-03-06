#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/7/27 20:23
"""

import os
import re
import shutil
import cv2

# 这里只需要把原始图片放到A_Pictures_Raw文件夹下即可，然后运行程序会把相应的处理后的图片放到New文件夹下
dir_New = "./A_Pictures_New/"
dir_raw = "./A_Pictures_Raw/"
# 为了实现把文件A_Pictures_Raw的图片重命名，命名要求是前一张图片的名字对应后一张的图片名字
# 注意这里enumerate的遍历顺序不是按照顺序，所以要确认命名的顺序正确。
def rename_picture_by_time_cv2():
    if not os.path.exists(dir_New):
        os.makedirs(dir_New)
    filename_list = os.listdir(dir_raw)
    for index, file_name in enumerate(filename_list):
        if index < len(filename_list) - 1:
            img = cv2.imread(dir_raw + file_name)
            cv2.imwrite(dir_New + filename_list[index + 1], img)


# 根据时间值，给正确的图片进行分类，然后分别存储到不同的文件夹
def classify_picture_by_time():
    # 按照停留时间1-4s为kind_0, 4-8s为kind_1, 8-12s为kind_2
    classes = [3, 8, 13]
    filename_list = os.listdir(dir_New)
    for file_name in filename_list:
        if file_name.endswith(".png"):
            # 目标是取出停留时间这个具体的数字
            index = file_name.split("_")[1]
            index = int(index)
            if index < 10:
                hover_time = re.findall("(?<=\d{14}_\d_).*?(?=\.png)", file_name)[0]
            elif 10 <= index < 100:
                hover_time = re.findall("(?<=\d{14}_\d{2}_).*?(?=\.png)", file_name)[0]
            elif 100 <= index < 1000:
                hover_time = re.findall("(?<=\d{14}_\d{3}_).*?(?=\.png)", file_name)[0]
            elif 1000 <= index < 10000:
                hover_time = re.findall("(?<=\d{14}_\d{4}_).*?(?=\.png)", file_name)[0]
            elif 10000 <= index < 100000:
                hover_time = re.findall("(?<=\d{14}_\d{5}_).*?(?=\.png)", file_name)[0]
            hover_time = round(float(hover_time))
            if hover_time < classes[0]:
                # 目标是获取类似20190727080550_6_19.928这个子字符串
                pre_name = re.findall(".*?(?=\.png)", file_name)[0]
                new_name = pre_name + "_" + "0" + ".png"
                os.rename(dir_New + file_name, dir_New + new_name)
                dir = dir_New + "kind_" + "1" + "-" + str(classes[0]) + "_0/"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                shutil.move(dir_New + new_name, dir)
            elif classes[0] <= hover_time < classes[1]:
                # 目标是获取类似20190727080550_6_19.928这个子字符串
                pre_name = re.findall(".*?(?=\.png)", file_name)[0]
                new_name = pre_name + "_" + "1" + ".png"
                os.rename(dir_New + file_name, dir_New + new_name)
                dir = dir_New + "kind_ " + str(classes[0]) + "-" + str(classes[1]) + "_1/"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                shutil.move(dir_New + new_name, dir)
            elif classes[1] <= hover_time < classes[2]:
                # 目标是获取类似20190727080550_6_19.928这个子字符串
                pre_name = re.findall(".*?(?=\.png)", file_name)[0]
                new_name = pre_name + "_" + "2" + ".png"
                os.rename(dir_New + file_name, dir_New + new_name)
                dir = dir_New + "kind_" + str(classes[1]) + "-" + str(classes[2]) + "_2/"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                shutil.move(dir_New + new_name, dir)
            elif classes[2] <= hover_time:
                # 目标是获取类似20190727080550_6_19.928这个子字符串
                pre_name = re.findall(".*?(?=\.png)", file_name)[0]
                new_name = pre_name + "_" + "3" + ".png"
                os.rename(dir_New + file_name, dir_New + new_name)
                dir = dir_New + "kind_" + str(classes[2]) + "-_3/"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                shutil.move(dir_New + new_name, dir)
            print("hoverTime:" + str(hover_time))


if __name__ == '__main__':
    rename_picture_by_time_cv2()
    classify_picture_by_time()
