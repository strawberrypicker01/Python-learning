print("Enter marks obtained in a subject")
mark1 = input()
mark2 = input()
mark3 = input()
mark4 = input()
mark5 = input()
tot = int(mark1) +int(mark2) + int(mark3) + int(mark4) + int(mark5)
avg = tot/5
if (avg >=90 and avg <= 100):
    print("Your grade is A-A+!")
elif (avg >=81 and avg <= 90):
    print("Your grade is a B+")
elif (avg >=71 and avg <=80):
    print("Your grade is a B-C")
elif (avg >=61 and avg <+70):
    print ("Your grade is a D+-C")
elif (avg >=51 and avg <+60):
    print ("Your grade is a D- and D")
elif (avg >=41 and avg <+50):
    print ("Your grade is a F+-D-")
elif (avg >=31 and avg <+40):
    print ("Your grade is a F-F")
elif (avg >=21 and avg <+30):
    print ("Your grade is a F---F")
elif (avg >=11 and avg <+20):
    print ("Atp just never pick up the pencil again bro")





