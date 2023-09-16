print("Hi")
import Bio
print("Python version:",Bio.__version__)
import os
os.getcwd()
print("Current working directory:",os.getcwd())
os.chdir("C:\\Users\\Nikita Maurya\\OneDrive\\Desktop\\Nikita\\pythonfiles")
print("Current working directory:",os.getcwd())
print(os.listdir())
#python --version
s = "ATGC"
print("my sequence",s)
print("Data type of my sequence before importing library:",type(s),"=",s)
from Bio.Seq import Seq
n = Seq(s)
print("data type of sequence after importing library:", type(n))
print("Original sequence:",n)
print("complement of the original sequence:",n.complement())
print("reverse of my original sequence",n.reverse_complement())

from Bio import SeqIO 
for seq_record in SeqIO.parse("ls_orchid.fasta.txt","fasta"): 
    print(seq_record.id) 
    print(repr(seq_record.seq)) 
    print(len(seq_record)) 



