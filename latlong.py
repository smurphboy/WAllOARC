# -*- coding: utf-8 -*-
#maiden head to lon/lat
import os
import sys


__MH__ = 'IO81ql'

def GetLon(ONE, THREE, FIVE):
    StrStartLon = ''
    StrEndLon = ''

    Field = ((ord(ONE.lower()) - 97) * 20) 
    Square = int(THREE) * 2
    SubSquareLow = (ord(FIVE.lower()) - 97) * (2/24)
    SubSquareHigh = SubSquareLow + (2/24)

    StrStartLon = str(Field + Square + SubSquareLow - 180 )
    StrEndLon = str(Field + Square + SubSquareHigh - 180 )

    return StrStartLon, StrEndLon

def GetLat(TWO, FOUR, SIX):
    StrStartLat = ''
    StrEndLat = ''

    Field = ((ord(TWO.lower()) - 97) * 10) 
    Square = int(FOUR)
    SubSquareLow = (ord(SIX.lower()) - 97) * (1/24)
    SubSquareHigh = SubSquareLow + (1/24)

    StrStartLat = str(Field + Square + SubSquareLow - 90)
    StrEndLat = str(Field + Square + SubSquareHigh - 90)    

    return StrStartLat, StrEndLat

def main(strMaidenHead = __MH__):
    if len(strMaidenHead) < 6: strMaidenHead = __MH__

    ONE = strMaidenHead[0:1]
    TWO = strMaidenHead[1:2]
    THREE = strMaidenHead[2:3]
    FOUR = strMaidenHead[3:4]
    FIVE = strMaidenHead[4:5]
    SIX = strMaidenHead[5:6]

    (strStartLon, strEndLon) = GetLon(ONE, THREE, FIVE)
    (strStartLat, strEndLat) = GetLat(TWO, FOUR, SIX)

    print ('Start Lon = ' + strStartLon)
    print ('End   Lon = ' + strEndLon)
    print ()
    print ('Start Lat = ' + strStartLat)
    print ('End   Lat = ' + strEndLat)

    return strStartLon, strEndLon, strStartLat, strEndLat

if __name__ == '__main__':
    main ()