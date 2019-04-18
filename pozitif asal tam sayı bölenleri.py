#authored and designed(what desiging?in python just joking) by osman ceylan
#UTF-8 türkçe karakter uymunu açmak lazım

def girilensayİ():
    D=0
    while D==0:
        try:
            sayı=int(input("Asal sayı bölenlerini bulmak istediğiniz sayı: "))
            if int(sayı)<=0:
                print("Sıfırdan büyük sayı girmelisin")
            elif int(sayı)>0:
                D=1
        except ValueError:
            print ("Lütfen sayıları kullanın")
    return sayı
#Prime number creator
Sınır=250
def asal():
    a=3
    b=3
    c=11
    t=0
    while c<Sınır:
        t=0
        while a<c:
            while b<(c/2):
                if a*b==c:
                    t=t+1
                b=b+2
            b=3
            a=a+2
        if t==0:
            A.append(c)
        a=3
        b=3
        c=c+2
    A.extend([2,3,5,7])
    A.sort()    
sayı=girilensayİ()
orjinalsayı=sayİ
A=[]
asal()
B=[]
i=0
while i<len(A):
    sayac=1
    while sayac==1:
        if ((sayı)//A[i])*A[i]==(sayı):
            B.append(float(sayı))
            sayı=(int(sayı))/A[i]
        else:
            i=i+1
            sayac=0
B.append(1.0)
i=0
C=[]
while i+1<len(B):
    alt=B[i]//B[i+1]
    C.append(alt)
    i=i+1
D=[]
i=0
while i<len(A):
    ust=C.count(A[i])
    D.append(ust)
    i=i+1
for i in range(1,len(D)):
    try:
        D.remove(0)
    except:
        print ("")
for i in range(0,len(D)):
    D[i]=D[i]+1
if len(D)==1:
    f=D[0]
for i in range(0,len(D)-1):
    f=D[i]*D[i+1]
    D[i]=D[i+1]
print ("\nBölüm şeması:",B,"\nBölen asal sayılar:",C,"\nToplam pozitif sayı bölenleri:",f,"\nToplam tam sayı bölenleri:",2*f)
if len(C)==0 or len(C)==1:
    if orjinalsayı<250:
        print ("Tebrikler girdiğiniz sayı asal sayıdır")
    if orjinalsayı>250:
        print ("Sayı 250'den büyük olduğundan asal sayı olup olmadığı kesin değil")
        Sec=0
        while Sec==0:
            try:
                Sec1=int(input("Sayının asal olup olmadığını kontrol etmek iste misiniz?\n(1'no:EVET diğerleri:HAYIR): "))
                if Sec1<0 or Sec1>0 or Sec==0:
                    Sec=1
            except ValueError:
                print ("Lütfen sadece sayı giriniz")
        if Sec1==1:
            Sınır=int(orjinalsayı)+2
            A=[]
            asal()
            if A.count(orjinalsayı)>=1:
                print ("Evet bu bir asal sayı")
            else:
                print ("Hayır asal sayı değilmiş")      







