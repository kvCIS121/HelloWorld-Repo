# Tolerance for Circuits 1 Lab, 2.3, using +/- 5% 
num = float(input('Nominal value: '))
tolerance = 0.05
downTotal = num - (num * 0.05)
upTotal = num + (num * 0.05)
print(downTotal)
print(upTotal)
