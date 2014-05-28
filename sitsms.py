#!/usr/bin/python
import mechanize
import cookielib
import sys
import os
from pytesser import *

br=mechanize.Browser()
br.set_handle_robots(False)
cj=cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/16.0.1-1.fc9 Firefox/17=18.0.1')]

def gettxt():
    print "enter your message $ to end"
    txt=""
    while True:
        line=raw_input()
        if "$" in line:
            break
        else:
            txt+=line+'\n'
    return txt

def loginsite():
    #opening a pass.txt file for the username and password
    try:
        str=''
        f=open('pass.txt')
        for line in f.readlines():
            str+=line;
        uname=str.split()[0]
        pword=str.split()[1]
    except:
        print 'info file not found'
        sys.exit()
    
    #login to site2sms
    url='http://www.site2sms.com/mainpage.asp'
    br.open(url)
    br.select_form('login')
    br.form['username']=uname
    br.form['Password']=pword
    br.submit()
    if 'verification.asp' in br.geturl():
        gen_captcha()
        br.select_form('frmVerify')
        br.form['txtCaptchaCode']=captcha_val()
        br.submit()
        if 'dashboard.asp' in br.geturl():
           print '>>> login successfull'
	else:
	    loginsite()
    else:
        print 'try again'
        sys.exit()
    br.open('http://www.site2sms.com/user/send_sms.asp')

def sendsms(mno,txt):
    print 'length of msg is '+str(len(txt))
    br.open('http://www.site2sms.com/user/send_sms_text.asp')
    print '>>> sending..'
    #print 'youre in :'+br.geturl()
    br.select_form('SendSms')
    br.form['txtMobileNo']=mno
    br.form['txtMessage']=txt
    br.submit()
    #print 'youre in :'+br.geturl()
    br.select_form('frm_confirm')
    br.submit()
    #print 'youre in :'+br.geturl()
    print '>>> sent..'

def groupsms(book,txt):
    print 'sending group txt'
    loginsite()
    f=open(book)
    for line in f.readlines():
        mno=line.split()[1]
        print 'sending to : '+line.split()[0]
        sendsms(mno,txt)
    print 'done'

def gen_captcha():
    print 'solving captcha... pls wait'
    url='http://www.site2sms.com/security/captcha.asp'
    br.open(url)
    with open("captcha.bmp","wb") as file:
         file.write(br.open_novisit(url).read())  
    br.back()

def captcha_val():
    image = Image.open('captcha.bmp')
    val = image_to_string(image)[0:3]
    print "captcha value "+val
    return val

def logoutsite():
    br.open('http://www.site2sms.com/user/logout.asp')
    print 'logout successfully'
    sys.exit()

def main():
    if len(sys.argv[:])==2 and '.txt' in sys.argv[1]:
        msg=gettxt()
        groupsms(sys.argv[1],msg)
        logoutsite()
    if len(sys.argv[:])==2:
        msg=gettxt()
        loginsite()
        sendsms(sys.argv[1],msg)
        logoutsite()
    if '.txt' in sys.argv[1]:
        groupsms(sys.argv[1],sys.argv[2])
        logoutsite()
    if len(sys.argv[:])==3 and '.txt' in sys.argv[1]:
        groupsms(sys.argv[1],sys.argv[2])
        logoutsite()
    if len(sys.argv[:])==3:
        loginsite()
        sendsms(sys.argv[1],sys.argv[2])
        logoutsite()

if __name__=='__main__':
    main()
