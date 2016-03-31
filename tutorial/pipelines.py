# -*- coding: utf-8 -*-


class ModelPipeLine(object):
    def process_item(self, item, spider):
        print item['title']
        return item
