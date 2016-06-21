#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymedia.audio.acodec as acodec#編碼器
import pymedia.audio.sound as sound#發聲器
import pymedia.muxer as muxer#合成器
import time#時間

name = 'ringtone_john.mp3'#你的檔案
dm = muxer.Demuxer( str.split( name, '.' )[ -1 ].lower( ) )#分解中，此部分是為了得知檔案資訊
snd = dec = None#先指定變數，之後用來發聲，解碼用
f = open( name, 'rb' )#開檔案
s = f.read( 32000 )#讀取前32,000個bit

print u'現正播放的是：',
print name
while len( s ):#當檔案還有後續時：
    frames = dm.parse( s )#解析檔案
    if frames:#若有解析檔案的話：
        for fr in frames:#解析檔案中...
		
            if dec == None:#若「無碼」的話：
                dec = acodec.Decoder( dm.streams[ fr[ 0 ] ] )#那就開啟解碼器！
            r = dec.decode( fr[ 1 ] )#解碼
			
            if r and r.data:#若解碼成功的話：
                if snd == None:#若「無聲」的話：
                    snd = sound.Output(
                        int( r.sample_rate ),
                        r.channels,
                        sound.AFMT_S16_LE )#那就大聲講出來！
                data = r.data#將檔案資料指定到資料
                snd.play( data )#就播放資料
				
    s = f.read( 512 )#讀檔

while snd.isPlaying( ):
	time.sleep( .05 )#播放完畢，休息0.5秒鐘