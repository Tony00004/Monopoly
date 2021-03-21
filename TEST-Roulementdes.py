from random import*
def Roulementdes():
    n=randint(1,6)
    m=randint(1,6)
    s=(n+m)
    return (s)

def Maxi(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi

#class InitialisationDes :
#     def __init__(self, y, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35,x36, x37, x38, x39) :

y=100
x=0
x0=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
x8=0
x9=0
x10=0
x11=0
x12=0
x13=0
x14=0
x15=0
x16=0
x17=0
x18=0
x19=0
x20=0
x21=0
x22=0
x23=0
x24=0
x25=0
x26=0
x27=0
x28=0
x29=0
x30=0
x31=0
x32=0
x33=0
x34=0
x35=0
x36=0
x37=0
x38=0
x39=0

for i in range(y):
    x=x+Roulementdes()
    if x==0 : 
         x0=x0+1
    if x==1 :
        x1=x1+1
    if x==2 : 
         x2=x2+1
    if x==3 : 
         x3=x3+1
    if x==4 : 
         x4=x4+1
    if x==5 : 
         x5=x5+1
    if x==6 : 
         x6=x6+1
    if x==7 : 
         x7=x7+1
    if x==8 : 
         x8=x8+1
    if x==9 : 
         x9=x9+1
    if x==10 : 
         x10=x10+1
    if x==11 : 
         x11=x11+1
    if x==12 : 
         x12=x12+1
    if x==13 : 
         x13=x13+1
    if x==14 : 
         x14=x14+1
    if x==15 : 
         x15=x15+1
    if x==16 : 
         x16=x16+1
    if x==17 : 
         x17=x17+1
    if x==18 : 
         x18=x18+1
    if x==19 : 
         x19=x19+1
    if x==20 : 
         x20=x20+1
    if x==21 : 
         x21=x21+1
    if x==22 : 
         x22=x22+1
    if x==23 : 
         x23=x23+1
    if x==24 : 
         x24=x24+1
    if x==25 : 
         x25=x25+1
    if x==26 : 
         x26=x26+1
    if x==27 : 
         x27=x27+1
    if x==28 : 
         x28=x28+1
    if x==29 : 
         x29=x29+1
    if x==30 : 
         x30=x30+1
         x=x-20
    if x==31 : 
         x31=x31+1
    if x==32 : 
         x32=x32+1
    if x==33 : 
         x33=x33+1
    if x==34 : 
         x34=x34+1
    if x==35 : 
         x35=x35+1
    if x==36 : 
         x36=x36+1
    if x==37 : 
         x37=x37+1
    if x==38 : 
         x38=x38+1
    if x==39 : 
         x39=x39+1
    if x>=40 : 
         x=x-40

Case0=x0/y*100
Case1=x1/y*100
Case2=x2/y*100
Case3=x3/y*100
Case4=x4/y*100
Case5=x5/y*100
Case6=x6/y*100
Case7=x7/y*100
Case8=x8/y*100
Case9=x9/y*100
Case10=x10/y*100
Case11=x11/y*100
Case12=x12/y*100
Case13=x13/y*100
Case14=x14/y*100
Case15=x15/y*100
Case16=x16/y*100
Case17=x17/y*100
Case18=x18/y*100
Case19=x19/y*100
Case20=x20/y*100
Case21=x21/y*100
Case22=x22/y*100
Case23=x23/y*100
Case24=x24/y*100
Case25=x25/y*100
Case26=x26/y*100
Case27=x27/y*100
Case28=x28/y*100
Case29=x29/y*100
Case30=x30/y*100
Case31=x31/y*100
Case32=x32/y*100
Case33=x33/y*100
Case34=x34/y*100
Case35=x35/y*100
Case36=x36/y*100
Case37=x37/y*100
Case38=x38/y*100
Case39=x39/y*100

CaseListe=[]
CaseListe.append(Case0)
CaseListe.append(Case1)
CaseListe.append(Case2)
CaseListe.append(Case3)
CaseListe.append(Case4)
CaseListe.append(Case5)
CaseListe.append(Case6)
CaseListe.append(Case7)
CaseListe.append(Case8)
CaseListe.append(Case9)
CaseListe.append(Case10)
CaseListe.append(Case11)
CaseListe.append(Case12)
CaseListe.append(Case13)
CaseListe.append(Case14)
CaseListe.append(Case15)
CaseListe.append(Case16)
CaseListe.append(Case17)
CaseListe.append(Case18)
CaseListe.append(Case19)
CaseListe.append(Case20)
CaseListe.append(Case21)
CaseListe.append(Case22)
CaseListe.append(Case23)
CaseListe.append(Case24)
CaseListe.append(Case25)
CaseListe.append(Case26)
CaseListe.append(Case27)
CaseListe.append(Case28)
CaseListe.append(Case29)
CaseListe.append(Case30)
CaseListe.append(Case31)
CaseListe.append(Case32)
CaseListe.append(Case33)
CaseListe.append(Case34)
CaseListe.append(Case35)
CaseListe.append(Case36)
CaseListe.append(Case37)
CaseListe.append(Case38)
CaseListe.append(Case39)

print(Maxi(CaseListe))

print('Case 0: ',Case0)
print('Case 1: ',Case1)
print('Case 2: ',Case2)
print('Case 3: ',Case3)
print('Case 4: ',Case4)
print('Case 5: ',Case5)
print('Case 6: ',Case6)
print('Case 7: ',Case7)
print('Case 8: ',Case8)
print('Case 9: ',Case9)
print('Case 10: ',Case10)
print('Case 11: ',Case11)
print('Case 12: ',Case12)
print('Case 13: ',Case13)
print('Case 14: ',Case14)
print('Case 15: ',Case15)
print('Case 16: ',Case16)
print('Case 17: ',Case17)
print('Case 18: ',Case18)
print('Case 19: ',Case19)
print('Case 20: ',Case20)
print('Case 21: ',Case21)
print('Case 22: ',Case22)
print('Case 23: ',Case23)
print('Case 24: ',Case24)
print('Case 25: ',Case25)
print('Case 26: ',Case26)
print('Case 27: ',Case27)
print('Case 28: ',Case28)
print('Case 29: ',Case29)
print('Case 30: ',Case30)
print('Case 31: ',Case31)
print('Case 32: ',Case32)
print('Case 33: ',Case33)
print('Case 34: ',Case34)
print('Case 35: ',Case35)
print('Case 36: ',Case36)
print('Case 37: ',Case37)
print('Case 38: ',Case38)
print('Case 39: ',Case39)

