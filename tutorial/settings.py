# -*- coding: utf-8 -*-

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ITEM_PIPELINES = {
   'tutorial.pipelines.ModelPipeLine': 300,
}
