import pylast


# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account/create for Last.fm
API_KEY = "fdbefce9b70a10ef7baf2ee2da06ed87"  
API_SECRET = "1dcb34a48af9dde1199e4b554d0f9d3c"

# In order to perform a write operation you need to authenticate yourself
username = "stylepixels"
password_hash = pylast.md5("hot15959.")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

f20 = open("C:/Users/BSE/Desktop/csgraduation/traindata6.txt", 'w')
f21 = open("C:/Users/BSE/Desktop/csgraduation/traintar6.txt", 'w')

def try_track(artist,title,bpm,score):
        for i in range (0, int(len(artist))):
        #for i in range (0, 10):
               try:
                   get_track(i,artist,title,bpm,score)
                   i+=1
               except Exception:
                   get_track(i+1,artist,title,bpm,score)
                   i+=1

def get_track(i,artist,title,bpm,score):
        #print(i,artist[i].strip("\n"),title[i].strip("\n"),bpm[i],score[i])
        result = network.get_track(artist[i].strip("\n"),title[i].strip("\n")).get_top_tags()
        tagreturn=tag_search(result)
        #print("tagreturn: ", tagreturn)
        if(tagreturn!=0):
            f20.write(str(bpm[i].strip("\n"))+","+str(score[i].strip("\n"))+"\n")
            f21.write(str(tagreturn)+"\n")
        

def tag_search(result):
    
    tag_weight = {}
    count=[0,0,0,0,0]
    
    f1 = open("C:/Users/BSE/Desktop/csgraduation/d1.txt", 'r')
    f2 = open("C:/Users/BSE/Desktop/csgraduation/d2.txt", 'r')
    f3 = open("C:/Users/BSE/Desktop/csgraduation/d3.txt", 'r')
    f4 = open("C:/Users/BSE/Desktop/csgraduation/d4.txt", 'r')

    l1 = f1.readlines()
    l2 = f2.readlines()
    l3 = f3.readlines()
    l4 = f4.readlines()
    
    for tag in result:
        tag_weight[str(tag.item.get_name())] = str(tag.weight)
        
        for line in l1:
            if (str(line)== (str(tag.item.get_name())+"\n")):
                count[1]=count[1]+int(tag.weight)
                print('count1: ', count[1])
                print('tagitem: ', str(tag.item.get_name()))
        for line in l2:
            if (str(line)== (str(tag.item.get_name())+"\n")):
                count[2]=count[2]+int(tag.weight)
                print('count2: ', count[2])
                print('tagitem: ', str(tag.item.get_name()))
        for line in l3:
            if (str(line)== (str(tag.item.get_name())+"\n")):
                count[3]=count[3]+int(tag.weight)
                print('count3: ', count[3])
                print('tagitem: ', str(tag.item.get_name()))
        for line in l4:
            if (str(line)== (str(tag.item.get_name())+"\n")):
                count[4]=count[4]+int(tag.weight)
                print('count4: ', count[4])
                print('tagitem: ', str(tag.item.get_name()))

    #print('tag result: ',sorted(tag_weight.items(), key=lambda x: x[1], reverse=True) )
                
    if(max(count)==0):
        #print('dimension zero')
        return 0
    else:
        return count.index(max(count))
        
    f1.close()
    f2.close()
    f3.close()
    f4.close()
        
def main():
        
        artist=[]
        title=[]
        bpm=[]
        score=[]
        
        f5 = open("C:/Users/BSE/Desktop/csgraduation/fullchart9.txt", 'r')
        l5=f5.readlines()
        
        for line in l5:
            if(l5.index(line)%4==0):
                artist.append(line)
            elif(l5.index(line)%4==1):
                title.append(line)
            elif(l5.index(line)%4==2):
                bpm.append(line)
            else:
                score.append(line)
       
        #for i in range (0, int(len(l5)/4)):
        try_track(artist,title,bpm,score)

        f5.close()


       

if __name__=='__main__':
    main()

f20.close()
f21.close()
        
'''       
f1.close()
f2.close()
f3.close()
f4.close()    
'''
#print(sorted(tag_weight.items(), key=lambda x: x[1], reverse=True))

