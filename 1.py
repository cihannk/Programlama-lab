import random

def createrandomlist(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

def histo(list):
    a = dict()
    for item in list:
        if item in a:
            a[item]=a[item]+1
        else:
            a[item]=1
    return a

def histo2(list):
    freq_list=[]
    for i in range(len(list)):
        s=False
        for j in range(freq_list):
            if (list[i]==freq_list[j][0]):
                freq_list[j][1]=freq_list[j][1]+1
                s=True
            if s==False:
                freq_list.append(list[i],1)
    return  freq_list

def returnmodeandfreq(dict):
    freq_max=-1
    mode=-1
    for key in dict.keys():
        print(key,dict[key])
        if dict[key]>freq_max:
            freq_max=dict[key]
            mode=key
    return freq_max,mode

#list = createrandomlist(10,0,10)
#histog = histo(list)
#modeandfrq = returnmodeandfreq(histog)
#print(f"list: {list}\nhistog: {histog}\nkaç kere ve en çok tekrar eden : {modeandfrq}")

def tuplemodeandfreq(list):
    freq_max=-1
    mode=-1
    for item,freq in list:
        print(item,freq)
        if freq>freq_max:
            freq_max=freq
            mode=item
    return mode,freq_max

#linear search


def my_search(my_list,item_search):
    found=(-1,-1)
    lenght=len(my_list)
    for item in range(lenght):
        if item==item_search:
            found=(my_list[item],item)
    return found
    # index,aranan sayi dondurur

def meanoflist(list):
    topl,ind=0,0
    for item in list:
        ind=ind+1
        topl=topl+item
    ort= topl/ind
    return ort

def bubble_sort(list):
    uz = len(list)
    for i in range(uz-1,-1,-1):
        for j in range(0,i):
            if not list[j]<list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

def my_binary_search(list,item_search):
    low=0
    high=len(list)-1
    found=(-1,-1)
    while(low<=high):
        mid = (low+high) // 2
        if list[mid]==item_search:
            return list[mid],mid
        elif list[mid]>item_search:
            high=mid-1
        else:
            low = mid+1
    return found

def my_median(list):
    lenght= len(list)
    sorted_list = bubble_sort(list)
    if (lenght%2) ==1:
        mid = int(lenght/2) +1
        median = sorted_list[mid]
    else:
        mid1 = int(lenght/2)
        mid2 = int((lenght/2)) +1
        median = int((sorted_list[mid1]+sorted_list[mid2])/2)
    return median,sorted_list



























