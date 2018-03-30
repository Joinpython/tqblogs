
# 时光网
import scrapy
import re


class MtimeSpider(scrapy.Spider):
    name = 'movies_mtime_spider'
    allowed_domains = ['mtime.com']
    start_urls = ['http://service.mtime.com/Service/Movie.msi?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Service.Pages.MovieService&Ajax_CallBackMethod=GetRatingsByMovieIds&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fwww.mtime.com%2Ftop%2Fmovie%2Fhot_top10%2F&t=20183182321615226&Ajax_CallBackArgument0=218085%7C108482%7C240425%7C236214%7C234873%7C228764']

    def parse(self, response):
        data = response.text

        ids = re.findall(r'.*?{"movieId":(.*?),.*?',str(data), re.S)

        print(ids)

        for id in ids:
            url = 'http://movie.mtime.com/'+str(id)
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        # print(response.text)

        titles = response.xpath('//*[@id="db_head"]/div[2]/div/div[1]/h1/text()').extract()
        abstracts = response.xpath('//*[@id="movie_warp"]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dt/p[1]/text()').extract()

        print(titles)
        print(abstracts)


