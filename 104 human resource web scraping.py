
# coding: utf-8

# In[2]:

import requests
import time
from bs4 import BeautifulSoup as bs
for i in range(1,36):               # 台北市中正區、資訊軟體系統類、全部工作 共35頁
    nextpage='http://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=0&jobcat=2007000000&area=6001001001&order=2&asc=0&page={}&psl=N_A'.format(i)
    #print nextpage                 #nextpage 網址內容
    res=requests.get(nextpage)
    soup = bs(res.text)
    domain='http://www.104.com.tw/'
    for li in soup.select('.j_cont'):
        print li.select('.jobname_summary span')[0].text,li.select('.requirement')[0].text,li.select('.compname_summary span')[0].text
        print domain+li.select('.jobname_summary a')[0]['href']
    time.sleep(3)


# In[1]:


import requests as rs
from bs4 import BeautifulSoup as bs
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

filename = 'HR1111/HR_1111_SE.txt'  # 1111人力銀行 軟體工程
f = open(filename, 'w')

address = 'http://www.1111.com.tw/mobileWeb/job-index.asp?role=1%2C2%2C4%2C16&keys=&c0Cht=&c0='           '&d0Cht=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B&d0=140200&t0Cht=&t0=&gr=&ex=&wk=&si=1&page={}'

for page in range(1, 114):  # 換頁迴圈 共 4490 筆
    address_format = address.format(page)
    res = rs.get(address_format)
    # print res.encoding - 'utf-8'
    soup = bs(res.text)
    jobList = soup.select('.jobList li')
    for li in jobList:  # 職缺列表迴圈
        jobTitle = ''.join(li.select('.list_content p')[0].text.encode('utf-8').split('\t'))
        # 職稱
        company = li.select('.black')[0].text.encode('utf-8')
        # 公司名稱
        postDate = li.select('.gray')[1].text.encode('utf-8')[15:]
        # 公告日期

        jobDetail_address = 'http:' + li.select('a')[0]['href'].encode('utf-8')
        # 職缺網址
        res2 = rs.get(jobDetail_address)
        soup2 = bs(res2.text, 'html.parser')
        companyDescription = soup2.select('#companyDescription')
        jobContent = soup2.select('#jobcontent')
        dic = {'工作性質：': '', '工作內容：': '', '工作經驗：': '', '工作待遇：': '',
               '工作地點：': '', '電腦專長：': '', '附加條件：': ''}
        for data in jobContent[0].select('li'):  # 職缺細節迴圈
            tle = data.select('.tle')
            info = data.select('.info')
            if len(tle) > 0:
                if tle[0].text.encode('utf-8') in dic:
                    dic[tle[0].text.encode('utf-8')] = ''.join(info[0].text.encode('utf-8').strip().split('\t'))

        empType = dic.get('工作性質：').encode('utf-8')
        # 雇用性質
        exp = dic.get('工作經驗：').encode('utf-8')
        # 年資要求
        salary = dic.get('工作待遇：').encode('utf-8')
        # 薪水
        content = dic.get('工作內容：') + dic.get('電腦專長：') + dic.get('附加條件：')
        content_format = ''.join(content.strip().encode('utf-8').split('\n'))
        # 工作內容
        location = dic.get('工作地點：').encode('utf-8')
        # 地址

        companyDescription = soup2.select('#companyDescription')
        company_address = 'http://www.1111.com.tw/mobileWeb/' + companyDescription[0]['href']
        res3 = rs.get(company_address)
        soup3 = bs(res3.text, 'html.parser')
        company_jobContent = soup3.select('#jobcontent')
        company_dic = {'　行業別：':''}
        for data in company_jobContent[0].select('li'):  # 公司資料迴圈
            tle = data.select('.tle')
            info = data.select('.info')
            if len(tle) > 0:
                if tle[0].text.encode('utf-8') in company_dic:
                    company_dic[tle[0].text.encode('utf-8')] = ''.join(info[0].text.encode('utf-8').strip().split('\t'))

        industry = company_dic.get('　行業別：').encode('utf-8')
        # 產業別
        time.sleep(0.5)

        row_data = '1111人力銀行' + '\t' + postDate + '\t' + jobTitle + '\t' + company + '\t' +                    industry + '\t' + location + '\t' + empType + '\t' + exp + '\t' + salary + '\t' +                    content_format + '\t' + jobDetail_address
        # 欄位 => 來源 張貼日期 職稱 公司名稱 產業別 地址 雇用類型 年資要求 薪水 工作內容 連結
        print row_data
        f.write(row_data.encode('utf-8') + '\n')

f.close()


# In[ ]:

#建字典抓擅長工具、工作技能
                dic={'擅長工具':'','工作技能':''}
                for i in domain3[0].select('li'):
                    if i.select('b')[0].text.strip().encode('utf-8') in dic:
                        dic[i.select('b')[0].text.strip().encode('utf-8')]=''.join(i.select('p')[0].text.strip().split()).encode('utf-8')


# In[62]:

import requests as rs
import time
import chardet
from bs4 import BeautifulSoup as bs
#joblist3 = open('joblist3.txt', 'w')

#f= open("final104.txt","w")

for line in open('104work.txt'):
    try:
        w = rs.get(line)
        wedsite = bs(w.text)
        main = wedsite.select('.main')[0]
        cont = main.select('.content')[0]
        cont2 = main.select('.content')[1]
        #日期
        job_date = main.select('.update')[0].text.encode('utf-8').split()[0]
        #職稱
        job_title = main.select('h1')[0].text.strip().text.encode('utf-8').split()[0]
        #job_title = ''.join(main.select('h1')[0].text.strip().split()[0].encode('utf-8').split()[0])
        #公司名
        companyname = main.select('.cn')[0].text.encode('utf-8')
        #公司屬性
        companyaddr = main.select('.company a')[0]['href']
        res = rs.get(companyaddr)
        res.encoding ='utf-8'#因為抓出為亂碼，需轉換
        soup = bs(res.text)
        company_addr = soup.select('#cont_main')[0]
        companytype = company_addr.select('.intro')[0]
        company_type = companytype.select('dd')[0].text.encode('utf-8')
        #工作性質
        jobtype = cont.select('dd')[2].text.encode('utf-8')
        #工作待遇
        salary = cont.select('dd')[1].text.encode('utf-8')
        #工作地址
        addr = cont.select('dd')[3].text.strip().encode('utf-8').split()[0]
        #工作經歷
        jobexp = cont2.select('dd')[1].text.encode('utf-8')
        #工作內容
        jobcont = cont.select('p')[0].text.strip().encode('utf-8').split()[0]
        #擅長工具
        tool = cont2.select('dd')[5].text.strip().encode('utf-8')
        #工作技能
        skill = cont2.select('dd')[6].text.strip().encode('utf-8')
        #其他條件
        other = cont2.select('dd')[7].text.strip().encode('utf-8')
        content = jobcont + tool + skill  
        
        total = '104人力銀行' + '\t' + job_date + '\t' + job_title+ '\t' + companyname + '\t' + company_type+ '\t' + addr + '\t'+ jobtype + '\t' + jobexp + '\t' + salary + '\t' + content + '\t' + line
        c = main.select('.info')[0].text.encode('utf-8').split()[0]
#         info = '{}'.format(job_title)
        f.write(total)
    except Exception as detail:
        #print line,detail
        
        print jobcont


# In[10]:

import string
a = '''qoo loves oop
       aaaaaaaaaaaaa
    '''
string.join(a.split(),'')


# In[13]:

import requests as rs
import time
import string
from bs4 import BeautifulSoup as bs
#joblist3 = open('joblist3.txt', 'w')

f= open("test.txt","w")
#因為104有獵人頭、接案等不同的網頁格式，所以要用try、except來踢除
for line in open('104work.txt'):
    try:
        w = rs.get(line)
        wedsite = bs(w.text)
        main = wedsite.select('.main')[0]
        cont = main.select('.content')[0]
        cont2 = main.select('.content')[1]
        #日期
        jobdate = main.select('.update')[0].text.encode('utf-8').split()[0]
        #職稱
        job_title = main.select('.header.static')[0]
        title = job_title.select('.center')
        jobtitle1 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[0]
        jobtitle2 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[1]
        jobtitle3 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[2]
        jobtitle4 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[3]
        jobtitle5 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[4]
        jobtitle6 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[5]
        jobtitle = jobtitle1 + jobtitle2 + jobtitle3 + jobtitle4 + jobtitle5 + jobtitle6
        #公司名
        companyname = main.select('.cn')[0].text.encode('utf-8')
        #公司屬性
        companyaddr = main.select('.company a')[0]['href']
        res = rs.get(companyaddr)
        res.encoding ='utf-8'#因為抓出為亂碼，需轉換
        soup = bs(res.text)
        company_addr = soup.select('#cont_main')[0]
        companytype = company_addr.select('.intro')[0]
        companytype = companytype.select('dd')[0].text.encode('utf-8')   
        #工作性質
        jobtype = cont.select('dd')[2].text.encode('utf-8')
        #工作待遇
        salary = cont.select('dd')[1].text.encode('utf-8')
        #工作地址
        addr = cont.select('dd')[3].text.strip().encode('utf-8').split()[0]
        #工作經歷
        jobexp = cont2.select('dd')[1].text.encode('utf-8')
        #工作內容
        #jobcont = cont.select('p')[0].text.encode('utf-8')
        #jobcontent = "".join(jobcont.split('\<br\>'))
        jobcont = cont.select('p')[0].text.strip().encode('utf-8')
        jobcont = "".join(jobcont.split('<br>'))
        jobcont = "".join(jobcont.split('\n'))
        jobcont = "".join(jobcont.split('"'))
        #擅長工具
        tool = cont2.select('dd')[5].text.strip().encode('utf-8')
        #工作技能
        skill = cont2.select('dd')[6].text.strip().encode('utf-8')
        #其他條件
        other = cont2.select('dd')[7].text.strip().encode('utf-8')
        other = "".join(jobcont.split('<br>'))
        other = "".join(jobcont.split('\n'))
        other = "".join(jobcont.split('"'))
        content = tool + skill + other
        
        total = '104人力銀行' + '\t' + jobdate + '\t' + jobtitle+ '\t' + companyname + '\t' + companytype+ '\t' + addr + '\t'+ jobtype + '\t' + jobexp + '\t' + salary + '\t' + content + '\t' + line
        f.write(total)
        
    except Exception as detail:
        print line,detail
        
        
f.close()


# In[45]:

f.close()


# In[7]:

#抓104職缺連結
import requests as rs
import time
from bs4 import BeautifulSoup as bs
address = 'http://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=0&jobcat=2007000000&isnew=0&order=2&asc=0&page={}&psl=L_A'
for page in range(1,125):
    address_format = address.format(page)
    res = rs.get(address_format)
    #print res.encoding
    soup = bs(res.text)
    job_cont = soup.select('.j_cont.line_bottom')
    domain = 'http://www.104.com.tw/'
    for li in job_cont:
        print domain + li.select('a')[0]['href']


# In[3]:

import requests as rs
import time
import string
from bs4 import BeautifulSoup as bs
#joblist3 = open('joblist3.txt', 'w')

f= open("20160219worklist.txt","w")

for line in open('20160219.txt'):
#因為104有獵人頭、接案等不同的網頁格式，所以要用try、except來踢除
    try:
        w = rs.get(line)
        wedsite = bs(w.text)
        main = wedsite.select('.main')[0]
        cont = main.select('.content')[0]
        cont2 = main.select('.content')[1]
        #日期
        jobdate = main.select('.update')[0].text.encode('utf-8').split()[0]
        jobdate = jobdate[15:]
        #職稱
        job_title = main.select('h1')[0].text.strip().encode('utf-8').split()[0]
        job_title = main.select('.header.static')[0]
        title = job_title.select('.center')
        jobtitle1 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[0]
        jobtitle2 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[1]
        jobtitle3 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[2]
        jobtitle4 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[3]
        jobtitle5 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[4]
        jobtitle6 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[5]
        jobtitle = jobtitle1 + jobtitle2 + jobtitle3 + jobtitle4 + jobtitle5 + jobtitle6
        #公司名
        companyname = main.select('.cn')[0].text.encode('utf-8')
        #公司屬性
        companyaddr = main.select('.company a')[0]['href']
        res = rs.get(companyaddr)
        res.encoding ='utf-8'#因為抓出為亂碼，需轉換
        soup = bs(res.text)
        company_addr = soup.select('#cont_main')[0]
        companytype = company_addr.select('.intro')[0]
        companytype = companytype.select('dd')[0].text.encode('utf-8')   
        #工作性質
        jobtype = cont.select('dd')[2].text.encode('utf-8')
        #工作待遇
        salary = cont.select('dd')[1].text.encode('utf-8')
        #工作地址
        addr = cont.select('dd')[3].text.strip().encode('utf-8').split()[0]
        #工作經歷
        jobexp = cont2.select('dd')[1].text.encode('utf-8')
        #工作內容
        #jobcont = cont.select('p')[0].text.encode('utf-8')
        #jobcontent = "".join(jobcont.split('\<br\>'))
        #擅長工具
        tool = cont2.select('dd')[5].text.strip().encode('utf-8')
        #工作技能
        skill = cont2.select('dd')[6].text.strip().encode('utf-8')
        #其他條件
        other = cont2.select('dd')[7].text.strip().encode('utf-8')
        content = tool + skill + other
        #因為雙引號包覆功能較強,避免存入格式時跑掉
        total = '"' + '104人力銀行' + '",' + '"'+ jobdate + '",' + '"'+ jobtitle+ '",' +'"'+companyname + '",' + '"'+companytype+ '",' + '"'+addr + '",'+ '"'+jobtype + '",' + '"'+jobexp + '",' + '"'+salary + '",' +'"'+ content + '",' + '"'+line
        f.write(total)
        #print total

    except Exception as detail:
        print line,detail
        
        
f.close()


# # 連接到資料庫

# In[18]:

import MySQLdb

try:
    db = MySQLdb.connect("","root","ellehcim","django",charset='utf8')
except MySQLdb.Error as e:
    print "Error %d: %s" % (e.args[0], e.args[1])


# # 讀取資料庫資料

# In[ ]:

import MySQLdb

