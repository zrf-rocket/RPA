import rpa as r
# 鼠标自动化
r.init(chrome_browser=True, visual_automation=True)


##### 计算机软件操作
r.click(12, 34) # left-click on element
r.rclick() # right-click on element
r.dclick() # double-click on element
r.hover() # move mouse to element
# 上面的函数可以传递x，y（坐标轴位置）或者 element_identifier
# element_identifier有三种，分别用于不同的情况：
# ①在Chrome操作模式中，element_identifier就是爬虫中的选择器，这篇咱们就不说了。
# ②他可以是一个软件组件的图片。简单来说就是按键精灵中的模式匹配，从屏幕中找到你给他的图片，然后他帮你点这个图片的位置的中心。
# ③他可以是一个软件窗口的图片。用在snap和read里面，用于指定截图的范围，咱们后面讲到这两个函数再细说。



# 使用鼠标打开右键 打开文件
r.click('TEMP/window_max_bt.png')
r.hover('TEMP/aim_pic_name.png')
r.rclick('TEMP/aim_pic_name.png')
r.click('TEMP/r_key_open_ways.png')
r.click('TEMP/r_key_open_ways_org_pic.png')

r.close()