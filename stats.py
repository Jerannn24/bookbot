def get_num_words(filepath):
    with open(filepath) as f:
        text = f.read().split()
    return len(text)
    
def get_num_huruf(filepath):
    with open(filepath) as f:
        text = f.read().split()
        dicti = {}
        for c in text:
            for d in c:
                dl = d.lower()
                if dl.isalpha():
                    if dl in dicti:
                        dicti[dl] += 1
                    else:
                        dicti[dl] = 1
        return dicti
    
def get_new_dict (dicti):
    newList = []
    for key, value in dicti.items():
        newDict = {}
        newDict['char'] = key
        newDict['num'] = value
        newList.append(newDict)
    return newList