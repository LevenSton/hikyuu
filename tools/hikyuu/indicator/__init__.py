#!/usr/bin/python
# -*- coding: utf8 -*-
# cp936
#
# The MIT License (MIT)
#
# Copyright (c) 2017 fasiondog
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from .indicator import *
from .indicator_doc import *
from .talib_wrap import * 


__all__ = [
'Indicator',
'IndicatorImp',
'Operand',
'OP',
'AMA',
'AMO',
'ATR',
'CLOSE',
'CVAL',
'DIFF',
'EMA',
'HHV',
'HIGH',
'KDATA',
'KDATA_PART',
'LLV',
'LOW',
'MA',
'MACD',
'OPEN',
'POS',
'PRICELIST',
'PriceList',
'REF',
'SAFTYLOSS',
'SMA',
'STDEV',
'VIGOR',
'VOL',
'WEAVE',


#----------------------------------------
#talib_wrap
#----------------------------------------

'TA_AD',
'TA_ADOSC',
'TA_ADX',
'TA_ADXR',
'TA_APO',
'TA_AROON',
'TA_AROONOSC',
'TA_ATR',
'TA_AVGPRICE',
'TA_BBANDS',
'TA_BETA',
'TA_BOP',
'TA_CCI',
'TA_CDL2CROWS',
'TA_CDL3BLACKCROWS',
'TA_CDL3INSIDE',
'TA_CDL3LINESTRIKE',
'TA_CDL3OUTSIDE',
'TA_CDL3STARSINSOUTH',
'TA_CDL3WHITESOLDIERS',
'TA_CDLABANDONEDBABY',
'TA_CDLADVANCEBLOCK',
'TA_CDLBELTHOLD',
'TA_CDLBREAKAWAY',
'TA_CDLCLOSINGMARUBOZU',
'TA_CDLCONCEALBABYSWALL',
'TA_CDLCOUNTERATTACK',
'TA_CDLDARKCLOUDCOVER',
'TA_CDLDOJI',
'TA_CDLDOJISTAR',
'TA_CDLDRAGONFLYDOJI',
'TA_CDLENGULFING',
'TA_CDLEVENINGDOJISTAR',
'TA_CDLEVENINGSTAR',
'TA_CDLGAPSIDESIDEWHITE',
'TA_CDLGRAVESTONEDOJI',
'TA_CDLHAMMER',
'TA_CDLHANGINGMAN',
'TA_CDLHARAMI',
'TA_CDLHARAMICROSS',
'TA_CDLHIGHWAVE',
'TA_CDLHIKKAKE',
'TA_CDLHIKKAKEMOD',
'TA_CDLHOMINGPIGEON',
'TA_CDLIDENTICAL3CROWS',
'TA_CDLINNECK',
'TA_CDLINVERTEDHAMMER',
'TA_CDLKICKING',
'TA_CDLKICKINGBYLENGTH',
'TA_CDLLADDERBOTTOM',
'TA_CDLLONGLEGGEDDOJI',
'TA_CDLLONGLINE',
'TA_CDLMARUBOZU',
'TA_CDLMATCHINGLOW',
'TA_CDLMATHOLD',
'TA_CDLMORNINGDOJISTAR',
'TA_CDLMORNINGSTAR',
'TA_CDLONNECK',
'TA_CDLPIERCING',
'TA_CDLRICKSHAWMAN',
'TA_CDLRISEFALL3METHODS',
'TA_CDLSEPARATINGLINES',
'TA_CDLSHOOTINGSTAR',
'TA_CDLSHORTLINE',
'TA_CDLSPINNINGTOP',
'TA_CDLSTALLEDPATTERN',
'TA_CDLSTICKSANDWICH',
'TA_CDLTAKURI',
'TA_CDLTASUKIGAP',
'TA_CDLTHRUSTING',
'TA_CDLTRISTAR',
'TA_CDLUNIQUE3RIVER',
'TA_CDLUPSIDEGAP2CROWS',
'TA_CDLXSIDEGAP3METHODS',
'TA_CMO',
'TA_CORREL',
'TA_DEMA',
'TA_DX',
'TA_EMA',
'TA_HT_DCPERIOD',
'TA_HT_DCPHASE',
'TA_HT_PHASOR',
'TA_HT_SINE',
'TA_HT_TRENDLINE',
'TA_HT_TRENDMODE',
'TA_KAMA',
'TA_LINEARREG',
'TA_LINEARREG_ANGLE',
'TA_LINEARREG_INTERCEPT',
'TA_LINEARREG_SLOPE',
'TA_MA',
'TA_MACD',
'TA_MACDEXT',
'TA_MACDFIX',
'TA_MAMA',
'TA_MAX',
'TA_MAXINDEX',
'TA_MEDPRICE',
'TA_MIDPOINT',
'TA_MIDPRICE',
'TA_MIN',
'TA_MININDEX',
'TA_MINMAX',
'TA_MINMAXINDEX',
'TA_MINUS_DI',
'TA_MINUS_DM',
'TA_MOM',
'TA_NATR',
'TA_OBV',
'TA_PLUS_DI',
'TA_PLUS_DM',
'TA_PPO',
'TA_ROC',
'TA_ROCP',
'TA_ROCR',
'TA_ROCR100',
'TA_RSI',
'TA_SAR',
'TA_SAREXT',
'TA_SMA',
'TA_STDDEV',
'TA_STOCH',
'TA_STOCHF',
'TA_STOCHRSI',
'TA_SUM',
'TA_T3',
'TA_TEMA',
'TA_TRANGE',
'TA_TRIMA',
'TA_TRIX',
'TA_TSF',
'TA_TYPPRICE',
'TA_ULTOSC',
'TA_VAR',
'TA_WCLPRICE',
'TA_WILLR',
'TA_WMA',
]