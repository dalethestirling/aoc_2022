#!/usr/bin/env python3

#(x,y)
def get_piece(t, y):
    A = set()
    if t==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif t == 1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif t == 2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif t==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

def move_left(piece):
    if any([x==0 for (x,y) in piece]):
        return piece
    return set([(x-1,y) for (x,y) in piece])

def move_right(piece):
    if any([x==6 for (x,y) in piece]):
        return piece
    return set([(x+1,y) for (x,y) in piece])

def move_down(piece):
    return set([(x,y-1) for (x,y) in piece])

def move_up(piece):
    return set([(x,y+1) for (x,y) in piece])

def signature(cavern_row):
    max_y = max([y for (x,y) in cavern_row])
    return frozenset([(x,max_y-y) for (x,y) in cavern_row if max_y-y<=30])

cavern_row = set([(x,0) for x in range(7)])

with open("./day17_input.txt") as f:
    movements = f.read().strip()


pattern_cache = {}
top = 0
idx = 0
rocks = 0
added = 0
while rocks<1000000000000:
    #print(rocks, len(SEEN))
    piece = get_piece(rocks%5, top+4)
    while True:
        # pushed -> down
        if movements[idx]=='<':
            piece = move_left(piece)
            if piece & cavern_row:
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & cavern_row:
                piece = move_left(piece)
        idx = (idx+1)%len(movements)
        piece = move_down(piece)
        if piece & cavern_row:
            piece = move_up(piece)
            cavern_row |= piece
            top = max([y for (x,y) in cavern_row])

            cache_query = (idx, rocks%5, signature(cavern_row))
            if cache_query in pattern_cache and rocks>=2022:
                (old_rocks, old_y) = pattern_cache[cache_query]
                print(old_rocks, old_y)
                dyn_top = top-old_y
                dyn_rocks = rocks-old_rocks
                amt = (1000000000000-rocks)//dyn_rocks
                added += amt*dyn_top
                rocks += amt*dyn_rocks
                assert rocks<=1000000000000
            pattern_cache[cache_query] = (rocks,top)
            break
    rocks += 1
print(cavern_row)
print(top+added)
