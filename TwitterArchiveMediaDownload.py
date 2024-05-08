import csv
import os
import wget

path=os.path.split(os.path.realpath(__file__))[0]
files=os.listdir(path)
for file in files:
    if not os.path.isdir(file):
        if file.find(".csv")!=-1:
            csvfile=file
line=0
with open(csvfile, 'r',encoding='utf_8_sig') as file:
    reader = csv.reader(file)
    for row in reader:
        line=line+1
        if line!=1:
            mediaurlcol=row[14]
            if mediaurlcol!="":
                os.mkdir(str(line))
                mediaurlcol2=mediaurlcol.split(',')
                medianum=1
                for mediaurl in mediaurlcol2:
                    if mediaurl!="":
                        while 1:
                            try:
                                mediafilename=wget.filename_from_url(mediaurl)
                                wget.download(mediaurl,".\\"+str(line)+"\\"+str(medianum)+"--"+mediafilename)
                                break
                            except:
                                print("\nLine "+str(line)+" download failed, retry. ")
                        medianum=medianum+1

