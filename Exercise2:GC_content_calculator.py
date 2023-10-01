"""
Aim: i) To build GC content calculator  
"""

#while loop is used to check if the given sequence has any number 
while True:
    seq = input("I am hungry again, Please feed me a DNA sequence: ")
    
    for letter in seq:
        if letter.isnumeric():
            print("Oops! your sequence has a number, please try again")
            break
            
    else:
        print("Thank you for feeding me")
        break

G_list = []
C_list = []
for i in seq:
    if i == "G" or i=="g":
        G_list +=i
    elif i == "C" or i=="c":
        C_list +=i
    else:
        pass
G_count = len(G_list)
C_count = len(C_list)
total_count = len(seq)
GC_content_calculator = 100*((G_count + C_count)/total_count)
#print("G list:",G_list)
#print(C_list)
#print(G_count)
#print(C_count)
#print(total_count)
print("The GC content of your sequence in percent:",round(GC_content_calculator,2)) #to round upto decimal point



