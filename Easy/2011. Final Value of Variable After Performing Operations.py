a = 0
change = {
    "++X": +1,
    "X++": +1,
    "--X": -1,
    "X--": -1,
}
for x in operations:
    a += change[x]
return a


# A little cleaner

for x in operations:
        if "+" in x:
            a += 1
        else:
            a -= 1
return a



# Or very short (not that intuitive)

return sum(1 if '+' in op else -1 for op in operations)
