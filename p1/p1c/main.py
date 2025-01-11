values = [4.8974, 2.1212, 1.8328, 1.7204, 1.6667, 0.0000] # TENSÕES MEDIDAS

q1 = values[1] - values[2]
q2 = values[2] - values[3]
q3 = values[2] - values[4]

r1 = 10.257271162966372
r2 = 10.051622109371705
r3 = 10.257271162966372

print("quedas de tensão: ")
print(q1)
print(q2)
print(q3)


# correntes medidas
print("\ncorrentes (medidas):")

i1 = q1/r1 # corrente total
i2 = q2/r2
i3 = q3/r3

print(i1)
print(i2)
print(i3)

print("i2+i3:", i2+i3)


# resistências equivalentes
print("\nresistências equivalentes:")

req1 = (1/(1/300 + 1/300 + 1/300)) + 10
req2 = 10 + (1/(1/300 + 1/300))
req3 = 10 + (1/(1/300 + 1/300 + 1/300))
req = req1 + (1/(1/req2 + 1/req3))

print("req1: ", req1)
print("req2: ", req2)
print("req3: ", req3)
print("total: ", req)


# correntes (teóricas)
print("\ncorrentes (teóricas):")

ex_i1 = 5/req
ex_i2 = (req3*ex_i1)/(req2+req3)
ex_i3 = (req2*ex_i1)/(req2+req3)

print(ex_i1)
print(ex_i2)
print(ex_i3)