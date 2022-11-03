import rpa as r

# 用到系统操作我们需要把r.init(visual_automation = True)这个参数设置为True。
# visual_automation = True表示动画可见。
# 需要注意的是本地操作需要安装JAVA，我是根据他提示的错误代码安装了Amazon Corretto这个版本的JAVA。
r.init(chrome_browser=False, visual_automation=True)

##### 网页操作
r.url('https://www.baidu.com/')
r.type('//*[@id="kw"]', '淘宝[enter]')
# 用法1
# 参数1：xpath表示输入的网页xpath，参数2：words表示输入的是什么内容。
# xpath获取方式,谷歌浏览器按F12，然后在想要查看位置右键检查：

# 用法2
# r.type('message_box.png', 'Hi Gillian,[enter]This is...')这个该网页或者图的某一部位的图，它会在该网页（或其他）找到message_box.png图所指示的位置，在该位置输入数据。其中[enter]表示按下Enter按键。

read_res = r.read('result-stats')
print(read_res)
# r.read(DOM/XPath/Region/Image)
# **注:DOM 和 XPath 标识符仅适用于 Chrome/Edge。要自动化其他浏览器，请使用点/区域和图像标识符。**
# # DOM
# 这匹配网页的 DOM（文档对象模型）中的元素，匹配id、名称、类属性或元素本身的文本。
# `click Getting started`
#
# # XPath
# 这与网页中元素的XPath匹配。这是一种更明确、更强大的定位 Web 元素的方式。
# **注：您也可以使用 CSS 选择器代替 XPath，但首选 XPath。**
# `click //body/div[1]/nav/div/div[1]/a`
#
# # Point
# 点击屏幕中的点。
# `click (200,500)`
# 这与屏幕上距屏幕左侧 200 像素和距屏幕顶部 500 像素的点相匹配。
#
# # Region
# 某个区域。
# `read (300,400)-(500,550) to some-variable`
# 这与两点 (300,400) 和 (500,550) 之间形成的矩形相匹配。
#
# # Image
# 点击某个图片，实际上是利用图形识别完成。
# `click button.png`
# 这匹配屏幕上看起来类似于图像文件的任何区域button.png（在流程的文件夹中）。您首先需要截取button.png. 这使用了视觉自动化。
# `click image/button.png`
# 这允许您button.png在image文件夹中查找。

# 这里可以通过OCR读取图片中的文字，例如:
# print(r.read('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]'))
# print(r.read('pdf_window.png'))


r.snap('page', "results.png")
# r.snap( DOM/XPath/Region/Image/page, filename)
# 这个表示截图，前面表示从哪里截图，后面表示保存的路径和文件名。例如:
# r.snap('page', 'TEMP/results.png')
# 支持的按键如下：
# [shift] [ctrl] [alt] [win] [cmd] [enter]
# [space] [tab] [esc] [backspace] [delete] [clear]
# [up] [down] [left] [right] [pageup] [pagedown]
# [home] [end] [insert] [f1] .. [f15]
# [printscreen] [scrolllock] [pause] [capslock] [numlock]


# 网页搜索采集数据


# 点击特定元素


# 使用滚轮
# r.vision('wheel(WHEEL_UP, 120)')


r.close()
