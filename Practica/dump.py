import schedule
import time
import threading
import rrdtool
import os
from pysnmp.hlapi import *
from copy import copy
rrdtool.dump('1.rrd','1DB.xml')
rrdtool.dump('2.rrd','2DB.xml')