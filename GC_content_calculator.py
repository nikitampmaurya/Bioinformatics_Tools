"""
Aim: i) To build GC content calculator  
"""

s = "ATGCATGCGCTAgc"
G_list = []
C_list = []
for i in s:
    if i == "G" or i=="g":
        G_list +=i
    elif i == "C" or i=="c":
        C_list +=i
    else:
        pass
G_count = len(G_list)
C_count = len(C_list)
total_count = len(s)
GC_content_calculator = 100*((G_count + C_count)/total_count)
#print("G list:",G_list)
#print(C_list)
#print(G_count)
#print(C_count)
#print(total_count)
print("The GC content in percent is:",round(GC_content_calculator,2)) #to round upto decimal point



