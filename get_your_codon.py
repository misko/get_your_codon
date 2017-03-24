import sys

codon_to_amino = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

amino_to_codon = {}
for key in codon_to_amino:
	amino_to_codon[codon_to_amino[key]]=key

alpha={'B':'P','J':'Y','O':'Q','U':'V','X':'K','Z':'S'}

def s_to_s(s):
	s=s.upper()
	for x in alpha:
		s=s.replace(x,alpha[x])
	return s

def text_to_codon(s):
	r=[]
	for x in s.split():
		dna=""
		for y in s_to_s(x):
			dna=dna+amino_to_codon[y]
		r.append(dna)
	return amino_to_codon['STOP'].join(r)

def codon_to_text(s):
	assert(len(s)%3==0)
	r=""
	for x in range(len(s)/3):
		c=s[x*3:(x+1)*3]
		a=codon_to_amino[c]
		if a=='STOP':
			r=r+" "
		else:
			r=r+a
	return r

if len(sys.argv)!=2:
	print sys.argv[0] + " msg"
	sys.exit(1)

s=sys.argv[1]

c=text_to_codon(s_to_s(s))
print s
print c
print codon_to_text(c)
