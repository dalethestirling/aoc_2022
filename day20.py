def swap(records, idx):
    pos = records.index(idx)
    val, _ = records.pop(pos)
    nidx = (pos+val)%len(records)
    records.insert(nidx, idx)    

def mix(entries):
    new_list = [(n, i) for i, n in enumerate(entries)]
    for i, n in enumerate(entries):
        swap(new_list, (n, i))
    return [code[0] for code in new_list]

with open('day20_input.txt') as f:
    entries = [ line.strip() for line in f ]
    
base = [int(num) for num in entries]
mixed = mix(base)
coords = sum(mixed[(row+mixed.index(0))%len(mixed)] for row in (1000, 2000, 3000))
print(coords)


dKey = 811589153
l = list(map(lambda x:x*dKey, base))
mixed = mix(l, 10)
s = sum(mixed[(i+mixed.index(0))%len(mixed)] for i in (1000, 2000, 3000))
print(s)
