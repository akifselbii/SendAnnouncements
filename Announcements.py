#Mehmet Akif SELBİ

import requests
from bs4 import BeautifulSoup
import String as st
  
def WebsiteLink(facultyNo,departmentNo):
    
    if(st.departmentTagList[facultyNo][departmentNo] == "!"):
        r = requests.get('http://'+st.facultyTagList[facultyNo]+'.comu.edu.tr/arsiv/duyurular')
        source = BeautifulSoup(r.content,"html.parser")
        linkTag = st.facultyTagList[facultyNo]
    elif(st.departmentTagList[facultyNo][departmentNo] == "?"):
        r = requests.get('http://'+st.facultyTagList[facultyNo]+'.comu.edu.tr/arsiv/duyurular')
        source = BeautifulSoup(r.content,"html.parser")
        linkTag = st.facultyTagList[facultyNo]
    else:
        r = requests.get('http://'+st.departmentTagList[facultyNo][departmentNo]+'.'+st.facultyTagList[facultyNo]+'.comu.edu.tr/arsiv/duyurular')
        source = BeautifulSoup(r.content,"html.parser")
        linkTag = st.departmentTagList[facultyNo][departmentNo]+'.'+st.facultyTagList[facultyNo]

    return source,linkTag
    
def Links(facultyNo,departmentNo):
    source,linkTag = WebsiteLink(facultyNo,departmentNo)
    sourceLink = source.find_all("a")
    flag=0
    dLink=[]
    for i in sourceLink:
        if(i.text == "Duyurular"):flag = 1
        if(i.text == "İlk"):flag = 0
        if(flag == 1):
            if(i.get("href")!= "arsiv/duyurular"):
                try:
                    if(i.get("href")[0] == "/"):
                        dLink.append("http://"+linkTag+".comu.edu.tr"+i.get("href"))     
                except:
                    continue
    return dLink

def Titles(facultyNo,departmentNo):
    dTitle=[]
    source,linkTag = WebsiteLink(facultyNo,departmentNo)
    sourceTitle = source.find_all("td")
    for i in sourceTitle:
        dTitle.append(i.text)
    return dTitle

def Body(dLink):
    dLinkText=[]
    for i in range(len(dLink)):
        r = requests.get(dLink[i])
        source = BeautifulSoup(r.content,"html.parser")
        sourceLink = source.find_all("p")
        _list=[]
        for j in sourceLink:
            _list.append(j.text)
        body = _list[1]
        if "Paylaş" in body:
            body = body.replace("Paylaş","")
        dLinkText.append((body+st.annoouncementLink+dLink[i]))
        
    return dLinkText

