import csv
def ortalama(list):
    top,index=0,0
    leng = len(list)
    for i in range(leng):
        top = list[i] + top
        index=index+1
    a = top // index
    return a

def cokluhisto(list,dictionary):
    for element in list:
        for i in element:
            if int(i) not in dictionary:
                dictionary[int(i)]=1
            else:
                dictionary[int(i)]=dictionary[int(i)]+1
    return  dictionary
def histo(array):
    dic = dict()
    for i in array:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]=dic[i]+1
    return dic

with open("input_dir_name/input_hw_2.csv", "r") as file:
    reader = csv.reader(file,delimiter = ';')
    mainarray= []
    for row in reader:
        stri = str(row[3])
        splited1=  stri.split()
        stri2= splited1[0]
        splited2= stri2.split("-")
        mainarray.append(splited2)
aylar = []
for i in mainarray:
    aylar.append(i[1])
a = histo(aylar)
toplam,index = 0,0
values=[]
for key, value in a.items():
    print(f"{key}. ay {value} kişi ayrıldı")
    toplam=toplam+value
    index=index+1
    values.append(value)

ort = toplam//index
result = 0
if index %2 == 1:
    result = index//2

medyan=values[result]
stringg = f"ortalama: {ort} \nmedyan: {medyan}"

txtdosyasi = open("output_dir_name/170401021_hw_2_output.txt","w")
txtdosyasi.write(stringg)
txtdosyasi.close()









