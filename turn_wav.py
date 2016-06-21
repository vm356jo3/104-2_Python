#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymedia.audio.acodec as acodec#編碼器
import pymedia.muxer as muxer#合成器
import wave#為了能夠寫wav檔
import string#字串

name= '01. Driving Sound #1.mp3'#你的檔案
name1= str.split( name, '.' )#讀取附檔名
name2= string.join( name1[ : len( name1 )- 1 ] )#讀取檔案名稱
dm= muxer.Demuxer( 'mp3' )#分解中，此部分是為了得知檔案資訊
snd= dec= None#先指定變數，之後用來解碼用
f= open( name, 'rb' ) #開檔案
s= ' '#先指定空的變數

print u'轉換成wav格式中...'
while len( s ):#當檔案還有後續時：
	s= f.read( 20000 )#讀取前20,000個bit
	if len( s ):#若檔案還有後續時：
		frames= dm.parse( s )#解析檔案
		for fr in frames:#解析檔案中...
		
			if dec== None:#若「無碼」的話：
				dec= acodec.Decoder( dm.streams[ 0 ] )#那就開啟解碼器！
			r= dec.decode( fr[ 1 ] )#解碼
			
			if r and r.data:#若解碼成功的話：
				if snd== None:#若還沒有任何檔案被寫入的話：
					snd= wave.open( name2+ '.wav', 'wb' )#開新檔案
					snd.setparams( (r.channels, 2, r.sample_rate, 0, 'NONE','') )#設定參數

				snd.writeframes( r.data )#將資料寫進去！

print u'轉檔成功！'
print u'採樣頻率：',
print r.sample_rate#印出採樣頻率
print u'聲道數量：',
print r.channels#印出聲道數量