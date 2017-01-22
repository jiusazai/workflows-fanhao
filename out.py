# -*- coding: utf-8 -*-
import sys
import os
from workflow import Workflow

reload(sys)
sys.setdefaultencoding('utf8')


def getargs(wf):
    query = sys.argv[1]
    sys.stdout.write(query)


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(getargs))
