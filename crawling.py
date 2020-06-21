import urllib.request,urllib.error,urllib.parse
import re
import itertools
import lxml.html
import cssselect
import csv
import urllib.robotparser

def download(url,user_agent='wswp',retries=2):
    print('download:',url)
    headers={'user agent':user_agent}
    try:
        html=urllib.request.urlopen(url).read()
        html = html.decode('utf-8')
        print(html)
    except urllib.request.URLError as e:
        print('dowmload error:',e.reason)
        html=None
        if retries> 0:
            if hasattr(e,'code') and 500<= e.code<600:
                return download(url,user_agent,retries-1)

    return html


def carwl_sitemap(url):
    sitemap=download(url)
    sitemap =sitemap.decode('utf-8')
    links=re.findall('<loc>(.*?)</loc>',sitemap)

    for link in links:
        html=download(link)

# max_error=5
# num_error=0
# for page in itertools.count(1):
#     url='http://example.webscraping.com/view/-%d' %(page)
#     html=download(url)
#     if html is None:
#         num_error+=1
#         if num_error==max_error:
#             break
#     else:
#         num_error=0


rp=urllib.robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()

def link_crawling(seed_url,regex):

    crawl_queue = [seed_url]

    seen=set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()

        html=download(url)



        for link in get(html):
                print(get(html))
                print('ook')

                if re.search(regex,link):
                    link=urllib.parse.urljoin(seed_url,link)
                    if link not in seen:
                        seen.add(link)
                        crawl_queue.append(link)


def get(html):
    web_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)

    return  web_regex.findall(html)

#

#
#
#html=download('http://example.webscraping.com/places/default/view/united-kingdom-239')
# #
# # tree=lxml.html.fromstring(html)
# # td=tree.cssselect('tr#places_area__row>td.w2p_fw')[0]
# # area=td.text_content()
# # print(area)
# FIELDS=['area']
# def callback(url,html):
#     if re.search('/view/',url):
#         tree=lxml.html.fromstring(html)
#         row=[tree.cssselect('table>tr#places_%s__row>td.w2p_fw' %(field))[0].text_content() for field in FIELDS]
#         print(url ,row)
#url='http://example.webscraping.com/places/default/view/united-kingdom-239'
# callback(url,html)


class scrapecallback:
    def __init__(self):
        self.writer=csv.writer(open('count.csv','w'))
        self.fields=('area','population','iso','country','capital','continent','tld','currency_code','currency_name','phone')
        self.writer.writerow(self.fields)

    def __call__(self, url,html):
        if re.match('http://example.webscraping.com/places/default/view/', url):
            tree=lxml.html.fromstring(html)
            row=[]
            for field in self.fields:
                row.append(tree.cssselect('table>tr#places_{}__row>td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)



link_crawling('https://www.taobao.com/','')

# x=scrapecallback()
# x(url,html)
