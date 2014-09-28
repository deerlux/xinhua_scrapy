# -*- coding: utf-8 -*-

# Scrapy settings for xinhua_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'xinhua_scrapy'

SPIDER_MODULES = ['xinhua_scrapy.spiders']
NEWSPIDER_MODULE = 'xinhua_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xinhua_scrapy (+http://www.yourdomain.com)'
# ITEM_PIPELINES=['xinhua_scrapy.pipelines.XinhuaScrapyPipeline']

KEYWORDS=[u'美军',u'演习']

# LOG_LEVEL='INFO'

