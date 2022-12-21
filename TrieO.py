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






p1=Trie()
p1.insertinTrie("i")
p1.insertinTrie("like")
p1.insertinTrie("sam")
p1.insertinTrie("samsung")
p1.insertinTrie("mobile")
if p1.findaWord("any"):
    print("found")
else:
    print("NOt Found")

if p1.wordBreak("ilikesamsung"):
    print("Word Break Is sunccesFull")
else:
    print("Word Break Not Possible")
if p1.checkPrefix("samx"):
    print("Prefix Exist")
else:
    print("prefix Doesn't Exist")