try:
    db = MySQLdb.connect("10.120.26.46","fu","iiizb104","project",charset='utf8')
    sql = "SELECT * FROM jobstored"

    # 執行SQL statement
    cursor = db.cursor()
    cursor.execute(sql)

    # 撈取多筆資料
    results = cursor.fetchall()

    # 迴圈撈取資料
    for record in results: 
        col1 = record[0]
        col2 = record[1]
        col3 = record[2]
        col4 = record[3]
        col5 = record[4]
        col6 = record[5]
        col7 = record[6]
        col8 = record[7]
        col9 = record[8]
        col10 = record[9]
        col11 = record[10]
        col12 = record [11]
        
        
        print "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (col1, col2, col3, col4, col5, col6, col7 ,col8 ,col9, col10, col11, col12)

    # 關閉連線
    db.close()

except MySQLdb.Error as e:
    print "Error %d: %s" % (e.args[0], e.args[1])


# In[ ]:

def writeintomysql():

    import _mysql_exceptions
    import requests as rs
    from bs4 import BeautifulSoup as bs
    import time
    import datetime
    import MySQLdb
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")  # 避免字型轉碼錯誤

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day

    filename = 'TextFile/InsertCopy_1111_' + ''.join(str(yesterday).split('-')) + '.txt'
    f = open(filename, 'w')

    src = '1111人力銀行'
    count = 0
    address = 'http://www.1111.com.tw/mobileWeb/job-index.asp?role=1%2C2%2C4%2C16&keys=&c0Cht=&c0=&d0Cht='               '%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%2C%E7%B3%BB%E7%B5%B1%E8%A6%8F%E5%8A%83%2C%E7%B6%B2%E8'               '%B7%AF%E7%AE%A1%E7%90%86&d0=140200%2C140300%2C140400&t0Cht=&t0=&gr=&ex=&wk=&si=1&page={}'
    # 1111 human resource bank - 軟體工程(SE) + 系統規劃(SA) + 網路管理(MIS)

    for page in range(1, 160):  # 換頁迴圈
        address_format = address.format(page)
        res = rs.get(address_format)
        # print res.encoding - 'utf-8'
        soup = bs(res.text, 'html.parser')
        jobList = soup.select('.jobList li')
        for li in jobList:  # 職缺列表迴圈
            jobTitle = ''.join(li.select('.list_content p')[0].text.encode('utf-8').split(','))
            # 職稱
            company = ''.join(li.select('.black')[0].text.encode('utf-8').split(','))
            # 公司名稱
            postDate = ''.join(li.select('.gray')[1].text.encode('utf-8')[15:].split(','))
            # 公告日期
            jobURL = 'http:' + li.select('a')[0]['href'].encode('utf-8')
            # 職缺網址

            try:
                res2 = rs.get(jobURL)  # 要求進入工作內容細節
                soup2 = bs(res2.text, 'html.parser')
                jobContent = soup2.select('#jobcontent')  # 來自 jobURL (soup2)
                dic = {'工作性質：': '', '工作內容：': '', '工作經驗：': '', '工作待遇：': '',
                       '工作地點：': '', '電腦專長：': '', '附加條件：': ''}  # 建立字典抓取資料
                for data in jobContent[0].select('li'):  # 職缺細節迴圈
                    tle = data.select('.tle')
                    info = data.select('.info')
                    if len(tle) > 0:
                        if tle[0].text.encode('utf-8') in dic:
                            dic[tle[0].text.encode('utf-8')] = ''.join(info[0].text.strip().split(','))

                empType = dic.get('工作性質：').encode('utf-8')
                # 雇用性質
                exp = dic.get('工作經驗：').encode('utf-8')
                # 年資要求
                salary = dic.get('工作待遇：').encode('utf-8')
                # 薪水
                content = dic.get('工作內容：') + dic.get('電腦專長：') + dic.get('附加條件：')
                content = ''.join(content.strip().encode('utf-8').split('\n'))
                # 工作內容
                # skill = GetSkill.getsSkill(content)
                # 內容中的職缺技能
                location = dic.get('工作地點：').encode('utf-8')
                # 地址

                companyDescription = soup2.select('#companyDescription')  # 來自 jobURL (soup2)
                companyURL = 'http://www.1111.com.tw/mobileWeb/' + companyDescription[0]['href']
                res3 = rs.get(companyURL)  # 要求進入公司資料
                soup3 = bs(res3.text, 'html.parser')
                company_jobContent = soup3.select('#jobcontent')
                company_dic = {'　行業別：': ''}
                for data in company_jobContent[0].select('li'):  # 公司資料迴圈
                    tle = data.select('.tle')
                    info = data.select('.info')
                    if len(tle) > 0:
                        if tle[0].text.encode('utf-8') in company_dic:
                            company_dic[tle[0].text.encode('utf-8')] = ''.join(info[0].text.strip().split(','))

                industry = company_dic.get('　行業別：').encode('utf-8')
                # 產業別
            except rs.exceptions.ConnectionError as e:
                print "Can not connect to this address!"
                print "Error message is %s" % e
                print jobTitle + '\t' + jobURL
            except IndexError as e:
                print "List index out of range!"
                print "Error message is %s" % e
                print jobTitle + '\t' + jobURL
            except Exception as e:
                print "Unknown exception!"
                print "Error message is %s" % e
                print jobTitle + '\t' + jobURL

            time.sleep(1)

            row_data = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'                .format(src, postDate, jobTitle, company, industry, location, empType, exp, salary, content, jobURL)

            row_data = ''.join(row_data.split('\t'))
            # 欄位 => 來源 張貼日期 職稱 公司名稱 產業別 地址 雇用類型 年資要求 薪水 工作內容 連結

            f.write(row_data.encode('utf-8') + '\n')

            if postDate == str(yesterday):

                db = MySQLdb.connect(host="localhost", user="jao", passwd="iiizb104", db="project")
                db.set_character_set('utf8')
                cursor = db.cursor()
                sql = (
                    'insert into '
                    'project.jobstored(srcno, postdate, title, company, industry, locno, emptypeno, exp, salary, content, url)'
                    ' VALUES '
                    '("' + src + '","' + postDate + '","' + jobTitle + '","' + company + '","' + industry + '","' + location + '","' + empType + '","' + exp + '","' + salary + '","' + content + '","' + jobURL + '")'
                )

                try:
                    cursor.execute(sql)
                    count += 1
                except _mysql_exceptions.IntegrityError as e:
                    print "Data duplicate entry!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except _mysql_exceptions.OperationalError as e:
                    print "Incorrect string value!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except _mysql_exceptions.DataError as e:
                    print "Data too long for column!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL
                except Exception as e:
                    print "Unknown exception!"
                    print "Error message is %s" % e
                    print jobTitle + '\t' + jobURL

                db.commit()

                cursor.close()
                db.close()

    f.close()
    print '匯入MySQL的資料筆數共 ' + str(count) + ' 筆'


# # 寫入資料庫

# In[90]:

import MySQLdb
import os
import re
db = MySQLdb.connect("localhost","帳號","密碼","dbname",charset='utf8')#連結資料庫
for i in open():
    a= "\"104\""
    b= 
    c= re.sub(r'["]','',a)
    sql = "INSERT INTO iiimap_comment(C_id,C_date,C_content,Attraction_id)VALUES({},{},{},{});".format(a,b,e,g)
    cursor = db.cursor()
    try:
            # 執行sql語句
            cursor.execute(sql)
            print "新增資料成功:"
            # 確認新增到資料庫
            db.commit()
        except MySQLdb.Error as e:
            print "新增資料失敗 %d: %s" % (e.args[0], e.args[1])  
        # 关闭数据库连接
    db.close()


# In[3]:

import MySQLdb, csv, sys,re
conn = MySQLdb.connect (host = "localhost",user = "root", passwd = "ellehcim",db = "finalproject",charset='utf8')

c = conn.cursor()
for i in open("20160128worklist.txt"):
    
    '''    #原本這是字串,這是把內容包起來,如果沒包mysql會認為這是空值(mysql無法存入字串)
    A = i.split("\",")[0]
    srcno = re.sub(r'["]','',A)
    B = i.split("\",")[1]
    postdate = re.sub(r'["]','',B)
    C = i.split("\",")[2]
    title = re.sub(r'["]','',C)
    D = i.split("\",")[3]
    company = re.sub(r'["]','',D)
    E = i.split("\",")[4]
    industry = re.sub(r'["]','',E)
    F = i.split("\",")[5]
    locno = re.sub(r'["]','',F)
    G = i.split("\",")[6]
    emptypeno = re.sub(r'["]','',G)
    H = i.split("\",")[7]
    exp = re.sub(r'["]','',H)
    I = i.split("\",")[8]
    salary = re.sub(r'["]','',I)
    J = i.split("\",")[9]
    content = re.sub(r'["]','',J)
    K = i.split("\",")[10]
    url = re.sub(r'["]','',K) 
    print srcno + ","+title + "," + company
    '''
    #sql = "INSERT INTO jobstored(srcno, postdate, title, company, industry, locno, emptypeno, exp, salary, content, url) VALUES ('" + src + '","' + postDate + '","' + jobTitle + '","' + company + '","' + industry + '","' + location + '","' + empType + '","' + exp + '","' + salary + '","' + content + '","' + jobURL + "')"

    sql = "INSERT INTO jobstored(srcno, postdate, title, company, industry, locno, emptypeno, exp, salary, content, url) VALUES (" + i + ")"
    try:
        c.execute(sql)
        print "新增資料成功:"
        #確認新增到資料庫
        conn.commit()
    except Exception as e:
        print e 

c.close()


# In[92]:

class('A')


# In[2]:

import csv
import MySQLdb
# open the connection to the MySQL server.
# using MySQLdb
mydb = MySQLdb.connect(host="localhost",user="csv",passwd="csv",db="csvdb")
cursor = mydb.cursor()
# read the presidents.csv file using the python
# csv module http://docs.python.org/library/csv.html
csv_data = csv.reader(file("104try.csv"))
# execute the for clicle and insert the csv into the
# database.
for row in csv_data:

cursor.execute("INSERT INTO jobstored(jodno,scrno,postdate,title,company,industry,locno,emptypeno,exp,salary,content,url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s), row")
#close the connection to the database.
cursor.close()
print "Import to MySQL is over"


# In[90]:

import MySQLdb

try:
    db = MySQLdb.connect("localhost","root","ellehcim","finalproject",charset='utf8')
    sql = "SELECT * FROM jobstored"

    # 執行SQL statement
    cursor = db.cursor()
    cursor.execute(sql)

    # 撈取多筆資料
    results = cursor.fetchall()

    # 迴圈撈取資料
    for record in results: 
        col1 = record[0]
        col2 = record[1]
        col3 = record[2]
        col4 = record[3]
        col5 = record[4]
        col6 = record[5]
        col7 = record[6]
        col8 = record[7]
        col9 = record[8]
        col10 = record[9]
        col11 = record[10]
        col12 = record [11]
        
        
        print "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (col1, col2, col3, col4, col5, col6, col7 ,col8 ,col9, col10, col11, col12)

    # 關閉連線
    db.close()

except MySQLdb.Error as e:
    print "Error %d: %s" % (e.args[0], e.args[1])


# In[10]:

import numpy as np
import numpy.linalg as LA
import random
import MySQLdb
import json

def getDocDistance(a, b):
    if LA.norm(a)==0 or LA.norm(b)==0:
        return -1
    return round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 4)

#test sample
my_randoms = []
for each in range(26):
    my_randoms.append(random.random())

def getRecommendCluster(a):
    db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
    cursor = db.cursor()
    sql = "SELECT clusterVector FROM project.cluster;"

    cursor.execute(sql)
    results = cursor.fetchall()

    tmpCom = []
    for row in results:
        vec = json.loads(row[0])
        tmpCom.append(getDocDistance(vec, a))

    # print ('max value:', max(tmpCom))
    return [i for i, j in enumerate(tmpCom) if j == max(tmpCom)][0]


# In[11]:

my_randoms = []
for each in range(26):
    my_randoms.append(random.random())
    
print getRecommendCluster(my_randoms)


# In[29]:

import MySQLdb
import json

db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
cursor = db.cursor()
sql = "SELECT loc FROM project.location where no = 2;"

cursor.execute(sql)
results = cursor.fetchone()
print json.load(results[0])


# In[10]:

import json
tmp = {'台東縣':'1.25','宜蘭縣':'5.586','台北市':'1.72349','雲林縣':'6.395','桃園市':'5.4086','屏東縣':'6.35','台中市':'8.8197','台南市':'3.3778','基隆市':'5.649','連江縣':'1.49','南投縣':'5.013','澎湖縣':'6.59','苗栗縣':'6.85','嘉義市':'4.379','新竹縣':'1.1176','新北市':'1.27074','花蓮縣':'3.608','高雄市':'8.1647','彰化縣':'2.4969','嘉義縣':'4.384','金門縣':'1.089','新竹市':'1.0949'}
print json.loads(tmp)


# In[38]:

