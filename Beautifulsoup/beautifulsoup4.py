# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

URL = "https://www.owleyes.org/list/genre/fiction"

R = requests.get(URL)

Soup = BeautifulSoup(R.text, "html.parser")


List = Soup.find("ul", {"class":"no-bullet books--horizontal" })

bookList=[]
urlList=[]
for book in List:
     if book.find('span') != -1 and book.find('a')!= -1:
       bookList.append(book.find('span').text)
       urlList.append(book.find('a')['href'])
       
def try_one_page(url):
    chapterList=[]
    urlList=[]
    full_url = "https://www.owleyes.org{url}/read#".format(url=url)
    R = requests.get(full_url)
    #print(R.text)
    Soup = BeautifulSoup(R.text, "html.parser")
    tmp1 = Soup.find("ol", {"class":"toc-chapters no-bullet"})
  
    for j,i in enumerate(tmp1):
        
        if i.find('a') != -1:  
            #print(i.find('a'))
            chapterList.append(i.find("span").text.lstrip().rstrip())
            urlList.append(i.find('a'))
            
                
    
    #print(list1)            
    #print(chapterList)
    #print(urlList)
    return urlList[1:],chapterList
            
deneme = try_one_page('/text/alice-adams-booth-tarkington')

chapter_name_list= deneme[1]
chapter_url_list=[]
for i in range(len(deneme[0])):
    chapter_url_list.append(deneme[0][i]['href'])
    

def get_contents(url):
    full_url = "https://www.owleyes.org{url}/read#".format(url=url)
    R = requests.get(full_url)
    Soup = BeautifulSoup(R.text, "html.parser")
    tmp_contents= Soup.find('div',{'id':'chapter-body'})
    list_content = []
    for i in tmp_contents:
        if i.find('p') != -1:
            #print(i.find('p').text)
            list_content.append(i.find('p').text)
    return ''.join(list_content)
            




def get_all_chapter_contents(url,chapter_name_list,chapter_url_list):
    this_dict={}
    for i in range(len(chapter_name_list)):
        tmp_url = ''
        tmp_content= ''
        if i == 0:
            tmp_url= url
            tmp_content = get_contents(tmp_url)
            this_dict[chapter_name_list[i]]= tmp_content
        if i !=0:
            tmp_url=chapter_url_list[i-1]
            tmp_content= get_contents(tmp_url)
            this_dict[chapter_name_list[i]]= tmp_content
    return this_dict

                
                

            
        


    
    
