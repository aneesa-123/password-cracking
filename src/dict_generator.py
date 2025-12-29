names = ["admin", "user", "test"]
years = ["123", "1234", "2024"]
symbols = ["@", "!", "#"]

with open("custom_wordlist.txt", "w") as file:
   for name in names:
       for year in years:
           file.write(name + year + "\n")
           for sym in symbols:
               file.write(name + year + sym + "\n")
print("Custom wordlist generated successfully!")
