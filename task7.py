a = True
b = False
c = False
print(f"а) {a or not (a and b) or c}")
print(f"б) {not a or a and (b or c)}")
print(f"в) {(a or b and not c) and c}")
