a1 = True
a2 = False
b1 = True
b2 = False
print(f"а) {not (a1 and b1)}, {not (a2 and b1)}, {not (a1 and b2)}, \
{not (a2 and b2)}")
print(f"б) {not a1 or b1}, {not a2 or b1}, {not a1 or b2}, \
{not a2 or b2}")
print(f"в) {a1 or not b1}, {a2 or not b1}, {a1 or not b2}, \
{a2 or not b2}")
