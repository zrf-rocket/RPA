
# 获取豆瓣最新电影排行
r.url('https://movie.douban.com/')
r.click('//*[@id="db-nav-movie"]/div[2]/div/ul/li[4]/a')
r.wait(1)
print(r.read('//*[@id="content"]/div/div[1]/div/div'))
r.click('//*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a')




