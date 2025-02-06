# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())

import json
import random
import numpy as np
# from sets import Set
import time
import datetime
import random

from collections import defaultdict
from collections import OrderedDict
import math

def convert_to_openai_style(session:dict):
    # 讲character dial转换为openai风格
    # 1。本函数并未构造出system prompt，而是保留了user_name，user_profile，assistan_name，assistant profiled等信息
    # 2、这里只处理了中文对话，想要利用英文对话，需要同样的代码处理session【"language_en]即可