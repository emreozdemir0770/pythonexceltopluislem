import os
import xlrd 



toplam=0
isim=""
deger=""
klasor = "./dosya"
for i in os.listdir(klasor):
    dosya = os.path.join(klasor,i)
    if os.path.isdir(dosya):
        print ('Klasör => ',i)
    elif os.path.isfile(dosya):   
        loc="dosya/"+i
        wb = xlrd.open_workbook(loc)  
        sheet = wb.sheet_by_index(0)
        print(sheet.cell_value(2,1))
        
        deger=sheet.cell_value(2,1)
        deger2=sheet.cell_value(1,1)
        deger3=sheet.cell_value(2,2)
        deger4=sheet.cell_value(1,2)
        
        
        x = []
        x.append([loc])
        
        y=[]
        y.append(deger)
        deger=int(deger)
        deger2=int(deger2)
        deger3=int(deger3)
        deger4=int(deger4)
        
        print (x)
        isim+="dosya adi:"+i+"deger:"+"==="+str(deger)+"--"+str(deger2)+"--"+str(deger3)+"--"+str(deger4)+"\n"
file1 = open("dosyalar.txt","w") 
L = [isim]  
file1.write("-----------------") 
file1.writelines(L) 
file1.close()