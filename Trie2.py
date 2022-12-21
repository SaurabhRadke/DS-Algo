class Node:
    def __init__(self):
        self.child=[None for i in range(26)]
        self.eow=False

class Trie:
    def __init__(self):
        self.root=Node()
    def insertinTrie(self,word):
        curr=self.root
        for i in range(0,len(word)):
            p=ord(word[i])-ord("a")
            if curr.child[p]==None:
                curr.child[p]=Node()
            if i ==len(word)-1:
                curr.child[p].eow=True
            curr=curr.child[p]
    def findaWord(self,word):
        curr=self.root
        for i in range(len(word)):
            ind=ord(word[i])-ord("a")
            if curr.child[ind]==None:
                return False
            if i==len(word)-1 and curr.child[ind].eow==False:
                return False
            curr=curr.child[ind]
        return True
    def wordBreak(self,key):
        if len(key)==0:
            return True
        for i in range(1,len(key)+1):
            p1=key[0:i]
            p2=key[i:]
            if self.findaWord(p1) and self.wordBreak(p2):
                return True
        return False
    def checkPrefix(self,pre):
        curr = self.root
        for i in range(len(pre)):
            ind = ord(pre[i]) - ord("a")
            if curr.child[ind] == None:
                return False
            curr = curr.child[ind]
        return True
    def countalluniqueSubstring(self,roo):
        if roo==None:
            return 0
        count=0
        for i in range(0,26):
            if roo.child[i]!=None:
                count+=self.countalluniqueSubstring(roo.child[i])
        return count+1
    def printcount(self):
        pp=self.root
        k=self.countalluniqueSubstring(pp)
        print(k)






p1=Trie()
key="ababac"
word=set()
for i in range(0,len(key)):
        word.add(key[i:])
        p1.insertinTrie(key[i:])
print(word)
p1.printcount()
