import scrapy


class EmojiSpider(scrapy.Spider):
    name = 'emoji'
    start_urls = ['https://www.fabiaoqing.com/bqb/lists/type/hot/page/1.html']

    def parse(self, response, **kwargs):
        print('+++++++++++++++++++++++++++++++++++++++++++++')
        print('第{}页：'.format(response.url.split('/')[-1].split('.')[0]),response.url)

        # extract title of emoji
        for info in response.css('div.bqppdiv img::attr(alt)'):
            print(info.get())

        # get the url of next page
        next_page = response.css('div[id="mobilepages"] a.item::attr(href)').get()
        next_page = response.urljoin(next_page)

        # move to next parse
        yield scrapy.Request(next_page,callback=self.parse_third_page)

    def parse_third_page(self,response, **kwargs):
        print('+++++++++++++++++++++++++++++++++++++++++++++')
        # print the current page number
        print('第{}页：'.format(response.url.split('/')[-1].split('.')[0]),response.url)

        for info in response.css('div.bqppdiv img::attr(alt)'):
            print(info.get())

        next_page = response.css('div[id="mobilepages"] a.item::attr(href)')[1].get()   # only here changed:add [1]; since the position is different between page1 and page2
        next_page = response.urljoin(next_page)

        yield scrapy.Request(next_page,callback=self.parse_third_page)