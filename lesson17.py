
def consecutive_combo(lst1, lst2):
    my_lst=lst1 + lst2
    my_lst.sort()
    for i in range(1, len(my_lst)):
        if my_lst[i] - my_lst[i -1] !=1:
            return False
    return True


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6])) #True




def tallest_skyscraper(lst):
    res = []
    for i, _ in enumerate(lst):
        if 1 in lst[i]:
            res.append(i)
    return len(res)


print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))  




def sock_merchant(lst):
    res=0
    for i in set(lst):
        res+= lst.count(i)//2
    return res

print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])) # 3

print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90])) #4




def remove_letters(letters, word):
    for i in word:
        letters.remove(i)
    return letters

print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))  
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "ballon")) 
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit")) 



def majority_vote(lst):
    for i in lst:
        if lst.count(i) > len(lst)/2:
            return i

print(majority_vote(["A", "A", "B"])) #"A"
print(majority_vote(["A", "A", "A", "B", "C", "A"])) #"A"
print(majority_vote(["A", "B", "B", "A", "C", "C"]))  #None


def pluralize(lst):
    res = []
    for i in lst:
        if lst.count(i)>1:
            res.append(i + 's')
        else:
            res.append(i)
    return set(res)

print(pluralize(["cow", "pig", "cow", "cow"])) #{ "cows", "pig" }
print(pluralize(["table", "table", "table"])) #{ "tables" }
print(pluralize(["chair", "pencil", "arm"])) #{ "chair", "pencil", "arm" }



def unique_styles(albums):
    res = []
    for i in albums:
        x = i.split(',')
        for j in x:
            res.append(j)
    return set(res)

print(unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
])) #9

print(unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
])) #7




def secret(txt):
    my_txt = txt.split('.')
    
    return  f"<{my_txt[0]} class='{' '.join(my_txt[1:])}'></{my_txt[0]}>"

print(secret("p.one.two.three")) #"<p class='one two three'></p>"
print(secret("p.one")) #"<p class='one'></p>"
print(secret("p.four.five")) #"<p class='four five'></p>"


def count_datatypes(*args):
    res = []
    types = [int, str, bool, list, tuple, dict]
    for i in args:
        
        res.append(type(i))
    return [res.count((i)) for i in types]


print(count_datatypes(1, 45, "Hi", False))  #[2, 1, 1, 0, 0, 0]