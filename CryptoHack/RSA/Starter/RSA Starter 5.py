def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

n = 882564595536224140639625987659416029426239230804614613279163
ct = 77578995801157823671636298847186723593814843845525223303932
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

ph = (p-1)*(q-1)
gcd, x, y = extended_gcd(e, ph)

print(pow(ct, x, n))