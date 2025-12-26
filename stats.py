def wordCount(text):
    return len(text.split())

def charCount(text):
    charChart=dict()
    for c in text:
        if c.lower() not in charChart: charChart[c.lower()]=0
        charChart[c.lower()]+=1
    return charChart

def getNumKey(page): return page["num"]

def sortedDictionary(char_dict):
    result=[]
    for character in char_dict:
        result.append({"char":character,"num":char_dict[character]})
    result.sort(reverse=True,key=getNumKey)
    return result