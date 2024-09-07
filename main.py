cash = int(input("enter cash amount:"))

note1 = cash // 100
note2 = (cash%100) // 50
note3 = ((cash%100))%50 // 10

print("you will get notes of 100 euros:",note1)
print("you will get notes of 50 euros:",note2)
print("you will get notes of 10 euros:",note3)


