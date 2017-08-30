import billboard



f=open('C:\\Users\\BSE\\Desktop\\csgraduation\\realchart.txt','w')

for i in range(0,20):
    chart=billboard.ChartData('hot-100', date=str(1998+i)+'-08-26', fetch=True)

    for j in range(0, 100):
        song=chart[j]
        f.write(song.artist+"\n")
        f.write(song.title+"\n")
    
f.close()
