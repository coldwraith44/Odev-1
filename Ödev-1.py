#Console Menu
#Anıl Erdoğan Bilgisayar Mühendisliği 220501006
#Akın Turan   Bilgisayar Mühendisliği 220501013


import tkinter as tk
from functools import reduce
import os
import math






def k_kucuk(k:int,l:list):
     
        l.sort()
            
        if k>len(l):

            print("Girdiğiniz değer listenin eleman sayısını aşıyor.")
            print("Tekrar deneyiniz!")
                       

        elif k==0 or k<0:

            print("Geçersiz değer girdiniz.")
            print("Tekrar deneyiniz!")
                        
        else:
            sonuc=l[k-1]
            return sonuc
                    

def en_yakin_cift(x:int,y:list):
      

    fark=10

    ilk_Sayi=5

    ikinci_sayi=5
     
    for i in range(len(y)):

        yeni_liste=y.copy()

        yeni_liste.pop(i)
            
        for j in range(len(yeni_liste)):
          
               z=y[i]+yeni_liste[j]

               if abs(x-z)<fark:

                    fark=abs(x-z)
                    
                    ilk_Sayi=y[i]

                    ikinci_sayi=yeni_liste[j]

    return [ilk_Sayi,ikinci_sayi]            

              



def tekrar_eden_elemanlar(x:list):

    tekrar_eden_elemanlar=[] 
    
    [tekrar_eden_elemanlar.append(i) for i in x if x.count(i)>1 and i not in tekrar_eden_elemanlar]

    return tekrar_eden_elemanlar[:]

def matris(liste1,liste2):
    sonuc = []

    for i in liste1:
        sonuc2 = []
        for i2 in zip(*liste2):
            sonuc2.append(sum(a*b for a,b in zip(i,i2))) #[[1,2,3], [4,5,6]] ve [[7,9,11],[8,10,12]
        sonuc.append(sonuc2)

    return sonuc


        

   

def kelime_sayisi(dosya_adi):
    
    with open(dosya_adi,'r') as d:
        kelimeler = d.read().split()


    """txt_directory ="C:/Users/PC/Desktop/Python Fell"
    txt_filename = "plabtext.txt"
    txt_path = os.path.join(txt_directory, txt_filename)"""

    def kucukharf(kelime):
        return kelime.lower()
    kelimeler = list(map(kucukharf,kelimeler))

    def sayac(kelime_sayac,kelime):
        kelime_sayac[kelime] = kelime_sayac.get(kelime,0)+1
        return kelime_sayac
    kelime_say = reduce(sayac,kelimeler,{})

    return kelime_say







def en_kucuk_deger(x:list):

    if len(x)==1:

        return x[0]
    
    else:

        if x[0] < x[1]:
            return en_kucuk_deger([x[0]]+x[2:])
        
        else:
            
            return en_kucuk_deger([x[1]]+x[2:])
        

def karekok(sayi, tahmin, maxiter, x=0):
    
    tol = 10**(-10)
    y = tahmin

    if x < maxiter:

        y = (1/2)*(tahmin + (sayi/tahmin))

        if abs((y**2) - (sayi)) < tol:

            return "Hata payı yeterince küçüldü. Sayınızın karekökü olarak hesaplandı:", y
        else:

            return karekok(sayi, y, maxiter, x+1)
    else:

        return "Yeterli denemede sayıya ulaşılmadı. Karekök değeri olarak hesaplandı:", y



def en_buyuk_ob(x:int,y:int):


    if y==0:

        return x
    
    else:
        return en_buyuk_ob(y,x%y)
    
def asal_sayi(x:int,y=2):

    if x ==y:

        return True
    elif x%y==0:

        return False
    
    return asal_sayi(x,y+1)


def fibo_dizisi(n, k=1, fibk=1, fibk1=0):
    print(n, k, fibk, fibk1)
    if k == n:
        return
    else:
        fibo_dizisi(n, k+1, fibk+fibk1, fibk)








print("┌──────────────────────────────────────────────────────┐")
print("│                         Menü                         │")
print("├──────────────────────────────────────────────────────┤")
print("│ 1-K’nıncı En Küçük Elemanı Bulma                     │")
print("│ 2-En Yakın Çifti Bulma                               │")
print("│ 3-Bir Listenin Tekrar Eden Elemanlarını Bulma        │")
print("│ 4-Matris Çarpımı                                     │")
print("│ 5-Bir Text Dosyasındaki Kelimelerin Frekansını Bulma │")
print("│ 6-Liste İçinde En Küçük Değeri Bulma                 │")
print("│ 7-Karekök Fonksiyonu                                 │")
print("│ 8-En Büyük Ortak Bölen                               │")
print("│ 9-Asallık Testi                                      │")
print("│ 10-Daha Hızlı Fibonacci Hesabı                       │")
print("│ 11-Çıkış                                             │")
print("└──────────────────────────────────────────────────────┘")


