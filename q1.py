from fractions import Fraction

# Possibilidade de 1 pessoa fazer aniversário = 1/365

possibilidade1 = Fraction(1,365)

# Possibilidade duas pessoas fazerem aniversário estando na mesma sala = 1/133225, que é 1/365 ao quadrado

possibilidade2 = possibilidade1**2

# Agora só usar uma regra de três pensando que, 133225 são 100% das chances, agora basta calcular 80%

print((possibilidade2.denominator * 80) / 100)