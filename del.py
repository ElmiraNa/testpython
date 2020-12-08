# importing the module 
import ast 
  
# reading the data from the file 
with open("C:/Users/ICTSG10/Desktop/new2.txt", encoding="utf-8") as f: 
    data = f.read() 
  
#print("Data type before reconstruction : ", type(data)) 
      
# reconstructing the data as a dictionary 
d = ast.literal_eval(data) 
  

print(type(d))
ezafat= ['amazing', 'follow4follow', 'instacool', 'picoftheday', 'instadaily', 'repost', 'viral', 'repost', '4k']

def remove(list1, list2):
    result=[]
    for item in list1:
        if item not in list2:
            result.append(item)

    return(result)


def get_key(val): 
    for key, value in d.items(): 
         if val == value: 
             return key 
final=[]
for item in d.values():
    a=remove(item, ezafat)
   

    final.append("{"+str(get_key(item))+"}"+":"+str(a))

with open("C:/Users/ICTSG10/Desktop/yes1.txt", mode='a', encoding="utf-8") as File:
    File.write(str(final))




""" def remove(list1, list2):
    result=[]
    for item in list1:
        if item not in list2:
            result.append(item)

    return(result)

ezafat= ['amazing', 'follow4follow', 'instacool', 'picoftheday', 'instadaily', 'repost', 'viral', 'repost']


with  open("C:/Users/ICTSG10/Desktop/new2.txt", mode="r", encoding='utf-8') as target:


    t=0
    for item in target:
        
        
        k=item.values()
        final=remove(k, ezafat)
        with open('C:/Users/ICTSG10/Desktop/finally.txt', mode='a') as myFile:
            myFile.write(final)
        t+=1
   





print(t) """