# -*- coding: utf-8 -*-

# Scrapy settings for doubanCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanCrawler'

SPIDER_MODULES = ['doubanCrawler.spiders']
NEWSPIDER_MODULE = 'doubanCrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'movie.douban.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive',
    'Cookie': 'bid=gWfevcB00KE; douban-fav-remind=1; __utma=30149280.91499174.1536068311.1545479099.1545569777.6; __utmz=30149280.1545479099.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108288"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1545569775%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DXBw2hgN3xsIojirPVue3B9CBNS_xWya26tT6Cg9qsx8t5P18IRLNNPuMTrHCV9obqUxlyUzihwvgiwyu5-YVwm-SVWi4bOiLbgT4QVY0B4W%26wd%3D%26eqid%3Dd3eab88000059347000000025c1e23b4%22%5D; _pk_id.100001.4cf6=03d2243e3f70f954.1536065998.5.1545571343.1545479117.; __utma=223695111.1599520972.1536065999.1545479099.1545569777.5; __utmz=223695111.1545479099.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=N7JhhrwU7fV3E9dDhGGFoq0m31crqS6S; _vwo_uuid_v2=D1E947D246FD8C1C2BB51FB2018EFCBB6|ba690534b70ab964e411c6d4a4b390d3; viewed="3112503"; gr_user_id=de63f43e-1d20-4733-afe8-4d78d11fe296; ap_v=0,6.0; __utmc=30149280; __utmc=223695111',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubanCrawler.middlewares.DoubancrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doubanCrawler.middlewares.DoubancrawlerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'doubanCrawler.pipelines.DoubancrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
