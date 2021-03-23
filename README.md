## 简介
----
这个下载是结合[小k上传](https://github.com/fangxianshenga/msall_k/tree/master)后生成的success.txt下载的。

## 主要功能
--------------------
-  下载优良中差文件，删除处理失败的视频。
-   下载后文件和视频根据处理效果自动分类(优良，中差各一类)

## 运行环境
--------------------
- windows
- python3

## 第三方库
--------------------
- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令
pip install -r requirements.txt
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

## 使用教程
--------------------

1. 安装谷歌浏览器及谷歌驱动，两者版本要一致(这里给的是87.0.4280.88版本的)，谷歌不是这个版本的需要自行下载对应版本[驱动](http://npm.taobao.org/mirrors/chromedriver/) 把安装的谷歌目录添加到环境变量中(path)。

2. 把chromdriver分别添加到浏览器的安装目录，python安装目录Scripts文件夹中,重启电脑。


3. 打开命令提示符(菜单+R,输入cmd即可打开)，在命令运行中输入以下命令会弹出谷歌浏览器界面：
```python
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
```
4. 在新弹出谷歌浏览器框里打开小k网址，并扫描登入。
5. success.txt文件必须是按成功上传视频名称的顺序。否则会跟下载的文件不匹配。

 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210323181023610.png)
6. 谷歌下载的文件夹里面要清空。
7.程序里面的路径根据自己的情况修改。
8.直接运行即可。

