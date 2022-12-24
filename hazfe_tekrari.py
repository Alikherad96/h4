araye_m = []
araye = []
while True:
    nn = input("plz enter ur num ( break : space )")
    if nn == " ":
        break
    else:
        araye.append(int(nn))
for t in araye:
    if t not in araye_m:
        araye_m.append(t)
        #print(araye_m)

print("liste gheyre tekrari : = ", araye_m)
