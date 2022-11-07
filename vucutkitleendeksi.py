kilonuz= float(input("Kilonuzu giriniz "))
boy=float(input("boyunuzu metre cinsinden giriniz "))
vucutKitleİndeksi= kilonuz/boy**2
print("vücut kitle indeksiniz ",vucutKitleİndeksi)
if  18.5<=vucutKitleİndeksi<=24.9:
    print("saglıklısınız,İdeal kilodasınız")
elif vucutKitleİndeksi<18.5 :
    print("yemek ye")
else:
    print("yedin doymadın")
