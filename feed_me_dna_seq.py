""""
Aim: Accept a DNA sequence as input, then generate and display the following information:
i)  The complement of the input sequence.
ii) The reverse of the input sequence.
ii) The length of the input sequence.
"""
#convert(seq) function take original sequence as its argument, it is used to producing a complement of an original sequence  
def convert(seq):
    new_seq = ""
    for i in seq:
        if i=="A" or i=="a":
            new_seq += "T"
        elif i=="T" or i=="t":
            new_seq += "A"
        elif i=="G" or i=="g":
            new_seq += "C"
        elif i=="C" or i=="c":
            new_seq += "G"
        else:
            new_seq += i
    return new_seq
# reverse_seq function take the same arguement and used to print the reverse of an original sequence 
def reverse_seq(seq):
    n = list(seq)
    nl = n[::-1]
    h = "".join(nl)
    return h

#while loop is used to check if the given sequence has any number 
while True:
    seq = input("I am hungry, Please feed me a DNA sequence: ")
    
    for letter in seq:
        if letter.isnumeric():
            print("Oops! your sequence has a number, please try again")
            break
            
    else:
        print("Thank you for feeding me")
        break

print("The original sequence:",seq)
print("The complement of original seq:",convert(seq))
print("The reverse of original sequence",reverse_seq(seq))
print("Length of the original sequence:", len(seq))







