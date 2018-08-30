lis = ["a","b","c","d","e","f"]
lis1 = ["a","e","a","r","c","a","a"]
vocals = ["a","e","i","o","u"]
#%%
def count_a(alist):
    ct = 0
    for let in alist:
        if let in vocals:
            ct = ct + 1
    print("There are",ct,"vocals a's in the list.")




count_a(lis1)