#
#


def DigitCancel(nom, dnom):

    rat = nom/dnom

    noml = [int(i) for i in str(nom)]
    dnoml = [int(j) for j in str(dnom)]

    noml.sort()
    dnoml.sort()

    if 0 in noml or 0 in dnoml or rat >= 1:
        return False

    elif noml[0] == dnoml[0]:
        if noml[1]/dnoml[1] == rat:
            return True
    elif noml[1] == dnoml[1]:
        if noml[0]/dnoml[0] == rat:
            return True

    else:
        return False

print(DigitCancel(14,46))

fracs = []

for i in range(10, 100):
    for j in range(10,100):
        if DigitCancel(i,j):
            fracs.append([i,j])


for f in fracs:
    print("{}/{} digit cancel".format(f[0], f[1]))
