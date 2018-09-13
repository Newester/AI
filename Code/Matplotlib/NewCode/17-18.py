#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import urllib
import numpy as np
from matplotlib import style

import matplotlib.dates as mdates

style.use('fivethirtyeight')
print(plt.style.available)
print(plt.__file__)

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    plt.title(stock)
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                               delimiter=',',
                                                               unpack=True,
                                                               converters={0:bytespdate2num('%Y-%m-%d')})
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x = x + 1

    #candlestick_ohlc(ax2, ohlc, witdth=0.4, colorup='#77d879', colordown='#db3f3f')
    ax2.plot(date, closep)
    ax2.plot(date, openp)
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.grid(True)

    bbox_props = dict(boxstyle='round',fc='w',ec='k',lw=1)
    ax2.annotate(str(closep[-1]),(date[-1],closep[-1]),xytext = (date[-1] + 3, closep[-1]), bbox = bbox_props)


    font_dict = {'family':'serif',
                 'color':'darkred',
                 'size':15}
    ax2.text(date[10], closep[1], 'Text Example', fontdict=font_dict)

    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')