import json
c = {"properties":{"COUNTYSN":"10018001","COUNTYNAME":"新竹市","name":"新竹市"},"type":"Feature","geometry":{ "type": "Polygon", "coordinates": [ [ [ 120.910900610308317, 24.827204872753327 ], [ 120.911061192976604, 24.82746221079071 ], [ 120.911318524094938, 24.827744524954205 ], [ 120.911440603200973, 24.828019987180625 ], [ 120.911447382494202, 24.828268295305172 ], [ 120.911751363873734, 24.828765065170366 ], [ 120.912353786331849, 24.829618620580554 ], [ 120.9133519220713, 24.830731975050604 ], [ 120.913509912851978, 24.830948752471112 ], [ 120.913665655155896, 24.83128289996564 ], [ 120.913834850585317, 24.831838345529015 ], [ 120.913985510021249, 24.832147570846427 ], [ 120.915290822042834, 24.834229475663392 ], [ 120.915792965220803, 24.834866310128149 ], [ 120.917255422652858, 24.83692125404874 ], [ 120.917719897507695, 24.837510751273637 ], [ 120.918567196702895, 24.838876786887649 ], [ 120.919213856462164, 24.839719106251245 ], [ 120.919516615843278, 24.840082082699901 ], [ 120.919935780788904, 24.840493739772313 ], [ 120.920230822378542, 24.840861929123335 ], [ 120.920412882360381, 24.841189239595835 ], [ 120.920795368117012, 24.842261729771522 ], [ 120.920848940598233, 24.84240496026985 ], [ 120.92093341811082, 24.842512264371209 ], [ 120.921008435519937, 24.843182756425527 ], [ 120.920970471226894, 24.843568626326594 ], [ 120.920901285593516, 24.843694989655127 ], [ 120.918355686565846, 24.845257819567003 ], [ 120.918336761023042, 24.845354776004104 ], [ 120.918794555342373, 24.84652430567683 ], [ 120.918819553607705, 24.846725213803698 ], [ 120.918775528801362, 24.846903513014638 ], [ 120.917304377870721, 24.848209761911829 ], [ 120.913559878282399, 24.85169260283357 ], [ 120.913507489472821, 24.851656458293544 ], [ 120.91323627190252, 24.851920314063996 ], [ 120.91343559178307, 24.852107871510057 ], [ 120.916712124152966, 24.849073881463713 ], [ 120.918935350829102, 24.846960037341429 ], [ 120.919020376082884, 24.846971369143944 ], [ 120.91904553758252, 24.847030068430637 ], [ 120.919390501067326, 24.848043774140912 ], [ 120.919496729627468, 24.848016745724948 ], [ 120.919164945554343, 24.84707076160004 ], [ 120.923256817327172, 24.844617131543785 ], [ 120.924066436016346, 24.84592668701583 ], [ 120.922268861899852, 24.846934713788471 ], [ 120.922375608671388, 24.847065782747958 ], [ 120.923657871531077, 24.846350821354786 ], [ 120.924109895268998, 24.846910831543774 ], [ 120.924455116027744, 24.847446075200601 ], [ 120.924712132813411, 24.848114363640104 ], [ 120.923442552712118, 24.84879089677591 ], [ 120.92352410703721, 24.848917347412691 ], [ 120.924779612122734, 24.848256507180789 ], [ 120.925422659542107, 24.8500039733091 ], [ 120.923130257419302, 24.851253339122842 ], [ 120.920639498087397, 24.84862004954757 ], [ 120.921476559949269, 24.847843990378326 ], [ 120.921407492214854, 24.847780745109706 ], [ 120.920274664377715, 24.848802692713111 ], [ 120.919968126164619, 24.84849111574805 ], [ 120.919862002742505, 24.848592548918958 ], [ 120.920545672104282, 24.849315243945622 ], [ 120.920762470672642, 24.849978994279542 ], [ 120.920747562193156, 24.850082823826334 ], [ 120.920687827924667, 24.85017091989166 ], [ 120.920561142402306, 24.850265562171561 ], [ 120.914062787754119, 24.853769586853392 ], [ 120.912960217437515, 24.853789181577572 ], [ 120.912960023080174, 24.854066917806076 ], [ 120.914137130097572, 24.854033642544081 ], [ 120.914176075761844, 24.854060750579794 ], [ 120.914360612592901, 24.853945742421775 ], [ 120.914338383729813, 24.853891549331596 ], [ 120.917580151066275, 24.852166553431907 ], [ 120.917944968217682, 24.852281967628272 ], [ 120.918416032864499, 24.853769679980612 ], [ 120.918577328227073, 24.853724625200975 ], [ 120.918108949392348, 24.852146620231277 ], [ 120.918153855741124, 24.852044974270147 ], [ 120.918078609910708, 24.851963676029328 ], [ 120.918193930220383, 24.851762844811802 ], [ 120.920027459632479, 24.8507761494131 ], [ 120.920102239324152, 24.850750611514467 ], [ 120.920239304959225, 24.850747840748411 ], [ 120.920895979858329, 24.850823289387574 ], [ 120.921305632270872, 24.850918314586853 ], [ 120.922350061369983, 24.851295821347829 ], [ 120.922839805702452, 24.851645931653437 ], [ 120.9236400189927, 24.85232146211278 ], [ 120.92825429173412, 24.851971536045333 ], [ 120.929796460699322, 24.850840773579662 ], [ 120.929865018190497, 24.850798172920101 ], [ 120.929921096322161, 24.850786832276182 ], [ 120.930036352874296, 24.850795409248153 ], [ 120.930136043370055, 24.850786932934344 ], [ 120.930232622938973, 24.850764235120931 ], [ 120.930322990897878, 24.850715956440506 ], [ 120.930394679960997, 24.850644935092664 ], [ 120.93044456686637, 24.850562527577413 ], [ 120.93047889596285, 24.850451690901469 ], [ 120.930503875681623, 24.850343693864019 ], [ 120.930553897653454, 24.850022535134599 ], [ 120.930658957195149, 24.849794396096566 ], [ 120.930694258103415, 24.849698574306014 ], [ 120.930718461873155, 24.849552999992252 ], [ 120.931041085570612, 24.847128890023949 ], [ 120.930970723651512, 24.846406554361888 ], [ 120.930897084955234, 24.846212487447719 ], [ 120.930740116748254, 24.846015935154437 ], [ 120.930759533268414, 24.845853420954139 ], [ 120.930872333283318, 24.845684178549913 ], [ 120.93096554107612, 24.845436008315421 ], [ 120.931186731259587, 24.845237472855505 ], [ 120.931293688486662, 24.845007185291344 ], [ 120.931331276558723, 24.844973345444473 ], [ 120.931435190416096, 24.844966305731816 ], [ 120.931475839567909, 24.844950840385032 ], [ 120.93151932527671, 24.844912335425835 ], [ 120.93165197332128, 24.844772597829081 ], [ 120.931777665115703, 24.84458980873011 ], [ 120.93230572878845, 24.844118369430891 ], [ 120.932571544563885, 24.844012304617621 ], [ 120.932999833602352, 24.843642307904595 ], [ 120.933169613180297, 24.843583689201527 ], [ 120.933275009502566, 24.84366048815216 ], [ 120.933326513767085, 24.843946689653635 ], [ 120.933366970559547, 24.844017771553066 ], [ 120.93346972669093, 24.844083202219036 ], [ 120.933508659181172, 24.844148162031694 ], [ 120.933551088903016, 24.844308537288235 ], [ 120.933606633515794, 24.844367509490372 ], [ 120.933653158252568, 24.844384079515976 ], [ 120.933699508817355, 24.844387729570162 ], [ 120.933743682245336, 24.844384625276518 ], [ 120.933790398224431, 24.84439885694529 ], [ 120.933840217883088, 24.844435832934149 ], [ 120.934008346611435, 24.844580869943179 ], [ 120.934021211754057, 24.844617504519782 ], [ 120.934023843201018, 24.844650134922404 ], [ 120.934014504276206, 24.84472016539241 ], [ 120.934015840856205, 24.844754059222335 ], [ 120.934029073768087, 24.844778243566282 ], [ 120.93407144481769, 24.844795181798666 ], [ 120.934145270208262, 24.844842451810131 ], [ 120.93417639393806, 24.844893621380717 ], [ 120.934201258565025, 24.844998815131021 ], [ 120.934235507147704, 24.845032931102097 ], [ 120.934282222909275, 24.845050015643281 ], [ 120.93453142019797, 24.845064335983707 ], [ 120.934587482866263, 24.845078571496902 ], [ 120.934644023185456, 24.845110268445449 ], [ 120.934976874297504, 24.845437807510592 ], [ 120.935027044260636, 24.84558229541587 ], [ 120.93486745465529, 24.845812066143573 ], [ 120.934808174554803, 24.845991121891469 ], [ 120.934755157707968, 24.846101960507283 ], [ 120.934722266336834, 24.846263774144916 ], [ 120.934731315931685, 24.846401472741931 ], [ 120.934754935617818, 24.846525490393873 ], [ 120.934814683998681, 24.846631746560391 ], [ 120.934829576245335, 24.846758604387482 ], [ 120.934814553909789, 24.846880050083428 ], [ 120.934749862935305, 24.84700417363716 ], [ 120.934539654431731, 24.847176328647031 ], [ 120.934520946953896, 24.847207586367734 ], [ 120.934527158682371, 24.847241708032289 ], [ 120.9345805109797, 24.847307152371862 ], [ 120.934585883986628, 24.847335007843146 ], [ 120.934571505708803, 24.847356308958773 ], [ 120.934472707267375, 24.847393959921117 ], [ 120.934422790206199, 24.847439685755692 ], [ 120.934416988676688, 24.847475869692403 ], [ 120.934438520560093, 24.847515216592029 ], [ 120.934474432502981, 24.847529985016344 ], [ 120.934521128276629, 24.847526728116414 ], [ 120.934623515874762, 24.847492347033167 ], [ 120.934677396291974, 24.847490736426021 ], [ 120.934727678062345, 24.847502224673327 ], [ 120.934777948145737, 24.847528474599972 ], [ 120.934824619405205, 24.847577664519864 ], [ 120.934826390272818, 24.847623539423072 ], [ 120.934804810408835, 24.847679263331351 ], [ 120.934799736951646, 24.847719754224265 ], [ 120.934804770909025, 24.847754642789095 ], [ 120.934824511238361, 24.847784147716364 ], [ 120.934847834510364, 24.847826772705425 ], [ 120.934849604065349, 24.847880845541582 ], [ 120.934838804682471, 24.847926723990319 ], [ 120.934808249076326, 24.847967691310583 ], [ 120.934772860576857, 24.847986554592719 ], [ 120.934684305260504, 24.848011877144952 ], [ 120.934655557788759, 24.848033171985204 ], [ 120.934614220224972, 24.848092155561236 ], [ 120.934590862392326, 24.848113443718436 ], [ 120.934558532443774, 24.848115072761757 ], [ 120.934466498706144, 24.848114635171314 ], [ 120.934411430080814, 24.848134212020199 ], [ 120.934327282799771, 24.848208073847758 ], [ 120.934246361918454, 24.848351547263732 ], [ 120.933579285895902, 24.848903691894211 ], [ 120.933422339512788, 24.849121743067389 ], [ 120.933373596855418, 24.849215546151587 ], [ 120.933358639856891, 24.849289384084383 ], [ 120.93337352069959, 24.84935774595705 ], [ 120.9334010022516, 24.849373242190556 ], [ 120.933468167351833, 24.849334575698055 ], [ 120.933514109079908, 24.849334596146722 ], [ 120.933528224900726, 24.84937007564368 ], [ 120.933485798886053, 24.849408753177315 ], [ 120.93343275029747, 24.849479666958189 ], [ 120.933392264531193, 24.849581301484221 ], [ 120.933310466685199, 24.849885888636749 ], [ 120.93329816819795, 24.850024552806662 ], [ 120.933322825836555, 24.850195212628751 ], [ 120.933372980290756, 24.850366777641746 ], [ 120.933319077400554, 24.850575945326952 ], [ 120.933315512804, 24.850633988346022 ], [ 120.933343761176218, 24.850675920552497 ], [ 120.933382634451803, 24.850675937888962 ], [ 120.933414454565479, 24.850650157477677 ], [ 120.933573913372882, 24.850481890956484 ], [ 120.933630525562577, 24.850436773314104 ], [ 120.933768767417391, 24.850396206135038 ], [ 120.933948233044205, 24.850373082177327 ], [ 120.934124931007844, 24.850379832288827 ], [ 120.93427139500298, 24.850426005644799 ], [ 120.934472431201186, 24.850649559828746 ], [ 120.934648161693389, 24.851067234753849 ], [ 120.934717806352495, 24.85148232611262 ], [ 120.934672804325743, 24.851796066910168 ], [ 120.934534432657742, 24.85208277141118 ], [ 120.934440211268281, 24.852202277233314 ], [ 120.934220115629657, 24.852362536709968 ], [ 120.93382422673082, 24.852518023250571 ], [ 120.933743114596609, 24.85257762092419 ], [ 120.933697582492044, 24.852632963838889 ], [ 120.933648144945892, 24.852763991399165 ], [ 120.934359119885968, 24.852637896617718 ], [ 120.935560635777037, 24.852272826268013 ], [ 120.936136829722571, 24.852049517535619 ], [ 120.937886207504576, 24.851197002037924 ], [ 120.939574840425195, 24.850462101573196 ], [ 120.940171687671409, 24.850135128645938 ], [ 120.940561434471974, 24.849848519032019 ], [ 120.940850700150392, 24.849534873246551 ], [ 120.942045119489038, 24.848038757684233 ], [ 120.942843059146213, 24.846982659787848 ], [ 120.943139427464089, 24.846465851367157 ], [ 120.944063348789982, 24.844055708028865 ], [ 120.944800893444679, 24.841069592937021 ], [ 120.946240194801547, 24.840392929456737 ], [ 120.947434211240093, 24.839894498369055 ], [ 120.947662606076094, 24.839765912308149 ], [ 120.950523894592521, 24.837755645187766 ], [ 120.951925735669249, 24.836815099116492 ], [ 120.954308250015558, 24.835000984520128 ], [ 120.954794561275065, 24.834648999662555 ], [ 120.95530110388971, 24.834342162161477 ], [ 120.95703615930347, 24.833570672949019 ], [ 120.957186889936736, 24.833548144735822 ], [ 120.957772745145675, 24.833634091931788 ], [ 120.958109595535845, 24.833627505550691 ], [ 120.958416645820208, 24.833501182089719 ], [ 120.959946829566135, 24.833016476065314 ], [ 120.960303021861847, 24.832942166515544 ], [ 120.960926784892408, 24.832919669101631 ], [ 120.961768730736182, 24.832700934599778 ], [ 120.962642034195738, 24.832547660421781 ], [ 120.963226384790829, 24.832495881914102 ], [ 120.964325805486723, 24.832478091137379 ], [ 120.965280673658199, 24.832514430281005 ], [ 120.96621788954846, 24.832652339940637 ], [ 120.966637586000928, 24.832679528971774 ], [ 120.967165348808223, 24.832657065327862 ], [ 120.967809228819078, 24.832542090906649 ], [ 120.968842938691566, 24.832267010310566 ], [ 120.970156102746785, 24.831797755670522 ], [ 120.972347552785237, 24.830859149932966 ], [ 120.973303765238924, 24.830346825014537 ], [ 120.973743591691871, 24.830175540310947 ], [ 120.974208606213267, 24.830038025574666 ], [ 120.974924812875955, 24.829918428333009 ], [ 120.977330161943442, 24.82969544512439 ], [ 120.978160112329292, 24.829718049848299 ], [ 120.978731741637262, 24.829837833281019 ], [ 120.979385135616653, 24.83005697640677 ], [ 120.97978084063493, 24.830262349562624 ], [ 120.981382823861978, 24.831226422521688 ], [ 120.981514685123727, 24.831226438883672 ], [ 120.981862676311025, 24.831106843701949 ], [ 120.982125936919104, 24.831118161141426 ], [ 120.982293820801843, 24.831091095357841 ], [ 120.982722824051493, 24.830912821927644 ], [ 120.982799655964442, 24.830906149632249 ], [ 120.983015760222685, 24.830962512722021 ], [ 120.983769716834402, 24.83063077783169 ], [ 120.985103885058635, 24.829707680380707 ], [ 120.985365621789867, 24.8294548876849 ], [ 120.985635717562246, 24.829105037989851 ], [ 120.986239000973569, 24.828166347088729 ], [ 120.986935397844007, 24.826568249544948 ], [ 120.98719559881728, 24.826141643959712 ], [ 120.987522262853588, 24.825735357793132 ], [ 120.98771704824108, 24.825557050167816 ], [ 120.987861587696599, 24.825471371587355 ], [ 120.988181878014274, 24.825385535316595 ], [ 120.988722142572499, 24.825306567814181 ], [ 120.988885539904118, 24.825243379889915 ], [ 120.989570368516297, 24.824870972620456 ], [ 120.990449828756923, 24.824286393736418 ], [ 120.991949763531025, 24.823670524122566 ], [ 120.992383368593607, 24.82353285171634 ], [ 120.992665942061222, 24.823487722860563 ], [ 120.993777985832821, 24.82344262125498 ], [ 120.994531861416533, 24.823379450546927 ], [ 120.995653317559118, 24.823361430156631 ], [ 120.995907602594713, 24.823239542249368 ], [ 120.996237625284436, 24.823144741622738 ], [ 120.997809525248371, 24.822783610972579 ], [ 120.99888228817926, 24.822467703186614 ], [ 121.000251521393579, 24.82211342497391 ], [ 121.000534547385755, 24.821968966660243 ], [ 121.001106163678088, 24.82153324336274 ], [ 121.00149553279816, 24.8211202718587 ], [ 121.001803438316117, 24.82072969125003 ], [ 121.001941624960793, 24.820494945924068 ], [ 121.002202076059007, 24.820215055711358 ], [ 121.002428213191521, 24.820054884839401 ], [ 121.002896408780316, 24.819824556902322 ], [ 121.003675462149232, 24.819567314944827 ], [ 121.004410311358527, 24.819269351238294 ], [ 121.004667984735079, 24.819102224003245 ], [ 121.00558505150056, 24.818305418431635 ], [ 121.006401012908086, 24.817467982798739 ], [ 121.007193631457255, 24.816784030023431 ], [ 121.0076519278918, 24.816510891990788 ], [ 121.008201109262856, 24.816271695143531 ], [ 121.008372824854092, 24.816118199342789 ], [ 121.01040337396789, 24.813702829333891 ], [ 121.013671323824838, 24.810167955765994 ], [ 121.014224595573566, 24.809522268090078 ], [ 121.015116475212182, 24.808594490582895 ], [ 121.015330067919635, 24.808468068249486 ], [ 121.016064982886718, 24.808199480144491 ], [ 121.017151522638912, 24.807923896489278 ], [ 121.017406074198391, 24.807820128304364 ], [ 121.017553517569752, 24.807756910772206 ], [ 121.01815648226146, 24.807343689374921 ], [ 121.018256928156845, 24.807212762224559 ], [ 121.01837003181798, 24.806959947135713 ], [ 121.018772040671692, 24.805892263316956 ], [ 121.019453767961593, 24.804673312799064 ], [ 121.019657270305643, 24.804345998765346 ], [ 121.019889532094766, 24.804097681041132 ], [ 121.020103103257952, 24.803921594418266 ], [ 121.020539337064719, 24.803409160991535 ], [ 121.020913250481613, 24.802734219806364 ], [ 121.021183140042723, 24.802023268189338 ], [ 121.021297286552624, 24.801614616549674 ], [ 121.021529496697397, 24.801436358312248 ], [ 121.022421323455603, 24.800898933993633 ], [ 121.023721456834963, 24.800278015672731 ], [ 121.024066841168391, 24.800054592365552 ], [ 121.024324283260881, 24.799826487691291 ], [ 121.024796238391417, 24.79958498481199 ], [ 121.025289346881394, 24.799243981416836 ], [ 121.025526716780362, 24.799137854769409 ], [ 121.025713716263326, 24.799099451097156 ], [ 121.025718492960323, 24.799029478430619 ], [ 121.025611688213417, 24.798988958220392 ], [ 121.024099385651397, 24.798910118646123 ], [ 121.023001870060824, 24.79865532297654 ], [ 121.022158624297276, 24.798515416223598 ], [ 121.02143550772999, 24.79860355065253 ], [ 121.020613494281235, 24.79880229590874 ], [ 121.020650092073723, 24.798603661093335 ], [ 121.020812955485738, 24.798427580321896 ], [ 121.021212259092977, 24.798131927027029 ], [ 121.021425650599241, 24.797901576360765 ], [ 121.021639035252022, 24.797641972632679 ], [ 121.022094632632673, 24.796890272816768 ], [ 121.022336144859594, 24.796601320863942 ], [ 121.022524521196971, 24.796474891832485 ], [ 121.023014415556176, 24.796307877955826 ], [ 121.023108595882874, 24.796199799785697 ], [ 121.023133765928407, 24.796084590592525 ], [ 121.023091836438155, 24.795843081239383 ], [ 121.022948460692035, 24.795678050919506 ], [ 121.022607948207934, 24.795456901319497 ], [ 121.021581841246018, 24.795156850858746 ], [ 121.021421714081598, 24.795080220793391 ], [ 121.021081973579882, 24.794836496014653 ], [ 121.020786589167159, 24.794585902542771 ], [ 121.020678844001111, 24.794430263870606 ], [ 121.020607090298711, 24.794177472093573 ], [ 121.020633642128431, 24.793985519730352 ], [ 121.02117590213939, 24.792793664529594 ], [ 121.021894177334204, 24.791053571864047 ], [ 121.021926906906018, 24.790861609260322 ], [ 121.02178870279279, 24.790604295273813 ], [ 121.0218110853328, 24.790457657941488 ], [ 121.021911528867463, 24.790412500092735 ], [ 121.022069006980374, 24.790412476957613 ], [ 121.022861240716608, 24.790730545233686 ], [ 121.023131219502517, 24.790705783352482 ], [ 121.023407671721074, 24.790604168226682 ], [ 121.023550748141645, 24.790468716249521 ], [ 121.024442373162586, 24.789351279561636 ], [ 121.024561724341893, 24.789098458184849 ], [ 121.024575489811511, 24.788874997148501 ], [ 121.024328381178279, 24.788053431446443 ], [ 121.024311367499479, 24.787581687829167 ], [ 121.024386568960026, 24.78729501629855 ], [ 121.02454985417252, 24.78699704450035 ], [ 121.024713155595194, 24.78678484459148 ], [ 121.025033907957933, 24.786493707934873 ], [ 121.025078850886288, 24.786358270804751 ], [ 121.025064763643826, 24.786229524747913 ], [ 121.024976812276122, 24.78613022439864 ], [ 121.024763227221172, 24.786033292277221 ], [ 121.023833677402493, 24.785857294362817 ], [ 121.023312401627464, 24.785661003493857 ], [ 121.023098813106628, 24.78552334981709 ], [ 121.023036132942707, 24.785444358859841 ], [ 121.022985885347566, 24.78530667979458 ], [ 121.02300471280958, 24.785168990111487 ], [ 121.023111238311415, 24.785035801232024 ], [ 121.023305925120326, 24.784916141539682 ], [ 121.02459338854365, 24.784428388875369 ], [ 121.025355771246481, 24.784060344488452 ], [ 121.026382940595667, 24.783337875501292 ], [ 121.026715756802005, 24.783154986436106 ], [ 121.027268151271542, 24.782927003859935 ], [ 121.027412773306622, 24.782841115039197 ], [ 121.027500677549071, 24.782741783825877 ], [ 121.027500653672249, 24.782633440091274 ], [ 121.027268122051836, 24.782082735257543 ], [ 121.027009745901353, 24.78134703771962 ], [ 121.026921932214591, 24.781152847345005 ], [ 121.026771843222122, 24.780954244024656 ], [ 121.026614815457606, 24.780816585150777 ], [ 121.026313291134542, 24.780622522526585 ], [ 121.026074655576281, 24.780396848083939 ], [ 121.025867262316751, 24.780299916379256 ], [ 121.025641190510441, 24.780299955264585 ], [ 121.025111057333859, 24.780525761305356 ], [ 121.024944163131366, 24.780500870134624 ], [ 121.024881405205278, 24.78039705112765 ], [ 121.024873480279766, 24.780175850569982 ], [ 121.02490019336183, 24.780076531000599 ], [ 121.025031965376996, 24.779891421739023 ], [ 121.02552312182236, 24.779489563958911 ], [ 121.025954914849137, 24.778992914031306 ], [ 121.026092933772659, 24.778895832061693 ], [ 121.02649483800235, 24.778803217828504 ], [ 121.026763556477789, 24.778794141389948 ], [ 121.026997362810874, 24.77882569969114 ], [ 121.02733023827426, 24.778936330547076 ], [ 121.027537465654589, 24.778963378528257 ], [ 121.027845108697733, 24.778884230665529 ], [ 121.027977049986788, 24.778769090789758 ], [ 121.027970677046554, 24.778608833447947 ], [ 121.027731999259942, 24.778202588589238 ], [ 121.027548308576527, 24.777687989410445 ], [ 121.027493045959162, 24.777243338494856 ], [ 121.027574757019323, 24.777101122208258 ], [ 121.027668848754828, 24.777037904290353 ], [ 121.028202596663348, 24.776803059768909 ], [ 121.028561218410147, 24.776703676625669 ], [ 121.028811705558994, 24.776728457433638 ], [ 121.02902511578057, 24.776796221397003 ], [ 121.029483660542553, 24.777130191928951 ], [ 121.029621801878193, 24.777123302890946 ], [ 121.029702598864091, 24.777044286185074 ], [ 121.029722148651743, 24.776732884105659 ], [ 121.029558217911799, 24.776150478191049 ], [ 121.02940175870522, 24.77579839152855 ], [ 121.029081309656391, 24.775243282200066 ], [ 121.028723251517874, 24.774428424966445 ], [ 121.028233251105718, 24.773643025135001 ], [ 121.028166147676586, 24.773451178832634 ], [ 121.028147236647058, 24.773193955973738 ], [ 121.028210099981706, 24.773085600268889 ], [ 121.028467498126076, 24.772959150371353 ], [ 121.029075973844428, 24.772909285575917 ], [ 121.029381279535812, 24.772823544038939 ], [ 121.029704485675666, 24.772647331187894 ], [ 121.030120683375443, 24.77234704521274 ], [ 121.030351160358322, 24.772092029397466 ], [ 121.030351128510276, 24.771961023581849 ], [ 121.030115353571446, 24.771396870335671 ], [ 121.029925116384064, 24.771268159797408 ], [ 121.029503280867075, 24.771227614525248 ], [ 121.029296029102326, 24.771026857837558 ], [ 121.029258301783031, 24.77091617385372 ], [ 121.029283147945705, 24.770789767770612 ], [ 121.029390039027575, 24.7706476357368 ], [ 121.029327227208483, 24.770308983029846 ], [ 121.029433872259204, 24.769880191046482 ], [ 121.029452671717706, 24.769667923545235 ], [ 121.029174563301524, 24.769042743207599 ], [ 121.029155378104335, 24.768934403007162 ], [ 121.029237202366645, 24.768652331669745 ], [ 121.02948141265469, 24.768361019167962 ], [ 121.029603428253324, 24.768166878865067 ], [ 121.029684492755095, 24.767948008043927 ], [ 121.029737544899149, 24.767532679030928 ], [ 121.029753320544515, 24.766954841439421 ], [ 121.029847481882797, 24.76658230003013 ], [ 121.030048264305094, 24.766261742301598 ], [ 121.030201189191871, 24.766115086032766 ], [ 121.030508141556851, 24.765907364538919 ], [ 121.030869194905208, 24.765794341969467 ], [ 121.031266416553706, 24.765740087593922 ], [ 121.0315267111027, 24.765557202565784 ], [ 121.031657443320057, 24.765410549467568 ], [ 121.031824897462272, 24.765293141332197 ], [ 121.031988194557641, 24.765223044104381 ], [ 121.032844413300666, 24.764983599173135 ], [ 121.032974032242123, 24.76494294170017 ], [ 121.033106882026786, 24.76484811140439 ], [ 121.03337683188343, 24.76438090830128 ], [ 121.033522130916253, 24.764046815183413 ], [ 121.03355249036268, 24.763760057915505 ], [ 121.033438208953015, 24.763378712547325 ], [ 121.033363871001868, 24.763290609322997 ], [ 121.033068715986744, 24.763089877188602 ], [ 121.032999605325685, 24.762904714440428 ], [ 121.032967062179239, 24.7625345461893 ], [ 121.032910462014328, 24.762333670748017 ], [ 121.032773347474588, 24.762071869396433 ], [ 121.03257753631901, 24.761853057153306 ], [ 121.032294897059273, 24.761652140156471 ], [ 121.031876614159245, 24.76148303246255 ], [ 121.031199844845233, 24.761293572855212 ], [ 121.030566668884589, 24.761192040549112 ], [ 121.030511651643323, 24.761142394075296 ], [ 121.03032243263722, 24.760693256109754 ], [ 121.030195090848792, 24.760555594590713 ], [ 121.029933305927472, 24.76031413015788 ], [ 121.029086172073349, 24.759641751224468 ], [ 121.028902408704624, 24.759364064812239 ], [ 121.028687686761984, 24.758844957366712 ], [ 121.028494038862036, 24.7585718769386 ], [ 121.028216653203813, 24.758319126560231 ], [ 121.027749240714769, 24.758039144376362 ], [ 121.027389854139855, 24.757885714006914 ], [ 121.027208470854745, 24.757847375187065 ], [ 121.026978277986217, 24.757856445487146 ], [ 121.026649373056713, 24.757919714101178 ], [ 121.026435859622254, 24.757897171209752 ], [ 121.026329084820773, 24.757804646093167 ], [ 121.026297999060404, 24.757653412216648 ], [ 121.026254272515501, 24.757626324830888 ], [ 121.025872516647439, 24.757617362562897 ], [ 121.024979641169267, 24.757312868515907 ], [ 121.02457315992956, 24.757265444897993 ], [ 121.024219014906308, 24.757015029034992 ], [ 121.023857934219535, 24.756852561765839 ], [ 121.023664345799233, 24.756800587290343 ], [ 121.023278885810115, 24.756791618996402 ], [ 121.022518335347058, 24.75691814572474 ], [ 121.021710903777972, 24.756681334371422 ], [ 121.021118246139764, 24.756579747147399 ], [ 121.020867036903368, 24.756568496497088 ], [ 121.020622169829508, 24.756606902274566 ], [ 121.020350587842088, 24.756737864245917 ], [ 121.020146530499261, 24.756920740576469 ], [ 121.020006906371606, 24.757157771062751 ], [ 121.0197559965887, 24.758065249441575 ], [ 121.019360460788292, 24.758900498602117 ], [ 121.019260079149092, 24.759175904147103 ], [ 121.019128398479168, 24.7598644024912 ], [ 121.018858484469746, 24.760857653850699 ], [ 121.018725939305227, 24.761986254340698 ], [ 121.018733130027982, 24.762541606927194 ], [ 121.018291756614019, 24.763866528326162 ], [ 121.018017570881455, 24.76424569337145 ], [ 121.01784176165701, 24.7643360101175 ], [ 121.017615721844152, 24.764308941837957 ], [ 121.017477602338161, 24.764354110382218 ], [ 121.017308132522004, 24.764485054763966 ], [ 121.016937691773961, 24.764882376514244 ], [ 121.016937703407763, 24.76496815787571 ], [ 121.01706968400191, 24.765232339734645 ], [ 121.017101070803847, 24.765505101189625 ], [ 121.017057063162753, 24.765706003052696 ], [ 121.016920981413435, 24.765981501132526 ], [ 121.016438237436432, 24.766645107598535 ], [ 121.015989912902882, 24.767071787608465 ], [ 121.015814111275176, 24.767288512266941 ], [ 121.015052376286135, 24.768460132037394 ], [ 121.013763087659953, 24.77067439076621 ], [ 121.013592841410201, 24.77090916952524 ], [ 121.012229222175478, 24.771823465896375 ], [ 121.011682907589019, 24.77222519451805 ], [ 121.010782929060085, 24.772776010143346 ], [ 121.010312006442774, 24.773162018405234 ], [ 121.010074391077794, 24.773450951596022 ], [ 121.009777594018672, 24.773742145438597 ], [ 121.009433967251468, 24.773868568666455 ], [ 121.008975542817581, 24.774103341899366 ], [ 121.00853595945415, 24.774229768781346 ], [ 121.00818862569659, 24.774446475910555 ], [ 121.008082168651669, 24.774475824823988 ], [ 121.007810844321597, 24.774514301293362 ], [ 121.007390099167196, 24.774498432213679 ], [ 121.00693438793914, 24.774304337914426 ], [ 121.006799954696561, 24.774272743784056 ], [ 121.006241068863261, 24.774457855557976 ], [ 121.004401052881946, 24.775265985560146 ], [ 121.00392391830465, 24.775518801145015 ], [ 121.002988183835825, 24.776170971435743 ], [ 121.00011846640983, 24.777954358677768 ], [ 120.999821013470012, 24.778186774155859 ], [ 120.999603447804446, 24.778310917688252 ], [ 120.999025845045935, 24.778561478159347 ], [ 120.997713262811004, 24.779003614929493 ], [ 120.996515408756252, 24.779626568670672 ], [ 120.996067909377913, 24.779915474358873 ], [ 120.995552418376974, 24.780127633180861 ], [ 120.994655878959833, 24.780351062917006 ], [ 120.993072484325566, 24.780585462996509 ], [ 120.992978227248088, 24.780574172795724 ], [ 120.992934345020132, 24.780540313300929 ], [ 120.992771028284025, 24.780310156231817 ], [ 120.992243374383918, 24.779720929237342 ], [ 120.991515180340414, 24.7788206430873 ], [ 120.990793045281265, 24.777621875474402 ], [ 120.990574284947357, 24.777143316226777 ], [ 120.99048698915044, 24.777034957850638 ], [ 120.99031594955521, 24.776915407529369 ], [ 120.989970611820524, 24.776825089244269 ], [ 120.989794769570125, 24.77681821558782 ], [ 120.989480788620853, 24.776858822797166 ], [ 120.989041174816265, 24.776996577534941 ], [ 120.988344110947438, 24.777398056143557 ], [ 120.988186191351417, 24.777429725307201 ], [ 120.985817491303422, 24.776932943833557 ], [ 120.985562320193495, 24.776136059578839 ], [ 120.985461892095643, 24.776068334962527 ], [ 120.984959564507022, 24.776032170738848 ], [ 120.984718687098322, 24.775939683911833 ], [ 120.985191415372498, 24.775384387934857 ], [ 120.985180924064949, 24.775260242900718 ], [ 120.984262712995545, 24.774680058159184 ], [ 120.98421250778766, 24.774587509160288 ], [ 120.984206270324449, 24.774341558903973 ], [ 120.984105859579785, 24.774185722715039 ], [ 120.983710210498742, 24.773761333375564 ], [ 120.98322672902124, 24.773305260628906 ], [ 120.98322056255121, 24.773208192849818 ], [ 120.983327186145914, 24.773122513776151 ], [ 120.983496308110702, 24.773041355854325 ], [ 120.983777217593328, 24.772960128633542 ], [ 120.985179695934931, 24.77301887900083 ], [ 120.985412082932356, 24.77298053002465 ], [ 120.985851680937103, 24.772831599355428 ], [ 120.986136752220901, 24.772815907122766 ], [ 120.986240898067265, 24.772768435018058 ], [ 120.986362834631691, 24.772495329280076 ], [ 120.986388053010501, 24.772204157357251 ], [ 120.986499663574094, 24.771696386684017 ], [ 120.98656116851204, 24.771592481382015 ], [ 120.986781209723006, 24.771373555985342 ], [ 120.986875327806985, 24.771168162265809 ], [ 120.986921900987753, 24.770529388665096 ], [ 120.987003512760595, 24.770213392658942 ], [ 120.98747212535875, 24.769351195462338 ], [ 120.98788036893599, 24.768994596913153 ], [ 120.988099953680106, 24.768678611344313 ], [ 120.98828831535333, 24.768502567272979 ], [ 120.988366362070352, 24.768265652216868 ], [ 120.988353867031535, 24.768064682236581 ], [ 120.988018588953793, 24.768066994216337 ], [ 120.987108048502492, 24.768405412213252 ], [ 120.986856816482302, 24.768432476366723 ], [ 120.986524013165024, 24.76840995639547 ], [ 120.986128482605196, 24.768353409887673 ], [ 120.98520177829802, 24.768132118959361 ], [ 120.98449846467561, 24.768150105148731 ], [ 120.984182044444694, 24.768082357095363 ], [ 120.983987377669038, 24.767996564112391 ], [ 120.983477873238655, 24.767565236616857 ], [ 120.983157453620478, 24.76738461862821 ], [ 120.982909314824155, 24.767404905014708 ], [ 120.982416582632013, 24.767510943810588 ], [ 120.98217168974459, 24.767510914862537 ], [ 120.982052416720123, 24.76747477693549 ], [ 120.981895456902222, 24.767366414081764 ], [ 120.981805238955985, 24.767262654774054 ], [ 120.981604754952045, 24.766833651367588 ], [ 120.981411208961291, 24.766504153445354 ], [ 120.980663090098048, 24.765578467053992 ], [ 120.980614293076016, 24.765404929786634 ], [ 120.980602370303345, 24.764581107560439 ], [ 120.980467868094095, 24.764145339511433 ], [ 120.980319877844849, 24.763996338096888 ], [ 120.97978430533405, 24.76349513958727 ], [ 120.97964311052246, 24.76337773874868 ], [ 120.979497427920435, 24.763307836986723 ], [ 120.979032696839852, 24.763273824868367 ], [ 120.97873775425208, 24.763285069132632 ], [ 120.978709938219978, 24.763314408354884 ], [ 120.978693685903792, 24.763490474107392 ], [ 120.978674830402014, 24.763531100431805 ], [ 120.978637131499383, 24.763535609394637 ], [ 120.978329547541463, 24.763386429672092 ], [ 120.977387764115932, 24.763095115914112 ], [ 120.977205612660072, 24.763077030971392 ], [ 120.97707381904543, 24.763106354033294 ], [ 120.976932735094877, 24.763250791073709 ], [ 120.976836762261243, 24.76340426362863 ], [ 120.976782654596988, 24.763571285615317 ], [ 120.976778612476778, 24.763708972176879 ], [ 120.976881925868696, 24.76395953368867 ], [ 120.976880210956196, 24.764052077267262 ], [ 120.976740811999363, 24.764252943539031 ], [ 120.976533599821579, 24.764401884231887 ], [ 120.976421429590047, 24.764399699738238 ], [ 120.976088368779401, 24.764171582809276 ], [ 120.975773981542574, 24.764051902452472 ], [ 120.975378319309314, 24.763970579935425 ], [ 120.97505819370798, 24.763977298477986 ], [ 120.974888536048439, 24.764051756641479 ], [ 120.974687636853162, 24.764282044133882 ], [ 120.974656258701756, 24.764356435045936 ], [ 120.974633635036525, 24.764685977559115 ], [ 120.974555575377835, 24.764859856439397 ], [ 120.974386057531319, 24.764997424425754 ], [ 120.974210232941445, 24.765004256044769 ], [ 120.973937707297495, 24.764925117760672 ], [ 120.973794660532803, 24.764825777473806 ], [ 120.973368974912233, 24.764252382056849 ], [ 120.973290805846901, 24.764204967637077 ], [ 120.973112824651039, 24.764184621296543 ], [ 120.972998644512842, 24.764204915260667 ], [ 120.972621778333902, 24.764378648699083 ], [ 120.972295260183614, 24.764629134171827 ], [ 120.971855718363656, 24.764554565735597 ], [ 120.971629661976365, 24.764642642880567 ], [ 120.971398165916682, 24.764872739567423 ], [ 120.971290440809327, 24.765030810905941 ], [ 120.97115218115708, 24.76561530016653 ], [ 120.971108288698602, 24.765673978032254 ], [ 120.971039221285892, 24.765696536358305 ], [ 120.970857071241795, 24.765655872037364 ], [ 120.970557387859756, 24.765427929916804 ], [ 120.970260781046647, 24.765265355342066 ], [ 120.969821249481171, 24.765152318827187 ], [ 120.969702006931442, 24.765014607600307 ], [ 120.969643507789257, 24.764782107601967 ], [ 120.969462194945933, 24.764475096087647 ], [ 120.969390869318985, 24.764256136359613 ], [ 120.969108368968762, 24.763926532018417 ], [ 120.968930462413155, 24.763610491862064 ], [ 120.968743988907775, 24.762958131800541 ], [ 120.968616427188365, 24.762122835876756 ], [ 120.968309986601156, 24.76176828773816 ], [ 120.968209004262903, 24.761524474194523 ], [ 120.968095561680343, 24.761075336923891 ], [ 120.967900475661921, 24.760890388073083 ], [ 120.967603889642632, 24.760687260392707 ], [ 120.967530540492589, 24.760540429290643 ], [ 120.967461982479648, 24.758608152099448 ], [ 120.967430650065126, 24.758488506335969 ], [ 120.967273735478727, 24.758276379564517 ], [ 120.967210897268785, 24.758127293387105 ], [ 120.967240132464639, 24.757989603470179 ], [ 120.967581490990611, 24.757691713399531 ], [ 120.967631725267964, 24.757605942820593 ], [ 120.967656956993181, 24.757416337065628 ], [ 120.967644482075102, 24.757262837865056 ], [ 120.967472496715374, 24.75679779674919 ], [ 120.967387152135558, 24.756447889914298 ], [ 120.966489411787805, 24.755811260412386 ], [ 120.966319939698749, 24.755766079030153 ], [ 120.966081229224798, 24.755804306774355 ], [ 120.965812020086517, 24.75607293901329 ], [ 120.965669081332209, 24.756169874317486 ], [ 120.96551549860348, 24.756212725262912 ], [ 120.965315120522234, 24.756194621659755 ], [ 120.965095475288578, 24.756004968447009 ], [ 120.964737654147058, 24.755460906878767 ], [ 120.964618419582891, 24.755329962949766 ], [ 120.964448759097266, 24.755214897440869 ], [ 120.964285672339727, 24.755192196677644 ], [ 120.964178906653714, 24.755219257225026 ], [ 120.963953280411374, 24.755422438645557 ], [ 120.963821006784386, 24.755501317405535 ], [ 120.963708134963369, 24.755546433495862 ], [ 120.963576342833875, 24.75555317302517 ], [ 120.962901625184514, 24.755088120896971 ], [ 120.962735117590711, 24.754943620736825 ], [ 120.96267675140966, 24.754821628772365 ], [ 120.962703839870485, 24.754652347804036 ], [ 120.962835712340436, 24.754365810319257 ], [ 120.962829546202684, 24.754320665397238 ], [ 120.962333638866127, 24.753699729602658 ], [ 120.962076472616886, 24.753275316803556 ], [ 120.961888178269007, 24.752828349372056 ], [ 120.961601482519612, 24.75161843293051 ], [ 120.961478306558632, 24.751270797064343 ], [ 120.961411273042955, 24.751223469523755 ], [ 120.961034627686175, 24.751216510266001 ], [ 120.960934065533223, 24.751178202472381 ], [ 120.960852563967165, 24.750959145370903 ], [ 120.960563893408647, 24.750735700077893 ], [ 120.960305887353115, 24.75027282167261 ], [ 120.959151629058695, 24.74954795964247 ], [ 120.958574174737379, 24.749227210618457 ], [ 120.958261900205727, 24.749362563268583 ], [ 120.957608464638724, 24.74961519204291 ], [ 120.957495374115624, 24.749626355579185 ], [ 120.957420153759671, 24.749569995239384 ], [ 120.95727392541815, 24.749346385348694 ], [ 120.957213113845725, 24.749179328312501 ], [ 120.957167076797575, 24.748269711275398 ], [ 120.957405704161246, 24.747994296028789 ], [ 120.95753773435861, 24.74772119768641 ], [ 120.957588057292512, 24.747382618140911 ], [ 120.957516450779309, 24.746872729858133 ], [ 120.957569350736492, 24.746683124353762 ], [ 120.957730131832889, 24.746362633318174 ], [ 120.957780423113704, 24.746123369205954 ], [ 120.957780566450865, 24.745698993809572 ], [ 120.957730266876766, 24.745507201256469 ], [ 120.957672362193563, 24.745419064912198 ], [ 120.957491811282921, 24.745279060108146 ], [ 120.956744713283285, 24.745233693892676 ], [ 120.956496151420524, 24.745197507198466 ], [ 120.956328863242021, 24.745127576496785 ], [ 120.956167175267311, 24.744946937457772 ], [ 120.955941292245811, 24.744567648211817 ], [ 120.955772179103306, 24.744414101650513 ], [ 120.955451590549856, 24.744481631599221 ], [ 120.955068631588617, 24.744425087979756 ], [ 120.954899208984443, 24.7442805690293 ], [ 120.95474236437208, 24.743966747682531 ], [ 120.954564641747609, 24.743711624379547 ], [ 120.954347038421858, 24.743517423352188 ], [ 120.954225634894414, 24.743449671145132 ], [ 120.954001643496369, 24.743404459120672 ], [ 120.953851007665051, 24.743431498892061 ], [ 120.953543482199436, 24.743702228505679 ], [ 120.953122780070132, 24.743803670295058 ], [ 120.952983867196266, 24.743882627828377 ], [ 120.952789914997808, 24.744074426534162 ], [ 120.95263927422377, 24.744119522462725 ], [ 120.952494847702198, 24.744074333308681 ], [ 120.952344138349872, 24.743889287606351 ], [ 120.952243750878736, 24.743814678673846 ], [ 120.952095773227896, 24.743762806771663 ], [ 120.951963838964076, 24.743773960124816 ], [ 120.951894769315942, 24.743814567080847 ], [ 120.951471276389668, 24.744331413360335 ], [ 120.951351974691974, 24.744428342814146 ], [ 120.951169963224544, 24.744498255973944 ], [ 120.950735686436488, 24.744536485798797 ], [ 120.950416518471428, 24.744531866212878 ], [ 120.949142046764436, 24.744423094926482 ], [ 120.948909694125831, 24.744434301770234 ], [ 120.948784455458366, 24.744497459855051 ], [ 120.948715211441865, 24.744576437209684 ], [ 120.948614641681203, 24.744944412126472 ], [ 120.948539359582853, 24.74505941179201 ], [ 120.948407384322948, 24.745161029455208 ], [ 120.948135764911299, 24.745221789074165 ], [ 120.947930148151684, 24.745196979178736 ], [ 120.947647782554014, 24.745097565248066 ], [ 120.947183182985341, 24.74484676585951 ], [ 120.946812900166336, 24.744783434102633 ], [ 120.9465868673297, 24.744817301594956 ], [ 120.946467417746291, 24.744884883858777 ], [ 120.946105274059136, 24.745293302226425 ], [ 120.94598383328497, 24.745315830230595 ], [ 120.945814370055118, 24.745286516114088 ], [ 120.945531851759938, 24.745189265030376 ], [ 120.945356093001777, 24.745074085283068 ], [ 120.944916818381742, 24.744507374288311 ], [ 120.944772540456469, 24.744473553901408 ], [ 120.944533844128543, 24.744495947197876 ], [ 120.944347552673435, 24.744446310643585 ], [ 120.944161003419936, 24.74428137740302 ], [ 120.943942531434786, 24.74399237780068 ], [ 120.943806107523784, 24.743676322582683 ], [ 120.943766961604311, 24.7434663908621 ], [ 120.94370842432906, 24.742391927616033 ], [ 120.943624886288219, 24.741954067881888 ], [ 120.94365636202528, 24.741358140888423 ], [ 120.943361606387214, 24.740653755645962 ], [ 120.943192226899157, 24.740102905125475 ], [ 120.943041745199096, 24.73978222103721 ], [ 120.943191974125611, 24.739299297047758 ], [ 120.943202402891444, 24.739125399303326 ], [ 120.94316141609751, 24.738888362459416 ], [ 120.942995147511169, 24.738642258344335 ], [ 120.942602848279748, 24.738434430599067 ], [ 120.94244587486412, 24.737894905816042 ], [ 120.942288997782185, 24.737730071794257 ], [ 120.941898454824894, 24.737429798033354 ], [ 120.941736831156845, 24.73718362205166 ], [ 120.941730554154304, 24.737057217847873 ], [ 120.941894071937554, 24.736558445756401 ], [ 120.941919360107377, 24.735996419074603 ], [ 120.941902722015016, 24.73589258259107 ], [ 120.941750064071158, 24.735635205434239 ], [ 120.94172773562957, 24.73515216133293 ], [ 120.941690113685027, 24.734998658807644 ], [ 120.941133619745443, 24.734486143868256 ], [ 120.940740058229224, 24.734063815814196 ], [ 120.940604695110608, 24.73382901602292 ], [ 120.940457759845742, 24.733400067335722 ], [ 120.940401255163579, 24.733330153705637 ], [ 120.940106297112578, 24.733142591292548 ], [ 120.940037286956382, 24.733061296362827 ], [ 120.939926921572763, 24.732882926287793 ], [ 120.939861673985817, 24.732688864287791 ], [ 120.939889574601168, 24.732492392847227 ], [ 120.939981217467633, 24.732406656880414 ], [ 120.940935575624152, 24.732045860634152 ], [ 120.941092567268726, 24.731944349477217 ], [ 120.941532302821969, 24.731393734528449 ], [ 120.941739544816741, 24.73119290846137 ], [ 120.942329981158096, 24.730430165979694 ], [ 120.942330039438048, 24.73030375509444 ], [ 120.941953606788374, 24.729603839984325 ], [ 120.941816587533168, 24.729183933961234 ], [ 120.941765458905934, 24.728854366301697 ], [ 120.941812256558222, 24.728536212811814 ], [ 120.941705559465703, 24.728450308361733 ], [ 120.941432948325783, 24.728400634535308 ], [ 120.940908244672556, 24.728357452045788 ], [ 120.940688578337358, 24.728393480157589 ], [ 120.940604354987329, 24.728474705192681 ], [ 120.940527274214404, 24.72880422246801 ], [ 120.940315244427879, 24.729014145957809 ], [ 120.939621137966142, 24.729528522428737 ], [ 120.939354616611851, 24.729650221154934 ], [ 120.938965520960878, 24.729776474204833 ], [ 120.938670464346984, 24.729821497350677 ], [ 120.93841297201763, 24.729810105936288 ], [ 120.938254517016262, 24.729749087980899 ], [ 120.938172989115003, 24.729685853447005 ], [ 120.938027422907837, 24.729487152795738 ], [ 120.938067976049666, 24.729322377601559 ], [ 120.938432095969361, 24.72910367169219 ], [ 120.938532709744976, 24.728990763844845 ], [ 120.938664583121721, 24.728753814281134 ], [ 120.93887836473219, 24.728117377682633 ], [ 120.938950205303513, 24.727767634790585 ], [ 120.938916276838867, 24.727659276472956 ], [ 120.938884774563434, 24.727643373111057 ], [ 120.938445497421156, 24.727607078614451 ], [ 120.9381253388392, 24.72752117412907 ], [ 120.937905760434518, 24.727383395564374 ], [ 120.937857594040679, 24.727331460537549 ], [ 120.937849297791004, 24.727241170010878 ], [ 120.937968606124556, 24.727114817482367 ], [ 120.938609015168424, 24.726783366228144 ], [ 120.938740984938818, 24.726661442325874 ], [ 120.938951391397282, 24.726289093838663 ], [ 120.939274963680802, 24.725395382840922 ], [ 120.93920599447263, 24.72523969991499 ], [ 120.938828271262693, 24.725056624629385 ], [ 120.938681593316957, 24.724934677123013 ], [ 120.938643952461746, 24.724837603076388 ], [ 120.938666437874261, 24.724666057716693 ], [ 120.938813698875464, 24.724223683873507 ], [ 120.938847154141826, 24.724034085521271 ], [ 120.938826519412672, 24.723587219005957 ], [ 120.938858026365651, 24.723277890067475 ], [ 120.938913846516442, 24.723151501789435 ], [ 120.939087252074231, 24.722932607939672 ], [ 120.939110796401025, 24.722797177756117 ], [ 120.939002006768661, 24.722585040018927 ], [ 120.938629294153273, 24.722295951047457 ], [ 120.93845995497577, 24.722099407795014 ], [ 120.93831202195048, 24.721717947001466 ], [ 120.93828917523409, 24.721381509594504 ], [ 120.938333283991028, 24.721196420997241 ], [ 120.93851536230865, 24.720927882401984 ], [ 120.938707911440247, 24.720720282664271 ], [ 120.938846153929276, 24.72039303003864 ], [ 120.938601565177621, 24.719957357701453 ], [ 120.938570266441587, 24.719848991244096 ], [ 120.93859549147048, 24.719745072 ], [ 120.938698281613938, 24.719582588088212 ], [ 120.938752591839815, 24.719379545369062 ], [ 120.938704706116752, 24.719076955389383 ], [ 120.938595918932904, 24.718873836949811 ], [ 120.938370064459178, 24.718668241649063 ], [ 120.938206913782281, 24.718462753105481 ], [ 120.93817776174933, 24.718388254157361 ], [ 120.938170635305113, 24.718119628749477 ], [ 120.938521349135002, 24.717246190014869 ], [ 120.938628363861312, 24.716650302107375 ], [ 120.938220450611951, 24.716386026500544 ], [ 120.937950742305176, 24.716169216826252 ], [ 120.936696010921466, 24.714997188727121 ], [ 120.936426108196514, 24.71487067246418 ], [ 120.936145986815205, 24.714798323707765 ], [ 120.936049645095736, 24.714739595966563 ], [ 120.935999527465086, 24.714590600650975 ], [ 120.936169417081146, 24.71427918204763 ], [ 120.936064772698145, 24.713845758708523 ], [ 120.935434520741012, 24.712604039038222 ], [ 120.935164536479448, 24.71294701419761 ], [ 120.935093929686616, 24.712998898841516 ], [ 120.93495104482291, 24.713050752131281 ], [ 120.934618363438702, 24.713079950878733 ], [ 120.934274693438923, 24.713158802064765 ], [ 120.933983555436839, 24.71319704632252 ], [ 120.933645494493419, 24.713183444385827 ], [ 120.933235287256025, 24.713219377300732 ], [ 120.932903295138544, 24.713417861145068 ], [ 120.932520287299042, 24.713704261088417 ], [ 120.931691454436489, 24.714195951471321 ], [ 120.931091352240671, 24.714663003765676 ], [ 120.93081999659924, 24.714953964911807 ], [ 120.930657668825191, 24.715249670923924 ], [ 120.930552144356227, 24.715601742279922 ], [ 120.93037086679837, 24.716508999618345 ], [ 120.9302806095546, 24.716621916025087 ], [ 120.930142544502601, 24.716612823074566 ], [ 120.929823143062563, 24.716359851754888 ], [ 120.92897811230489, 24.715409027641471 ], [ 120.928835016790515, 24.715284905186746 ], [ 120.928665575224528, 24.715318592133894 ], [ 120.928477099033387, 24.715422332698818 ], [ 120.928069032533244, 24.715749455844797 ], [ 120.927968652875549, 24.715735954885712 ], [ 120.927899646982709, 24.7156861644518 ], [ 120.927515623395621, 24.715293302225128 ], [ 120.927404004325524, 24.715221009447767 ], [ 120.927026330008658, 24.715069495800329 ], [ 120.926725044932468, 24.715022038440939 ], [ 120.926549269969101, 24.715058067372798 ], [ 120.92634207685802, 24.715206858443086 ], [ 120.92621019823271, 24.715184312116651 ], [ 120.926047167546145, 24.715084906867631 ], [ 120.925863083455297, 24.715071182639871 ], [ 120.92565731939213, 24.715152348341579 ], [ 120.925331470654328, 24.715377913586593 ], [ 120.925180704287527, 24.715429762648416 ], [ 120.925048966372046, 24.71542969688867 ], [ 120.924923426409009, 24.715395767380549 ], [ 120.924668686287234, 24.715251171105677 ], [ 120.924239984256971, 24.714950732165093 ], [ 120.92385180798469, 24.71457131124598 ], [ 120.923738779741029, 24.714541991743467 ], [ 120.923393453947099, 24.714559882280025 ], [ 120.923023231766763, 24.714622893831859 ], [ 120.92260768298469, 24.714814459123485 ], [ 120.922405747092171, 24.714956656499165 ], [ 120.921986058480584, 24.715346867842335 ], [ 120.921935661556091, 24.715428109145492 ], [ 120.921916734361687, 24.715565787291176 ], [ 120.921998116145531, 24.715960863245826 ], [ 120.921948313601803, 24.716076052843757 ], [ 120.921787844687358, 24.716084997988119 ], [ 120.921521054202799, 24.715949418823328 ], [ 120.921313972852502, 24.715908590819808 ], [ 120.921150712113501, 24.715931167186636 ], [ 120.921062752150306, 24.716064213295045 ], [ 120.92103767797694, 24.7161499819696 ], [ 120.920980910495601, 24.716533690731623 ], [ 120.920867951534632, 24.716630698952891 ], [ 120.919763033915643, 24.716928077831781 ], [ 120.919461697841299, 24.716957259690385 ], [ 120.919285964145871, 24.71692339783106 ], [ 120.918865498660239, 24.716681490259592 ], [ 120.918125172479833, 24.716353887242491 ], [ 120.917816066399951, 24.716229483040529 ], [ 120.917704572173378, 24.716213621659275 ], [ 120.917504243319854, 24.716245202434767 ], [ 120.916519491210963, 24.716544772297873 ], [ 120.915909377575844, 24.71665729052382 ], [ 120.915094634207264, 24.716762919047422 ], [ 120.914798339839166, 24.716880124395445 ], [ 120.914387752852335, 24.717227586567571 ], [ 120.914239389285541, 24.717261079623679 ], [ 120.913876608374025, 24.7172608717846 ], [ 120.913762308320813, 24.717281211021756 ], [ 120.913655538450257, 24.717355555266206 ], [ 120.913642966493995, 24.71744583520465 ], [ 120.913680612842157, 24.717497871313199 ], [ 120.914182461155278, 24.717847949814768 ], [ 120.914314192163033, 24.71797006628627 ], [ 120.914395702387907, 24.718250003043995 ], [ 120.914370401621724, 24.718432820112714 ], [ 120.914263431885686, 24.718685463750205 ], [ 120.914308648782921, 24.718848105791178 ], [ 120.914470307338348, 24.719139374135878 ], [ 120.914903246683593, 24.719541398202885 ], [ 120.915606836450507, 24.720081351709744 ], [ 120.916000927910332, 24.720544222301239 ], [ 120.916161823144975, 24.720828734864693 ], [ 120.91622795701845, 24.721013869474259 ], [ 120.916276597400298, 24.72126220430895 ], [ 120.916263767460478, 24.721508328895677 ], [ 120.916144369422526, 24.72175422238621 ], [ 120.915899380270218, 24.72203399336345 ], [ 120.914801554423235, 24.722943160935294 ], [ 120.914699212538423, 24.723082966526722 ], [ 120.914616110200669, 24.723319940954163 ], [ 120.914371749296365, 24.723574971055768 ], [ 120.914038268377112, 24.723829760092983 ], [ 120.913830953904011, 24.724116411003443 ], [ 120.913744542245553, 24.724445846019059 ], [ 120.913750204329702, 24.72496926157898 ], [ 120.913781551897529, 24.725204044076531 ], [ 120.913994351044508, 24.72593327955488 ], [ 120.913978473765212, 24.726558544518799 ], [ 120.91417419720969, 24.726967232705011 ], [ 120.914174130619472, 24.727064300285509 ], [ 120.913798926838126, 24.727109228617188 ], [ 120.913660810897255, 24.727158897333485 ], [ 120.913654573538139, 24.727244585188487 ], [ 120.913784785233929, 24.727459100889451 ], [ 120.913756370184558, 24.727675791535741 ], [ 120.913696637531842, 24.727838282891938 ], [ 120.913545228404701, 24.728124965401399 ], [ 120.913233213373815, 24.728363973634345 ], [ 120.913107541377968, 24.728506111987823 ], [ 120.912954901275725, 24.729226198009432 ], [ 120.91294356924972, 24.729607581901437 ], [ 120.912874170754947, 24.730117699397166 ], [ 120.912660245896078, 24.730995760634109 ], [ 120.912264021227642, 24.731918677825618 ], [ 120.912042687001176, 24.732340757232297 ], [ 120.911665545730003, 24.732909379670851 ], [ 120.910539796881039, 24.734375595686672 ], [ 120.909900122121059, 24.735032095437653 ], [ 120.909284665053221, 24.73551252943351 ], [ 120.909009833309838, 24.735762927232731 ], [ 120.908587236047865, 24.736349571408457 ], [ 120.908463239118291, 24.736710661558007 ], [ 120.908379382218968, 24.737313402000133 ], [ 120.908635907623804, 24.738658635018918 ], [ 120.908706320278199, 24.739541196307872 ], [ 120.908668238316892, 24.740073901922418 ], [ 120.90862990839355, 24.740310990003277 ], [ 120.908554828169102, 24.740532065844874 ], [ 120.908150919779828, 24.740883964852586 ], [ 120.907841055971375, 24.741071128983716 ], [ 120.907696593858063, 24.741104987968193 ], [ 120.907439558617796, 24.741084424643866 ], [ 120.907043886432419, 24.7409510879185 ], [ 120.905895071417788, 24.740701982898916 ], [ 120.905763876864782, 24.740349754548834 ], [ 120.905688738812302, 24.740227901257121 ], [ 120.905236021944432, 24.739749068155973 ], [ 120.904773643474158, 24.739387600494311 ], [ 120.904343771482729, 24.739242804582048 ], [ 120.903818917086937, 24.738960231921446 ], [ 120.903523257738712, 24.738747867726218 ], [ 120.903266854562858, 24.738512956553482 ], [ 120.903128892090336, 24.738330126774262 ], [ 120.903018918866479, 24.738014033438514 ], [ 120.902970562088257, 24.737950801312074 ], [ 120.901780244590711, 24.736746781501719 ], [ 120.901466704292289, 24.73629746151348 ], [ 120.901096040794201, 24.736204574033884 ], [ 120.900832455533106, 24.736077998219507 ], [ 120.899775341134372, 24.735176710208442 ], [ 120.89954036163067, 24.735018451488791 ], [ 120.89932055004914, 24.734925759932644 ], [ 120.899212216805637, 24.734797109515199 ], [ 120.899041479909357, 24.734476358623638 ], [ 120.898863816877252, 24.734318317991534 ], [ 120.89867205407198, 24.734214268242162 ], [ 120.898209983380852, 24.734098830370499 ], [ 120.897998054428129, 24.733911422183226 ], [ 120.897877472157404, 24.733748814562361 ], [ 120.897419568439602, 24.73345055503998 ], [ 120.896653953750189, 24.733179168425789 ], [ 120.896315029018126, 24.733025446612327 ], [ 120.895938503079407, 24.73295512309004 ], [ 120.895518055704457, 24.732760713742735 ], [ 120.895260787163622, 24.732679275989405 ], [ 120.894538904354889, 24.732577197164687 ], [ 120.893729344609255, 24.732316960284191 ], [ 120.893564519296262, 24.732332643593825 ], [ 120.893352546978875, 24.732569505273904 ], [ 120.892549152291963, 24.73277660975543 ], [ 120.892467212067899, 24.732862323618267 ], [ 120.892441828684312, 24.733101583888853 ], [ 120.892379388866956, 24.733144425385941 ], [ 120.892322863747239, 24.733133098935326 ], [ 120.892256021412848, 24.733085740557385 ], [ 120.89179658970086, 24.732432951055191 ], [ 120.891046929159742, 24.731773277290941 ], [ 120.890958119654542, 24.731766531499048 ], [ 120.890897854753788, 24.731793573750505 ], [ 120.890497115283821, 24.73204149854265 ], [ 120.890252191328159, 24.732151921000032 ], [ 120.889460332441431, 24.732763078566521 ], [ 120.888945469999328, 24.732972624292881 ], [ 120.888568489478203, 24.733243223487971 ], [ 120.888261143210457, 24.733371752963393 ], [ 120.887482419846535, 24.733869662829257 ], [ 120.887344345173986, 24.733851501763692 ], [ 120.887269002589335, 24.733810816017122 ], [ 120.886923604001112, 24.733395488843932 ], [ 120.886421571946002, 24.733246126924691 ], [ 120.885574356217504, 24.73305135682995 ], [ 120.88506601006749, 24.732883928167549 ], [ 120.884877809674421, 24.732782292242241 ], [ 120.884802900971181, 24.732777630076217 ], [ 120.88468973584375, 24.732881472384179 ], [ 120.884532646470944, 24.733127022243295 ], [ 120.883897543838799, 24.734232618874078 ], [ 120.883708739065909, 24.734449170182828 ], [ 120.883614456537998, 24.73451230689524 ], [ 120.883463867412388, 24.734494123513766 ], [ 120.88326930357907, 24.734426256976853 ], [ 120.882055321697777, 24.733714252309209 ], [ 120.881785591256843, 24.733576343306034 ], [ 120.881039167827311, 24.733273273704423 ], [ 120.880768623898874, 24.733505565694099 ], [ 120.878515018011683, 24.735212255795066 ], [ 120.878903796078873, 24.73572272736811 ], [ 120.879173371111577, 24.736020909649959 ], [ 120.880264827337783, 24.736945302732327 ], [ 120.880359864392943, 24.737069532088466 ], [ 120.8804807195677, 24.7374918369954 ], [ 120.880590547840526, 24.73765210245061 ], [ 120.881007601874813, 24.737995551238452 ], [ 120.881970547506825, 24.738923784256649 ], [ 120.882176036439887, 24.739174573186212 ], [ 120.882417024155188, 24.739541119362848 ], [ 120.88251793239445, 24.739746727462681 ], [ 120.882669175362253, 24.739964951852038 ], [ 120.882756975748237, 24.740068859447902 ], [ 120.882932474983789, 24.740224037172954 ], [ 120.88318933678687, 24.740410138154747 ], [ 120.883333577410241, 24.740615580815771 ], [ 120.883440046139057, 24.740909113922342 ], [ 120.883523914796967, 24.741586366475847 ], [ 120.883551223211612, 24.742845690223614 ], [ 120.883480547792416, 24.743653557784317 ], [ 120.883487639245018, 24.743775649112383 ], [ 120.883522255274855, 24.743876896549622 ], [ 120.883633892020171, 24.744023726396112 ], [ 120.884152234865184, 24.744755839195282 ], [ 120.884302724735463, 24.744893651818863 ], [ 120.885118606702505, 24.745088784208029 ], [ 120.885432392575808, 24.745226621450708 ], [ 120.885710275235496, 24.745434511268211 ], [ 120.886129908314075, 24.745886291671436 ], [ 120.886351342671986, 24.74605088099662 ], [ 120.886404437015742, 24.746070323875443 ], [ 120.886443390293337, 24.746063888859492 ], [ 120.886464667001704, 24.7460283319861 ], [ 120.886447019807818, 24.745966887490823 ], [ 120.886454118233971, 24.745947490238912 ], [ 120.886493062665437, 24.745950752003608 ], [ 120.886605757930099, 24.746019924751984 ], [ 120.886737271418212, 24.746060878960371 ], [ 120.886829320994551, 24.746067413025553 ], [ 120.886914324914173, 24.746038377754878 ], [ 120.886990498853123, 24.745966900990172 ], [ 120.887560063532703, 24.746054022722276 ], [ 120.887654249889124, 24.746196692295335 ], [ 120.888129085809325, 24.746748076708617 ], [ 120.888622264485932, 24.747326468965269 ], [ 120.888914938816555, 24.74758107817642 ], [ 120.889115361841149, 24.748046239550227 ], [ 120.8892031512149, 24.748177229309878 ], [ 120.889328749560534, 24.748347729340743 ], [ 120.889587996544407, 24.748595405588571 ], [ 120.889814863982224, 24.748906014534231 ], [ 120.890525805529066, 24.749747159353713 ], [ 120.891598614935432, 24.750763755305719 ], [ 120.891717102675997, 24.750948838484618 ], [ 120.892031353854094, 24.751285383295098 ], [ 120.892740318849164, 24.751811902880952 ], [ 120.893462038164714, 24.752410476961785 ], [ 120.893700340995451, 24.752686020681207 ], [ 120.89425252374815, 24.75320781713306 ], [ 120.89480155199648, 24.753815508082539 ], [ 120.895042599035975, 24.75414307475436 ], [ 120.895206674539679, 24.754456628894062 ], [ 120.895412554906343, 24.754768514637984 ], [ 120.895475130106092, 24.754951397883257 ], [ 120.895501888919043, 24.755210656721292 ], [ 120.895529374963829, 24.755299156841978 ], [ 120.895592411707625, 24.755376305609715 ], [ 120.89565437958386, 24.755454780820305 ], [ 120.895682868584004, 24.755624738255822 ], [ 120.895711389401825, 24.75575548419819 ], [ 120.895785300117325, 24.755947087846131 ], [ 120.895844743614816, 24.7560605834203 ], [ 120.897049085784261, 24.757647526853873 ], [ 120.897165189892007, 24.75786080950801 ], [ 120.897241485963832, 24.757926229395729 ], [ 120.897300063500481, 24.757938801347237 ], [ 120.897375080477033, 24.757943746285484 ], [ 120.897484859583031, 24.757913322604246 ], [ 120.897689996572595, 24.757974460488569 ], [ 120.897909394004245, 24.758105336196241 ], [ 120.898404731252995, 24.758334675971092 ], [ 120.898793817599255, 24.758650960649536 ], [ 120.898956889413142, 24.758944430104318 ], [ 120.899220347064926, 24.759287714873249 ], [ 120.899458462399508, 24.759637834918578 ], [ 120.899521065756289, 24.759793621374588 ], [ 120.899617164026651, 24.760181918340582 ], [ 120.899604416065685, 24.760473084196018 ], [ 120.898529738341182, 24.762672924949385 ], [ 120.898076399244658, 24.763442364631597 ], [ 120.897808858284449, 24.763733464968468 ], [ 120.897774546716505, 24.763936505126242 ], [ 120.89779927065041, 24.764498592100306 ], [ 120.897606538510303, 24.765825474477754 ], [ 120.897527894735433, 24.766200137020032 ], [ 120.897406463833121, 24.766496717474084 ], [ 120.897296557291043, 24.766675292164571 ], [ 120.89726786030019, 24.766753704414967 ], [ 120.897243820619693, 24.766971558403853 ], [ 120.897175336577305, 24.767283397260933 ], [ 120.897052248660458, 24.767588138146095 ], [ 120.896856475470116, 24.767938622214281 ], [ 120.896747771859609, 24.768068650220368 ], [ 120.896641604193519, 24.768086625275746 ], [ 120.896534226650616, 24.768075364639742 ], [ 120.896421162777614, 24.768027786749901 ], [ 120.896289458327004, 24.76791482841633 ], [ 120.896132678151929, 24.767666422770553 ], [ 120.895938337593421, 24.76725329015143 ], [ 120.895744070884817, 24.766749681160498 ], [ 120.895631451877875, 24.766541934636901 ], [ 120.895550256209788, 24.766308062952209 ], [ 120.895435891538838, 24.766107547007209 ], [ 120.89524267955386, 24.765647772161486 ], [ 120.895205015767388, 24.765602593506927 ], [ 120.895129771644235, 24.765602540848139 ], [ 120.89506878975206, 24.765688983641031 ], [ 120.895047889772385, 24.765774046025921 ], [ 120.895049541459741, 24.765880693668052 ], [ 120.895066563331696, 24.765986241551911 ], [ 120.895130384512086, 24.766216273193123 ], [ 120.895301872128144, 24.766586757625447 ], [ 120.895316155466105, 24.766625997114822 ], [ 120.895292264876517, 24.766660831025181 ], [ 120.895215891382833, 24.76668256376313 ], [ 120.895065984747177, 24.766674811551962 ], [ 120.894986796685998, 24.766721614775975 ], [ 120.894938971262874, 24.766843594481085 ], [ 120.894928245486355, 24.766938730921137 ], [ 120.894959367187511, 24.767229944913201 ], [ 120.894934792506263, 24.767421795608143 ], [ 120.894851638075963, 24.767638443009716 ], [ 120.894738549495187, 24.767803235824864 ], [ 120.894593975813422, 24.767924939720324 ], [ 120.89409773129988, 24.768245034639712 ], [ 120.893438014894812, 24.768564993624977 ], [ 120.893180437461851, 24.768759016460741 ], [ 120.892947974603871, 24.769034134091772 ], [ 120.892794260570241, 24.769247100326822 ], [ 120.892715276867847, 24.769401885143523 ], [ 120.892652204772574, 24.76961852757934 ], [ 120.892581259494705, 24.770293458631894 ], [ 120.892588339906425, 24.771047265674525 ], [ 120.892820043370079, 24.771850981411703 ], [ 120.892844516516774, 24.771974673347685 ], [ 120.89282601259265, 24.772097016346585 ], [ 120.892724893061171, 24.772340582013442 ], [ 120.892643477340044, 24.772671658350408 ], [ 120.892519286610138, 24.772797925191941 ], [ 120.892352180571763, 24.772884949672964 ], [ 120.892002712758398, 24.773019694399551 ], [ 120.89185181519187, 24.773121067496252 ], [ 120.891759768555517, 24.773245235174116 ], [ 120.891669880706147, 24.773730369624204 ], [ 120.891537773425412, 24.774075709985748 ], [ 120.891361413830751, 24.774757172618646 ], [ 120.891310862831361, 24.775136366085288 ], [ 120.891379343779406, 24.775818213800488 ], [ 120.891441804697138, 24.776134279659065 ], [ 120.891742876998592, 24.776597152352128 ], [ 120.891987404553632, 24.777051045285976 ], [ 120.892100273977832, 24.77733103260957 ], [ 120.892269118895669, 24.778105414329499 ], [ 120.89233804186668, 24.778279274260804 ], [ 120.892407031192732, 24.778376381732951 ], [ 120.892701975309919, 24.778611356076681 ], [ 120.892859097848159, 24.778826007129542 ], [ 120.892902679081061, 24.778938526131114 ], [ 120.893154617159681, 24.780308892375402 ], [ 120.893177661255748, 24.780647500800203 ], [ 120.893158376218054, 24.781150860666628 ], [ 120.893070226115313, 24.781414903428562 ], [ 120.89288155777777, 24.781764655322192 ], [ 120.892824823533019, 24.781970025225078 ], [ 120.892824472632441, 24.782378597834107 ], [ 120.892905413104131, 24.783134849094353 ], [ 120.89291742305447, 24.783725989464802 ], [ 120.892873144476027, 24.784184188037436 ], [ 120.892690405794127, 24.784820711227848 ], [ 120.892658665784026, 24.785249476284456 ], [ 120.892696100602279, 24.785565532325712 ], [ 120.89280260490537, 24.785886233391768 ], [ 120.892808822084277, 24.786023843213687 ], [ 120.892745680401433, 24.786310565369746 ], [ 120.892626523068444, 24.786506771413734 ], [ 120.892512958675283, 24.78702370540265 ], [ 120.892537268082634, 24.787687272958674 ], [ 120.892492995881582, 24.788168033716563 ], [ 120.892505314250201, 24.788398272588783 ], [ 120.892617838600501, 24.788908470834397 ], [ 120.892873025529056, 24.789389518377117 ], [ 120.892893481493005, 24.789682873107605 ], [ 120.89294373269577, 24.78983197168353 ], [ 120.893313436488626, 24.790669550437087 ], [ 120.893485361520774, 24.791299419498973 ], [ 120.893494918191749, 24.791511689270607 ], [ 120.893708103650752, 24.792143844521068 ], [ 120.893625749808251, 24.79266961306076 ], [ 120.893619295977274, 24.792990124597569 ], [ 120.893869873461583, 24.793633682137465 ], [ 120.893875898200619, 24.793999255316713 ], [ 120.893806312097695, 24.794595094976927 ], [ 120.894803122449872, 24.796776300941918 ], [ 120.894878195253455, 24.797004236025401 ], [ 120.895009626252744, 24.797658903095705 ], [ 120.89534913510893, 24.798801260948945 ], [ 120.895807264312992, 24.799300411664234 ], [ 120.896296476286608, 24.800154045925304 ], [ 120.896522388914505, 24.800388946298966 ], [ 120.896677090886385, 24.800486020517273 ], [ 120.896814520333535, 24.800540287032952 ], [ 120.896949105615874, 24.800568991456103 ], [ 120.897211637622746, 24.800573523812936 ], [ 120.897478895452409, 24.800634713503342 ], [ 120.897740576217487, 24.800746323717231 ], [ 120.897954047384403, 24.800888670121903 ], [ 120.89817545524734, 24.801066540189513 ], [ 120.898248997561154, 24.80118681523988 ], [ 120.899026981897691, 24.802370144763895 ], [ 120.899240013012928, 24.802873759911549 ], [ 120.899276534165637, 24.803019343783788 ], [ 120.899276266613455, 24.80335050405467 ], [ 120.899303584236421, 24.803578079563959 ], [ 120.899371229803876, 24.803830935214073 ], [ 120.899447614424474, 24.803964998238218 ], [ 120.900098933360155, 24.804899037985514 ], [ 120.900262059652476, 24.805197108992363 ], [ 120.900432503450702, 24.805623851389662 ], [ 120.900500201685389, 24.805811249090073 ], [ 120.900548526225435, 24.8061618350063 ], [ 120.900588956222265, 24.806341838153163 ], [ 120.900806981785308, 24.806992042625509 ], [ 120.900969831025435, 24.807644386110873 ], [ 120.901148468216391, 24.808079339993494 ], [ 120.90129214906365, 24.808533916826782 ], [ 120.901357863056134, 24.808889885854747 ], [ 120.901453098222603, 24.809190601168133 ], [ 120.901505906389133, 24.809511485471198 ], [ 120.90164649284209, 24.809784611990064 ], [ 120.901815628170169, 24.810312896422381 ], [ 120.901915052739341, 24.810572082564239 ], [ 120.90201994767915, 24.810733375071774 ], [ 120.902091702372715, 24.810868336467479 ], [ 120.902298525419909, 24.811435097764921 ], [ 120.902398429580444, 24.812152855577509 ], [ 120.902405323484672, 24.812384940273471 ], [ 120.90235740426796, 24.812615833531879 ], [ 120.902347558140505, 24.812967653617509 ], [ 120.902352184158488, 24.813186609225227 ], [ 120.902409916433768, 24.813471038775567 ], [ 120.902480655964183, 24.813722612671501 ], [ 120.90266648812046, 24.814167157485006 ], [ 120.90284268347115, 24.814724968582567 ], [ 120.902875718097022, 24.81521735560991 ], [ 120.902925774490072, 24.815554750686317 ], [ 120.902992312951298, 24.815857269922798 ], [ 120.903067412565775, 24.81608079444441 ], [ 120.903375843895802, 24.816673035203188 ], [ 120.903475868187471, 24.816969391224124 ], [ 120.903518650031543, 24.817204713061201 ], [ 120.903587922016129, 24.817376905961307 ], [ 120.903732127205529, 24.817589089580746 ], [ 120.904033436610192, 24.81792110214063 ], [ 120.904233926156124, 24.818264010274131 ], [ 120.904500989604898, 24.818630191222706 ], [ 120.904908660553446, 24.819072879162995 ], [ 120.905457831286498, 24.81989486542005 ], [ 120.905796832331959, 24.820267599065708 ], [ 120.906198765685119, 24.820936211280031 ], [ 120.906417936703718, 24.821243076924624 ], [ 120.906585090229868, 24.821428809263672 ], [ 120.906989131649425, 24.821794177317123 ], [ 120.90713845869017, 24.821991210763084 ], [ 120.907329252056527, 24.822217892562247 ], [ 120.907535210856025, 24.822453603051848 ], [ 120.907893165860074, 24.822711048477299 ], [ 120.908104409353101, 24.822792435745605 ], [ 120.90825503522683, 24.822907642748859 ], [ 120.908393107289896, 24.823063470561664 ], [ 120.909112324203818, 24.824355015656906 ], [ 120.909275637757418, 24.82445903387665 ], [ 120.909438744854484, 24.824635117978961 ], [ 120.909614439641544, 24.824933185724831 ], [ 120.909765178032487, 24.825111600389548 ], [ 120.909884262307955, 24.825457033710354 ], [ 120.910147775493414, 24.825949376649046 ], [ 120.910417516874617, 24.826380590273693 ], [ 120.910693528500502, 24.826906787851932 ], [ 120.910881784438658, 24.827159718609984 ], [ 120.910900610308317, 24.827204872753327 ] ] ] }
print json.loads(c)


# In[45]:

import numpy as np
import numpy.linalg as LA
import random
import MySQLdb
import json

def getDocDistance(a, b):
    if LA.norm(a)==0 or LA.norm(b)==0:
        return -1
    return round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 4)

