#Exercise 1: To install Biopython
#pip install biopython 

#Exercise 2: To Check Biopython version
import Bio
print("Biopython version:",Bio.__version__)

#Exercise 3: To check the data type of a sequence before and after using library 
s = "ATGC"
print("my sequence: ",s)
print("Data type of my sequence before importing library:",type(s),"=",s) 

#Excercise 4: To check the data type of a sequence after importing library
from Bio.Seq import Seq
n = Seq(s) #convert string into sequence
print("Data type of sequence after importing library:", type(n)) 

#Exercise 5: To print original sequence, complement and reverse of my sequence
print("Original sequence:",n)
print("complement of the original sequence:",n.complement())
print("reverse of my original sequence",n.reverse_complement())
print("Length of the the original sequence:",len(n))

#Exercise 6: To parse simple fasta file, to get every sequence's id, length and 
from Bio import SeqIO 
file_path = "C:\\Users\\Nikita Maurya\\OneDrive\\Desktop\\Nikita\\pythonfiles\\ls_orchid.fasta.txt"
for my_sequence_record in SeqIO.parse(file_path,"fasta"): 
    print(my_sequence_record.id) 
    print(repr(my_sequence_record.seq)) 
    print(len(my_sequence_record)) 

#Exercise 7: To parse genebank file, to get every sequence's id, sequence and length

from Bio import SeqIO
file_path = "C:\\Users\\Nikita Maurya\\OneDrive\\Desktop\\Nikita\\pythonfiles\\ls_orchid.gbk.txt"
for my_sequence_record in SeqIO.parse(file_path,"genbank"):
    print(my_sequence_record.id)
    print(repr(my_sequence_record.seq))
    print(len(my_sequence_record))

"""
Exercise 8: 
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

#Exercise 9: To add two sequence 

from Bio.Seq import Seq
seq1 = Seq("AAT")
seq2 = Seq("TGC")
new_seq = seq1 + seq2
print("The first sequence: ",seq1)
print("The second sequence: ",seq2)
print("The concatenated sequence: ",new_seq)

#Excercise 10: To add repeating string in the middle of two sequences

from Bio.Seq import Seq
list_of_seq = [Seq("ATG"),Seq("CGT")]
add_repeating_string = Seq("X"*5)
example = add_repeating_string.join(list_of_seq)
print(example)  


"""
Exercise 11: To transcibe and translate dna sequnce in biopython
Important note: 
- transcription in Biopython 
- in Biopyhton transcription occurs from complementary strand/coding strand and not template strand
- because it is easy to convert complementary strand/coding strand to mrna, by just switching T to U
- complementary strand and coding strand have same sequence but serve different purposes
"""
from Bio.Seq import Seq
template_strand = Seq("TACCGGTAAATC")
print("The template strand running from 3' end to 5'end:",template_strand)
complementary_strand = template_strand.complement()
print("The complement strand running from 5' to 3'end:",complementary_strand)
mrna = complementary_strand.transcribe() #switching T in coding strand/complement strand to U in mrna
print("mrna strand from 5' end to 3' end:",mrna)
print("mrna to dna from 5'end to 3' end:", mrna.back_transcribe()) #swiching U in mrna to T in dna

#To translate protein from rna
translated_mrna = mrna.translate()
print("The protein translated from mrna:",translated_mrna)
#to tranlate protein from coding strand
tranlated_from_complementary_strand = complementary_strand.translate()
print("The protein from complementary strand: ",tranlated_from_complementary_strand)


"""
Exercise 12: 
"""
from Bio.Seq import MutableSeq
sequence = MutableSeq("GCCATTG")
print("Original sequence: ",sequence)
sequence[0] = "A"
print("Mutated sequence at index 0:",sequence)
sequence.remove("T") #one letter at time, not segment
print("Mutated sequence without T:",sequence)
sequence = Seq(sequence) #to convert mutated sequence back to read only object



