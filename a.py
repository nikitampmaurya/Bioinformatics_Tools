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
print("Length of the the original sequence:",len(n))

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
