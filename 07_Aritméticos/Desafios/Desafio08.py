n1=float(input("Uma distancia em metros:"))
cm= n1 * 100
mm= n1 * 1000
km= n1 / 1000
hm= n1 / 100
dm= n1 / 10
print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(n1, cm, mm))
print("A medida de {}m corresponde a {}km e {}hm e{}dm".format(n1,km,hm,dm))