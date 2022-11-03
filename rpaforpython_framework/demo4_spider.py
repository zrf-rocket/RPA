import rpa as r
r.init()
# 获取豆瓣最新电影排行
r.url('https://movie.douban.com/')
r.click('//*[@id="db-nav-movie"]/div[2]/div/ul/li[4]/a')
r.wait(1)
print(r.read('//*[@id="content"]/div/div[1]/div/div'))
r.click('//*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a')


# 网络自动化
# r.init()
# r.url('https://www.baidu.com')
# r.type('//*[@name="q"]', 'decentralisation[enter]')
# print(r.read('result-stats'))
# r.snap('page', 'results.png')



r.close()


