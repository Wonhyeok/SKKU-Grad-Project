from bs4 import BeautifulSoup
import urllib.request
import re
import sys; sys.getdefaultencoding()



# 함수

def get_text(URL):
        source_code_from_URL= urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        text=''
        lyric=''
        title=''
            
        for item in soup.find_all('title'):
            title=title+str(item.find_all(text=True))

#클래스로 가져오는 법
        for item in soup.find_all('p',class_='songtext'):
            lyric = lyric+str(item.find_all(text=True))

        text='Title: '+str(title)+'\nLyric \n'+str(lyric)+'\n'
        
        return text
    
#텍스트 클리닝 함수
    
def clean_text(text):
    
    cleaned_text = re.sub('',
                          '', text)
    '''cleaned_text = re.sub('\'n',
                          '', cleaned_text)
    cleaned_text = re.sub('\',',
                          '', cleaned_text)
    cleaned_text = re.sub(' n',
                         '', cleaned_text)'''
    print(cleaned_text)

    return cleaned_text

# 파일명
def get_song(URL):
        source_code_from_URL= urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        song=''
        

        
        for item in soup.find_all('h1'):
            song=song+str(item.find_all(text=True))
        song = re.sub('[\{\}\[\]\/?.,;|\)*~`!^\-_+<>@\#$%&\\\=\(\"\' ]',
                          '', song)
        return song


 
# 메인
def main():
    f=open('C:\\Users\\BSE\\Desktop\\csgraduation\\weblyric\\lyriclist.txt','r')
    URLS=f.readlines()
    for URL in URLS:
        result_text=get_text(URL)
        s=get_song(URL)
        cleaned_text = clean_text(result_text)
        OUTPUT_FILE_NAME= str(s) + '.txt'
        open_output_file= open(OUTPUT_FILE_NAME, 'w',encoding='UTF8')
        open_output_file.write(cleaned_text)
    f.close()
    open_output_file.close()

if __name__=='__main__':
    main()






