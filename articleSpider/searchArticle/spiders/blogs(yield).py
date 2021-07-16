import scrapy


class BlogsSpider(scrapy.Spider):
    name = 'blogs'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    def parse(self, response):

        for news in response.css('div.content'):

            yield {
                'title': news.css('h2.news_entry>a[href]::text').get(),
                'logo': news.css('div.entry_summary>a[href]>img').attrib['src'],
                'published': news.css('span.gray::text').get(),
            }
