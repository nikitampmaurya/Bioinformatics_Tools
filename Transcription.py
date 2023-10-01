#Aim: to turn dna into mrna (transcription) 

seq = "ATGC"
mrna = ""
for i in seq:
    if i=="A" or i=="a":
        mrna +="U"
    elif i=="T" or i=="t":
        mrna+="A"
    elif i=="G" or i=="g":
        mrna+="C"
    elif i=="C" or i=="c":
        mrna+="G"
    else:
        mrna += i
print("The original sequence: ", seq)
print("Here is your order - freshly prepared mrna:",mrna)

