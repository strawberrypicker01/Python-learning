Amount = int(input("Please enter amount for Withdrawal"))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("Notes of 100 dollars", note_1)
print("Notes of 50 dollars", note_2)
print("Notes of 10 dollars", note_3)