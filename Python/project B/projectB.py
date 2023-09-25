# -*- coding: utf-8 -*-
codons = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
          "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
          "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
          "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
          "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
          "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
          "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
          "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
          "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
          "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
          "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
          "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
          "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
          "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
          "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
          "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}

#outputs the comparisons between dna1,2,3 and ref        
def main():
    """ Write your code here """
    ref = readFile('ref.txt')
    dna1 = readFile('dna1.txt')
    dna2 = readFile('dna2.txt')
    dna3 = readFile('dna3.txt')
    
    print(f'Subject 1 DNA has {count(dna1, ref)} mutations and is', 'synonymous' if synonymous(dna1, ref) else 'not synonymous')
    print(f'Subject 2 DNA has {count(dna2, ref)} mutations and is', 'synonymous' if synonymous(dna2, ref) else 'not synonymous')
    print(f'Subject 3 DNA has {count(dna3, ref)} mutations and is', 'synonymous' if synonymous(dna3, ref) else 'not synonymous')


#file reader    
def readFile(fileName):
    """
    Reads a text file.
    
    Parameters
    ----------
    fileName : str
        File path to read.

    Returns
    -------
    str
        Text from file.
    """
    with open(fileName,'r') as dnaFile:
        dna = "".join(dnaFile.readlines()).strip()
    return dna
    
#file writer    
def writeFile(fileName,text):
    """
    Writes a text file.

    Parameters
    ----------
    fileName : str
        File path to write.
    text : str
        Text to write.

    Returns
    -------
    None.

    """
    with open(fileName,'w') as textFile:
        textFile.write(text)
    
#turns string dna into string mRNA complement
def transcribe(dna):
    """ Write your code here """
    mRNA = ''
    for char in dna:
        if char == 'T':
            mRNA += 'U'
        else: mRNA += char
    return mRNA

#turns string mRNA into string protein chain    
def translate(mrna):
    """ Write your code here """
    prt = ''
    while len(mrna) > 2:
        prt += codons[mrna[:3]] + ' '
        mrna = mrna[3:]
    return prt

#returns T or F, T if 2 dna returns the same protein chain, F if not
def synonymous(sub, ref):
    """ Write your code here """
    mRNA1 = transcribe(sub)
    mRNA2 = transcribe(ref)
    prt1 = translate(mRNA1)
    prt2 = translate(mRNA2)
    if prt1 == prt2:
        return True
    return False
    

#deletes dna[i]
def delete(dna, i):
    """ Write your code here """
    if i == len(dna)-1:
        return dna[:i]
    else:
        return dna[:i] + dna[i+1:]

#inserts base at dna[i]
def insert(dna, i, base):
    """ Write your code here """
    if i == len(dna):
        return dna[:len(dna)] + base
    else:
        return dna[:i] + base + dna[i:]

#substitutes dna[i] with base
def substitute(dna, i, base):
    """ Write your code here """
    new_dna = delete(dna,i)
    new_dna = insert(new_dna, i, base)
    return new_dna

#gets index of first difference between string sub and string ref
def diff(sub, ref):                 
    """ Write your code here """
    for index in range(min(len(sub), len(ref))):
        if sub[index] == ref[index]:
            pass
        else:
            return index
    if len(sub) != len(ref):
        return min(len(sub), len(ref)) 
    return -1

#returns the best repair of string osub to match string ref
def repair(osub, ref):
    """ Write your code here """
    #method, diff
    sub = osub
    repairs = {}
    best_sub = sub
    best_err = 0
    err1 = diff(best_sub,ref)
    if err1 == -1:
        return sub

    #substitute
    repairs['substitute'] = substitute(sub, err1, ref[err1])
    err2 = diff(repairs['substitute'], ref)
    if err2 > best_err or err2 == -1:
        best_sub = repairs['substitute']
        best_err = err2
        sub = osub
        if best_err == -1:
            return repairs['substitute']
    #delete
    repairs['delete'] = delete(sub, err1)
    err3 = diff(repairs['delete'], ref)
    if err3 > best_err or err3 == -1:
        best_sub = repairs['delete']
        best_err = err3
        sub = osub
        if best_err == -1:
            return repairs['delete']
        
    #insert
    repairs['insert'] = insert(sub, err1, ref[err1])
    err4 = diff(repairs['insert'], ref)
    if err4 > best_err or err4 == -1:
        best_sub = repairs['insert']
        best_err = err4
        sub = osub
        if best_err == -1:
            return repairs['insert']
    return best_sub


    
#counts how many mutations between sub and ref    
def count(sub, ref):
    """ Write your code here """
    i = 0
    while diff(sub,ref) != -1:
        sub = repair(sub, ref)
        i += 1
    return i

#executes main
if __name__ == "__main__":
    main()







