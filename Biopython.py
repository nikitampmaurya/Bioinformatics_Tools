#Step1: To install Biopython
#pip install biopython 

#Step2: To Check Biopython version
import Bio
print("Biopython version:",Bio.__version__)

#Step3: To check the data type of a sequence before and after using library 
s = "ATGC"
print("my sequence: ",s)
print("Data type of my sequence before importing library:",type(s),"=",s) 

#Step 4: To check the data type of a sequence after importing library
from Bio.Seq import Seq
n = Seq(s) #convert string into sequence
print("Data type of sequence after importing library:", type(n)) 

#Step 5: To print original sequence, complement and reverse of my sequence
print("Original sequence:",n)
print("complement of the original sequence:",n.complement())
print("reverse of my original sequence",n.reverse_complement())
print("length of the the original sequence:",len(n))

#Step 6: To parse simple fasta file, to get every sequence's id, length and 
from Bio import SeqIO 
file_path = "C:\\Users\\Nikita Maurya\\OneDrive\\Desktop\\Nikita\\pythonfiles\\ls_orchid.fasta.txt"
for my_sequence_record in SeqIO.parse(file_path,"fasta"): 
    print(my_sequence_record.id) 
    print(repr(my_sequence_record.seq)) 
    print(len(my_sequence_record)) 

#Step 7: To parse genebank file, to get every sequence's id, sequence and length

from Bio import SeqIO
file_path = "C:\\Users\\Nikita Maurya\\OneDrive\\Desktop\\Nikita\\pythonfiles\\ls_orchid.gbk.txt"
for my_sequence_record in SeqIO.parse(file_path,"genbank"):
    print(my_sequence_record.id)
    print(repr(my_sequence_record.seq))
    print(len(my_sequence_record))

"""
Step 8: 
i)   to print nucleotide present at x position in the given dna sequence
ii)  to print first and last nucleotide of the given dna sequence
iii) to slice the given sequence
iv) to count specify segement of the given dna sequence
v)  to calculate GC content of the given DNA sequence 
"""
from Bio.Seq import Seq                             
s = Seq("ATGCAA")                 #Feed a new dna sequence
print("The original sequence: ", s) 
for a, b in enumerate(s):         #i) a = index of nucleotide, b = nucleotide
    print("%s %i" %(b, a))                         #s and i are placeholder for b and a, used for formatting  
print("The first nucleotide of the sequence: ",s[0])     #ii) print only first nucleotide          
print("The first nucleotide of the sequence: ",s[-1])          #ii) print only last nucleotide
print("The short segment of the sequence: ",s[2:])        #iii) to slice sequence from third place till the end
print("The number of given nucelotide sequence is", s.count("A"))      #iv) to count specify segment
cal_GC_content = ((s.count("G") + s.count("C"))/len(s))*100       #v) To calculate GC content in percentage
print("Total GC content: ",round(cal_GC_content,2)) 

from Bio.SeqUtils import gc_fraction                              #v)To directly print GC content
print("Using gc function to print gc content: ",gc_fraction(s))

#Step 9: To add two sequence 

from Bio.Seq import Seq
seq1 = Seq("AAT")
seq2 = Seq("TGC")
new_seq = seq1 + seq2
print("The first sequence: ",seq1)
print("The second sequence: ",seq2)
print("The concatenated sequence: ",new_seq)
