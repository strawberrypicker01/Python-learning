print("Half Pryamid Pattern of Stars(*):")
n = int(input("Please enter a number of rows that you'd like to see: "))
for i in range(n):
    for j in range(i+1):
      print("* ", end="")
    print()