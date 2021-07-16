step1: scrapy startproject searchArticle .
step2: cd searchArticle
step3: scrapy genspider blogs news.cnblogs.com
step4: scrapy shell "http://news.cnblogs.com/"
step5: get 1 item that includes title, date url
news = response.css('div.content')
title = all_news.css('h2.news_entry>a[href]::text').get()
img = all_news.css('div.entry_summary>a[href]>img').attrib['src']
date = all_news.css('span.gray::text').get()
step6: scrapy crawl blogs
step7: scrapy crawl blogs -o blogs.json
