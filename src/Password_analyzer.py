import math

password = input("Enter password to analyze:")

length = len(password)
entropy = length * math.log2(94)

print("\nPassword Analysis")
print("------------------")
print("Length:", length)
print("Estimated Entropy:", round(entropy, 2))

if length < 8:
   print("Weak Password")
else:
   print("Moderate/Strong Password")