#test sample
my_randoms = []
for each in range(26):
    my_randoms.append(random.random())

def getRecommendCluster(a):
    db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
    cursor = db.cursor()
    sql = "SELECT clusterVector FROM project.cluster;"

    cursor.execute(sql)
    results = cursor.fetchall()

    tmpCom = []
    for row in results:
        vec = json.loads(row[0])
        tmpCom.append(getDocDistance(vec, a))

    #print ('max value:', max(tmpCom))
    return [i for i, j in enumerate(tmpCom) if j == max(tmpCom)][0]


# In[19]:

import requests as rs
import time
import string
from bs4 import BeautifulSoup as bs
#joblist3 = open('joblist3.txt', 'w')

#f= open("20160217worklist.txt","w")

for line in open('20160217.txt'):
    try:
        w = rs.get(line)
        wedsite = bs(w.text)
        main = wedsite.select('.main')[0]
        cont = main.select('.content')[0]
        cont2 = main.select('.content')[1]
        #日期
        jobdate = main.select('.update')[0].text.encode('utf-8').split()[0]
        jobdate = jobdate[15:]
        #職稱
        job_title = main.select('.header.static')[0]
        title = job_title.select('.center')
        test = job_title.select('h1')[0].text.strip().encode('utf-8')[0]
        jobtitle1 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[0]
        jobtitle2 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[1]
        jobtitle3 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[2]
        jobtitle4 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[3]
        jobtitle5 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[4]
        jobtitle6 = job_title.select('h1')[0].text.strip().encode('utf-8').split(' ')[5]
        jobtitle = jobtitle1 + jobtitle2 + jobtitle3 + jobtitle4 + jobtitle5 + jobtitle6
        #公司名
        companyname = main.select('.cn')[0].text.encode('utf-8')
        #公司屬性
        companyaddr = main.select('.company a')[0]['href']
        res = rs.get(companyaddr)
        res.encoding ='utf-8'
        soup = bs(res.text)
        company_addr = soup.select('#cont_main')[0]
        companytype = company_addr.select('.intro')[0]
        companytype = companytype.select('dd')[0].text.encode('utf-8')   
        #工作性質
        jobtype = cont.select('dd')[2].text.encode('utf-8')
        #工作待遇
        salary = cont.select('dd')[1].text.encode('utf-8')
        #工作地址
        addr = cont.select('dd')[3].text.strip().encode('utf-8').split()[0]
        #工作經歷
        jobexp = cont2.select('dd')[1].text.encode('utf-8')
        #工作內容
        #jobcont = cont.select('p')[0].text.encode('utf-8')
        #jobcontent = "".join(jobcont.split('\<br\>'))
        #擅長工具
        tool = cont2.select('dd')[5].text.strip().encode('utf-8')
        #工作技能
        skill = cont2.select('dd')[6].text.strip().encode('utf-8')
        #其他條件
        other = cont2.select('dd')[7].text.strip().encode('utf-8')
        content = tool + skill + other
        
        total = '"' + '104人力銀行' + '",' + '"'+ jobdate + '",' + '"'+ jobtitle+ '",' +'"'+companyname + '",' + '"'+companytype+ '",' + '"'+addr + '",'+ '"'+jobtype + '",' + '"'+jobexp + '",' + '"'+salary + '",' +'"'+ content + '",' + '"'+line
        #f.write(total)
        print jobtitle1+'\n'

    except Exception as detail:
        print line,detail
        
        
#f.close()


# In[6]:

def matchskill(selectskill):
    import cPickle as pickle
    import MySQLdb
    import json
    #連MySQL取26個技能start==============
    db = MySQLdb.connect("10.120.26.46","yang","iiizb104","project" )
    cursor = db.cursor()
    sql = "SELECT dict FROM project.dict where no = '1';"

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    resultdic = cursor.fetchall()
    dic = resultdic[0]
    list_skill = json.loads(dic[0])
    db.close()
    #連MySQL取26個技能start==============
    #set_skill = pickle.load(file('JsonToArray/set_skill_v2_300.data'))
    
    #print list_skill
    #print "--------------------------"
    a = []
    for i in list_skill:
        if i in selectskill:
            a.append(1)
        else:
            a.append(0)
    return a
    print a

