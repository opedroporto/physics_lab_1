values = [4.7654, 0.0000] # TENSÕES MEDIDAS

q200 = values[0]
print("queda de tensão no resistor de 200 Ω: ", q200)

q10 = 5 - q200
print("queda de tensão no resistor de 10 Ω: ", q10)

current = q200/200
print("corrente: ", current)

def get_voltage(q200):
    q10 = 5 - q200
    return q10 / current

print("(1) resistência REAL do de 10: ", get_voltage(4.7556))
print("(2) resistência REAL do de 10: ", get_voltage(4.7605))
print("(3) resistência REAL do de 10: ", get_voltage(4.7556))
