# -*- coding: utf-8 -*-

import re
import urllib
from sgmllib import SGMLParser
from workflow import Workflow, ICON_WEB, web
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class MySGMLParser(SGMLParser):
    # 重写SGMLParser模块中的reset函数，
    def reset(self):
        # 调用原来的函数resert
        SGMLParser.reset(self)
        # 数据存放的位置
        self.is_h3 = ""
        self.lable = False
        self.url = []
        self.title = []

        # 查找的标签(start_ +　标签）表示查找的那个标签（参数是固定的）

    def start_a(self, attrs):
        # 查找对象的标签里面的属性(此处用到了列表解析)
        href = [v for k, v in attrs if k == 'href']
        # 判断href是不是存在
        if href:
            self.url.extend(href)
        self.lable = True


        # 查找结束的标志

    def end_a(self):
        self.lable = False
        # 处理信息数据的地方

    def handle_data(self, data):
        # 判断标签数不超找完毕
        if self.lable:
            data = data.strip()
            self.data.append(data)

    def start_h3(self, attrs):
        self.is_h3 = 1

    def end_h3(self):
        self.is_h3 = ""

    def handle_data(self, data):
        if self.is_h3 == 1:
            self.title.append(data)

class ParserData():
    def __init__(self, urlpath):
        self.urlpath = urlpath
        self.dealData()

    def readData(self):
        data = None
        # 访问的地址是不是存在,不存在侧抛出异常
        try:
            data = urllib.urlopen(self.urlpath)
        except IOError, e:
            print u'地址不存在'
        return data


        # 处理数据

    def dealData(self):
        # 对上述的类实例化
        parser = MySGMLParser()
        # 获取访问url的对象
        data = self.readData()
        if data != None:
            #   调用定义在 SGMLParser 中的 feed 方法，将 HTML 内容放入分析器中(feed传值为字符串)
            parser.feed(data.read())
            self.closeData(data, parser, )
            # 遍历查找的数据
            k=0
            for i in parser.url:
                if i.startswith('thunder'):
                    wf.add_item(title=unicode(parser.title[k], 'utf-8'),subtitle=i,arg=i,valid=True)
                    k+=1

            # for i in xrange(len(parser.title)):
            #         wf.add_item(title=unicode(parser.title[i], 'utf-8'),subtitle=,valid=True)

    def closeData(self, data, parser):
        parser.close()
        data.close()


def main(wf):
    query = wf.args[0].strip().replace("\\", "")
    url = 'http://102436.com/cili/'+query+'.html'
    data=ParserData(url)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()

    sys.exit(wf.run(main))

