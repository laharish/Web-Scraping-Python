import os
import shutil

def file(name, year):

    for file in os.listdir('C:/Users/Admin1/Downloads'):
        if file.endswith(".TXT"):
            i=0;
            count = 0
            list=[]
            org_file = 'C:/Users/Admin1/Downloads/'+file
            with open(org_file, 'r') as myFile:
                 for num, line in enumerate(myFile, 1):
                    if 'LENGTH:' in line:
                        list.append(num)
                        i=i+1
            num_lines = open(org_file).read().count('\n')
            data = myFile.read().splitlines(True)
            for num in range(0,i):
                new_file =  "L:/"+name+"/"+str(year)+"/"+str(num+1)+".txt"
                with open(new_file, 'w') as fout:
                    if(num==i-1):
                        fout.writelines(data[list[num]:num_lines-8])
                    else:
                     fout.writelines(data[list[num]:list[num+1]-24])


        print(i)

def name(cname):
    for file in os.listdir('C:/Users/Admin1/Downloads'):
        if file.endswith(".TXT"):
            c = 'C:/Users/Admin1/Downloads/'+file
            shutil.move(c, "L:/Scraping/"+cname+'2'+".txt")