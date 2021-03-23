# -*- encoding=utf8 -*-
"""
time：2021/3/11

运行：
success.txt文件排序(倒序读取)
小K视频从第一个下载
找到下载后的文件。移动到一个success文件夹
找到video视频的路径修改名字移到一个success文件夹
重复以上操作
"""

import os
import time
import shutil
import pywinauto
from selenium import webdriver
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class upload(object):


    # 下载的路径,这个路径文件里面要为空的
    down_load = r'C:\Users\v_fxfxfang\Downloads'

    # 视频路径
    video = r'C:\Users\v_fxfxfang\Desktop\555\yang借的号22号'

    # 要移动到的文件夹(优秀)
    goal_path = r'C:\Users\v_fxfxfang\Desktop\success'

    # 要移动到的文件夹(中良)
    well_path = r'C:\Users\v_fxfxfang\Desktop\well'

    #txt路径
    txt_path = r'C:\Users\v_fxfxfang\Desktop\success.txt'


    def __init__(self):
        # self.rename_video()
        ##设置接管理管Chrome浏览器
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)


        self.wait = WebDriverWait(self.driver, 100)

    #读取txt文件内容名字(倒序)
    def text_list(self):
        txtList = []
        for line in open(self.txt_path, 'r',encoding='utf-8'):
            txtList.append(line)
        # 去掉列表里面的转行符
        txtList = [' '.join([i.strip() for i in price.strip().split('\t')]) for price in txtList]
        txtList =txtList[::-1]
        self.uploadbtn(txtList)


    # 执行下载
    def uploadbtn(self,txtList):
        #i是遍历后视频名称
        for i in txtList:
            print('--'*20)
            print('i:',i)
            self.driver.refresh()
            time.sleep(2)
            #判断处理效果
            try:
                result = self.driver.find_element_by_xpath('//div[@class="video-list clear"]/div[@class="xk-video-list-item visiable video-list-item"]//div[@class="text"]').text
            except:
                result = self.driver.find_element_by_xpath('//*[@id="xkVideoList"]/div[1]/div[1]/div[1]/div[2]/div/div[1]').text
            print('result:',result)
            if '动作' in str(result):
                source = self.driver.find_element_by_xpath('//*[@id="xkVideoList"]/div/div[1]/div[1]/div[2]/div/div[2]/span[2]/span').text
                print(source)
                if '优' in source:
                    self.down_file()#下载小K
                    self.move_file(i)  ##下载后移动
                if '良' in source:
                    self.down_file()  #下载小K
                    self.move_file(i)  ##下载后移动
                if '中' in source:
                    self.down_file()    #下载小K
                    self.well_file(i)  ##下载后移动
                if '差' in source:
                    self.down_file()    #下载小K
                    self.well_file(i)  ##下载后移动
            if '处理失败' in str(result):
                self.delete_k(i)
                continue

            if '全身' in str(result):
                self.delete_k(i)
                continue
            #网络异常，请稍后重新上传视频删除
            if '上传' in str(result):
                self.delete_k(i)
                continue


    ##下载
    def down_file(self):
        #点击第一个图图准备下载
        self.driver.find_element_by_xpath('//div[@class="item-main"]/div/img').click()
        self.driver.find_element_by_xpath('//div[@class="item-main"]/div/img').click()
        time.sleep(5)
        # 点击下载动作文件（BIP 和 FBX）
        try:
            while True:
                self.driver.find_element_by_xpath('//div[@class="model-footer"]/div[3]/button/span').click()
                # self.driver.find_element_by_xpath('//*[@id="gameContainerBox"]/div[2]/div[3]/button/span').click()
        except:
            ...
        # 点击下载动作文件（BIP 和 FBX）
        try:
            while True:
                self.driver.find_element_by_xpath('//*[@id="gameContainerBox"]/div[2]/div[3]/button/span').click()
                # self.driver.find_element_by_xpath('//*[@id="gameContainerBox"]/div[2]/div[3]/button/span').click()
        except:
            ...


        time.sleep(2)
        #点击下载动作文件
        # self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/button/span').click()
        try:
            while True:
                self.driver.find_element_by_xpath('//div[@class="pay-footer"]/button/span').click()
        except:
            ...


        time.sleep(22)


    ##删除处理失败的
    def delete_k(self,i):
        #点击垃圾桶
        self.driver.find_element_by_xpath('//div[@class="video-list clear"]/div[1]/div[2]/div/i[1]').click()
        time.sleep(2)
        try:
            while True:
                self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]/span').click()
        except:
            ...
        self.delete_video(i)
        time.sleep(2)

    ##移动到优
    def move_file(self,name):
        #name是遍历后视频名称
        print('name:',name)
        b = os.listdir(self.down_load)
        for zip_name in b:
            if 'zip' in zip_name:
                # 视频命名文件的前缀
                front_name = name.split('.')[0]
                # 下载小K的绝对路径
                # C:\Users\v_fxfxfang\Downloads\37363_action_202103161632.zip
                down_path = os.path.join(self.down_load, zip_name)
                print(down_path)

                # 视频绝对路径
                # C:\Users\v_fxfxfang\Desktop\success\2.mp4
                video_path = os.path.join(self.video, name)

                #视频和zip文件移到到目的文件
                try:
                    shutil.move(video_path, self.goal_path)
                    shutil.move(down_path, self.goal_path)
                except:
                    print('移动失败。没有这个视频')

                #修改名字，zip文件的名字改成和视频名字一样
                src = os.path.join(os.path.abspath(self.goal_path), zip_name)
                dst = os.path.join(os.path.abspath(self.goal_path), '%s.zip' % front_name)

                try:
                    os.rename(src, dst)

                except:
                    print('修改失败')

    ##移动到中良
    def well_file(self,name):
        #name是遍历后视频名称
        print('name:',name)
        b = os.listdir(self.down_load)
        for zip_name in b:
            if 'zip' in zip_name:
                # 视频命名文件的前缀
                front_name = name.split('.')[0]
                # 下载小K的绝对路径
                # C:\Users\v_fxfxfang\Downloads\37363_action_202103161632.zip
                down_path = os.path.join(self.down_load, zip_name)
                print(down_path)

                # 视频绝对路径
                # C:\Users\v_fxfxfang\Desktop\success\2.mp4
                video_path = os.path.join(self.video, name)

                #视频和zip文件移到到目的文件
                try:
                    shutil.move(video_path, self.well_path)
                    shutil.move(down_path, self.well_path)
                except:
                    print('移动失败。没有这个视频')
                    self.delete_zip(zip_name)

                #修改名字，zip文件的名字改成和视频名字一样
                src = os.path.join(os.path.abspath(self.well_path), zip_name)
                dst = os.path.join(os.path.abspath(self.well_path), '%s.zip' % front_name)

                try:
                    os.rename(src, dst)

                except:
                    print('修改失败')
    #删除处理失败的视频
    def delete_video(self,i):
        video_path = os.path.join(self.video,i)
        try:
            os.remove(video_path)
            print('%s视频处理无效果已删除' % i )
        except:
            print('视频删除失败')

    #如果移动失败就要删除zip下载后的文件
    def delete_zip(self,zip_name):
        video_path = os.path.join(self.down_load, zip_name)
        try:
            os.remove(video_path)
            print('%s文件处理无效果已删除' % zip_name)
        except:
            print('文件删除失败')



if __name__ == '__main__':

    pq = upload()
    pq.text_list()

