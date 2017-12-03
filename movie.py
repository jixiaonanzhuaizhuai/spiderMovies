import requests
import re #正则模块

#翻页下载
for i in range(1, 167):
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_'+str(i)+'.html'
    html = requests.request('GET', url)
    html.encoding = 'gb2312'
    #print(html.text)
    detail_list = re.findall('<a href="(.*?)" class="ulink">',html.text)
    for j in detail_list:
        b_url = 'http://www.dytt8.net/'+j
        b_html = requests.get(b_url) #请求电影的详细信息
        b_html.encoding = 'gb2312'
        #<a href="ftp://ygdy8:ygdy8@yg45.dydytt.net:7082/[阳光电影www.ygdy8.net].
        # 全球风暴.HD.720p.韩版中英双字幕.rmvb">ftp://ygdy8:ygdy8@yg45.dydytt.net:7082/[阳光电影www.ygdy8.net].全球风暴.HD.720p.韩版中英双字幕.rmvb</a>
        ftp = re.findall('<a href="(.*?)">.*?</a></td>',b_html.text)
        #print(ftp)
        try:
            with open(r'dytt_movie_url.txt','a',encoding='utf-8') as file:
                file.write(ftp[0]+'\n')
        except:
            print('这一页没有匹配到')