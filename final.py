# -*- coding: utf-8 -*-

from collections import  deque  
import numpy as np  
import cv2  
import time
import mechanize
  
#設定紅色的值  
redLower = np.array([170, 100, 100])  
redUpper = np.array([179, 255, 255])  
#初始化追蹤點的列表  
mybuffer = 128  
pts = deque(maxlen=mybuffer)  
#開啟攝影機  
camera = cv2.VideoCapture(0)  
#等待兩秒  
time.sleep(2)  

def mec():
    #cookie
    cj = mechanize.CookieJar()

    #browser 建立一個browser的物件
    br = mechanize.Browser()

    #options
    #br.set_handle_equiv(True)
    #br.set_handle_gzip(True)
    #br.set_handle_redirect(True)
    #br.set_handle_referer(True)
    br.set_handle_robots(False) #有些網站會禁止機器人瀏覽，忽視它



    #debug 除錯的設定 
    br.set_debug_http(True)
    br.set_debug_redirects(True)
    br.set_debug_responses(True)


    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

    #cookie
    br.set_cookiejar(cj)

    br.open("https://m.facebook.com/")

    br.select_form(nr = 0)

    #抓取表單訊息
    for form in br.forms():
	    print "Form name",form.name
	    print form

    br.form['email'] = "eric40302@gmail.com"
    #br.select_form(name = "pass")
    br.form['pass'] = 'fjjjjj'

    br.submit() 


    #for form in br.forms():
	    #print "Form name",form.name
	    #print form

    #if(logincheck):
    #print logincheck


    br2 = mechanize.Browser()

    #options
    #br2.set_handle_equiv(True)
    #br.set_handle_gzip(True)
    #br2.set_handle_redirect(True)
    #br2.set_handle_referer(True)
    br2.set_handle_robots(False)


    #debugging?
    br2.set_debug_http(True)
    br2.set_debug_redirects(True)
    br2.set_debug_responses(True)

    br2.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

    #cookie
    br2.set_cookiejar(cj)

    r = br2.open("https://m.facebook.com/")

    for form in br2.forms():
	    print "Form name",form.name
	    print form
	
    br2.select_form(nr = 1)
    for control in br2.form.controls:
        print control
        print "type=%s, name=%s, value=%s" %(control.submit, control.waterfall_app_name, control.web_m_touch)
    willy = open('1.jpeg', 'r')
    br2.form.file_uploads.file_name = willy
    #post_message = br.submit()
    #post_check = post_message.read()
    #br2.submit()
    submit_response = br2.submit(name='view_post')    #print br2.response.read()
    #br2.back()

    #result
    #br2_response = br2.response().read()
    #print br2_response
  
while True:  
    #讀取每個「幀」  
    (ret, frame) = camera.read()
    frame = cv2.flip(frame, 1)	
    #判斷是否成功開啟攝影機  
    if not ret:  
        print 'No Camera'  
        break  
    #frame = imutils.resize(frame, width=600)  
    #轉到HSV空間  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    #根據「紅」值構建「膜」  
    mask = cv2.inRange(hsv, redLower, redUpper)  
    #腐蝕操作  
    mask = cv2.erode(mask, None, iterations=2)  
    #膨脹操作，其實先腐蝕再膨脹的效果是開運算，去除噪點  
    mask = cv2.dilate(mask, None, iterations=2)  
    #輪廓檢測  
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  
    #初始化紅點圓形輪廓質心  
    center = None  
    #如果存在輪廓  
    if len(cnts) > 0:  
        #找到面積最大的輪廓  
        c = max(cnts, key = cv2.contourArea)  
        #確定面積最大的輪廓的外接圓  
        ((x, y), radius) = cv2.minEnclosingCircle(c)  
        #計算輪廓的矩  
        M = cv2.moments(c)  
        #計算質心  
        center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))  
        #只有當半徑大於10時，才執行畫圖  
        if radius > 10:  
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)  
            cv2.circle(frame, center, 5, (0, 0, 255), -1)  
            #把質心添加到pts中，並且是添加到列表左側  
            pts.appendleft(center)  
    #搜尋追蹤點，分段畫出軌跡 
    for i in xrange(1, len(pts)):  
        if pts[i - 1] is None or pts[i] is None:  
            continue  
        #計算所畫小線段的粗细  
        thickness = int(np.sqrt(mybuffer / float(i + 1)) * 2.5)  
        #畫出小線段  
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)  
    #res = cv2.bitwise_and(frame, frame, mask=mask)  
    cv2.imshow('Frame', frame)  
    #鍵盤檢測，檢測到esc鍵退出  
    k = cv2.waitKey(5)&0xFF  
    if k == 27:  
        break
    elif k == ord('s'):
        cv2.imwrite('1.jpeg', frame)
        mec()
	
#攝影機釋放  
camera.release()  
#關閉所有視窗  
cv2.destroyAllWindows()  
