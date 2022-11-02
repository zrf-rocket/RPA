import rpa as r
r.init(chrome_browser=True, visual_automation=True)




##### 识别图片并点击
# r.snap()

# OCR
# ocr主要是使用read函数
r.url('https://www.baidu.com')
r.type('//*[@id="kw"]', '新冠肺炎[enter]')
r.wait(1)
r.snap('page', 'TEMP/results.png')
print(r.read('//*[@id="1"]/div/div[2]/a/div[2]'))




r.close()