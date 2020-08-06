# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:28:24 2020

@author: 1002
"""

import string


class CaesarCiper:
    def __init__(self):
        self.text = ""
        self.key  = 0
        self.x_26 = "abcdefghijklmnopqrstuwxyz"
        
    def encoder(self,text,key):
        s = text
        k = key
        c_lot_pun=string.punctuation+string.whitespace
        s=str(s)
        k=int(k)
        l=[]
        for  i in range(len(s)):
            b=s[i]
            if b in c_lot_pun:
                l.append(chr(ord(b)))
                
            else:#let letter between 26 lower letter
                if ord(b)+k>122:
                    y=ord(b)+k
                    y=y-26
                    l.append(chr(y))
                elif ord(b)+k<97:
                    y=ord(b)+k
                    y=y+26
                    l.append(chr(y))
                else:
                    l.append(chr(ord(b)+k))
                    
            
        return "".join(l)
        
    def decoder(self,thearticle):
        self.text = thearticle
        b={}
        a_list=[]
        a_list26 = list(self.x_26)
        thearticle1=list(thearticle)
        for letter in thearticle1:    
             if letter in a_list26:
                 a_list.append(letter)
        # get a dictionary , key is letter and value is the count of letter
        for i in a_list:
                
            if i in b:
                    
                    b[i]+=1
            else:
                    
                    b[i]=1
           
        #to find the letter and count of the most letter:　
        
        wcdict=b
        valkeylist=[]
        for key ,val in wcdict.items():
                valkeylist.append((val,key))
        
        valkeylist=sorted(valkeylist)
        
        
        t=len(valkeylist)
        max_count=valkeylist[t-1]
        max_letter=max_count[1]
        p=self.x_26.find(max_letter)
        #print("!!!!!!!!!!!!!!!!!!!!:",p)
        #print("!!!!!!!!!!!!!!!!!!!!:",max_letter)
        # get the shift key
        
        shiftkey=p-4
        k=shiftkey
        if k >0:
            print("it is right with:",k)
        else :
            print("it is left with :",k)
        self.key = -k
        #print("!!!!!!!!!!!!!!!!!!!!k:",k)
        
        decodeText = self.encoder(self.text,self.key)
        
        return decodeText
        
'''
encode:
    
ctcrj _qpxqnwvkqpcn jgvyqtmu (c_ju) jcxg dggpgzvgpukxgna uvwfkgf kp tgegpv agctu. iquv qh gzkuvkp
 c_j crrtqcejgu ctg fgukipgf hqt vjg jqoqigpqwu itcrju ykvj c ukping varg qh tgncvkqp. dqygxgt, 
 jgvgtqigpgqwu itcrju qh ownvkrng vargu qh tgncvkqpu ctg cnuq wdkswkvqwu cpf vjgtg ku c ncem qh
ogvjqfqnqikgu vq vcemng uwej itcrju. oqog rtgxkqwu uvwfkgu cfftguu vjg kuuwg da rgthqtokpi 
eqpxgpvkqpcn c_j qp gcej ukping tgncvkqp cpf vjgp dngpf

'''      
    
    


if __name__ == "__main__" :
     test = CaesarCiper()
     strkey = input("input key:")
     key = int(strkey)
     strText = input("input text which wang to be code:")
     codeText = test.encoder(strText,key)
     print("密文:",codeText)
     
     decodeText = test.decoder(codeText)
     print("密文:",decodeText)