x=["1","2","3","4","5","6","7","8","9","10","11"]
y=True




while y:
    
    secim=input("Bir seçim giriniz:")

    
        

    if secim=="1":
            
            secim1=int(input("Bir tam sayı girin:"))

            secim2=input("Bir liste girin:")

            string_cevir1=""

            
            for i in secim2:
                string_cevir1=string_cevir1+i
                
            
            string_cevir1=string_cevir1[1:-1]

            print(string_cevir1)

            listeye_geri_cevir1=string_cevir1.split(",")

            print(listeye_geri_cevir1)

            listeyi_inte_cevir1=[]

            for i in listeye_geri_cevir1:
                
                listeyi_inte_cevir1.append(int(i))
            

            print("Bu listenin",secim1,". küçük elemanı:",k_kucuk(secim1,listeyi_inte_cevir1))


        

    elif secim=="2":
            

            secim3=int(input("Lütfen bir tam sayı girin:"))

            secim4=input("Bir liste girin")

            string_cevir2=""

            
            for i in secim4:

                string_cevir2=string_cevir2+i
                
            
            string_cevir2=string_cevir2[1:-1]

            listeye_geri_cevir2=string_cevir2.split(",")
            
            listeyi_inte_cevir=[]

            for i in listeye_geri_cevir2:
                
                listeyi_inte_cevir.append(int(i))
            
        



            print(en_yakin_cift(secim3,listeyi_inte_cevir))


    elif secim=="3":




        secim5=input("Lütfen bir liste girin:")

        string_cevir=""


        for i in secim5:

            string_cevir=string_cevir+i
                
        string_cevir=string_cevir[1:-1]

        listeye_geri_cevir=string_cevir.split(",")
            
        print(tekrar_eden_elemanlar(listeye_geri_cevir))
                
            
            
    elif secim =="4":
        secim10=input("Lütfen bir liste girin")
        secim11=input("Lütfen ikinci listeyi giriniz:")

        string_cevir4=""
        
        for i in secim10:
             string_cevir4=string_cevir4+i

        
        string_cevir4=string_cevir4[1:-1]
        listeye_geri_cevir4=string_cevir4.split(",")

        string_cevir5=""

        for i in secim11:
             string_cevir5=string_cevir5+i

        
        string_cevir5=string_cevir5[1:-1]
        listeye_geri_cevir5=string_cevir4.split(",")

        print("Sonuç:",matris(listeye_geri_cevir4,listeye_geri_cevir5))
        

    elif secim =="5":

        secim12=input("Lütfen dosyanın adını uzantısını belirterek girin:")

        print("Kelime frekansları:",kelime_sayisi(secim12))

    elif secim == "6":
         

        secim6=input("Lütfen bir liste girin:")

        string_cevir3=""

        for i in secim6:

            string_cevir3=string_cevir3+i
                
        string_cevir3=string_cevir3[1:-1]

        listeye_geri_cevir3=string_cevir3.split(",")
            
        print("Bu listedeki en küçük değer:",en_kucuk_deger(listeye_geri_cevir3))

         

    elif secim =="7":

        secim13=int(input("Lütfen bir sayı girin:"))
        secim14= float(input("Lütfen bir tahmin girin:"))
        secim15=int(input("Lütfen bir deneme sayısı girin:"))
        print("Sonuç:",karekok(secim13,secim14,secim15))
        

    elif secim=="8":

        secim7=int(input("Lütfen ilk sayıyı girin:"))
        secim8=int(input("Lütfen ikinci sayıyı girin:"))

        print("Bu iki sayının en büyük ortak böleni:",en_buyuk_ob(secim7,secim8))

    elif secim=="9":

        secim9=int(input("Lütfen bir tam sayı girin:"))

        if asal_sayi(secim9)==True:
             
             print(secim9,"bir asal sayıdır.")

        elif asal_sayi(secim9)==False:
             
             print(secim9,"bir asal sayı değildir.")

    elif secim =="10":

        secim16=int(input("Lütfen sayı girin:"))
        print("Sonuç",fibo_dizisi(secim16))


    elif secim=="11":
            print("İyi günler dileriz")
            break
    else:
            print("Lütfen seçeneklerdeki değerlerden birini girin!")
            continue

