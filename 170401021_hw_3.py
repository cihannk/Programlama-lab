from sympy import Symbol,factor,pprint,factorial
import sympy.plotting as syp
import matplotlib.pyplot as plt
x=Symbol("x")
n=Symbol("n")
p=Symbol("p")
q= Symbol("q")
'''Cihan Kavuk 
170401021 
github.com/cihannk '''

formula = factorial(n)*(p**x)*(q**(n-x)) / (factorial(n-x)* factorial(x))
pprint( formula)
# Yeni evlenen 10 çiftden sayıya bağlı bir yıl sonunda mutlu olup olmadıklarını inceleyelim.
# Anketlere göre yeni evlenen çiftin mutlu olma olasılığı 0.3 tür
# x istenilen durum sayısı değişkendir, n deneme sayısıdır 10 çift üzerinden işlem yapıyoruz, p ise orandır

syp.plot(formula.subs({n:10,p:0.3,q:0.7}) , (x, 0,10), title="Her 10 yeni evlenen çiftten sayıya bağlı mutlu olma oranı")

x_values = []
y_values = []
for value in range(0,10):
   y = formula.subs({x:value,p:0.3,q:0.7,n:10}).evalf()
   y_values.append(y)
   x_values.append(value)
   print(value,y)
plt.plot(x_values,y_values)
plt.show()

'''Çalıştığım olasılık dağılımı binomial distribution'dur yani 2 farklı olasılığı olan bir olayın bir bütün halinde
incelenmesidir. Bu örneğimde çiftlerin mutlu ya da mutsuz olma olasılığı 2 farklı bir olasılıktır. x ise mutlu olan çiftlerin sayısıdır
x değiştikçe y yani mutlu olma oranı değişir.  

'''

