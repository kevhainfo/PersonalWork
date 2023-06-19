def rando():
    m, m2 = 2147483647, 2145483479
    a12, a13, a21, a23 = 63308, -183326, 86098, -539608
    q12, q13, q21, q23 = 33921, 11714, 24919, 3976
    r12, r13, r21, r23 = 12979, 2883, 7417, 2071
    invm = 4.656612873077393e-10
    h = rando.x10 // q13
    p13=-a13*(rando.x10-h*q13)-h*r13
    h = rando.x11 // q12
    p12=a12*(rando.x11-h*q12)-h*r12
    if p13<0:p13=p13+m
    if p12<0:p12=p12+m
    rando.x10, rando.x11, rando.x12 = rando.x11, rando.x12, p12 - p13
    if rando.x12 < 0: rando.x12 = rando.x12 + m
    h = rando.x20 // q23
    p23=-a23*(rando.x20-h*q23)-h*r23
    h=rando.x22 // q21
    p21=a21*(rando.x22-h*q21)
    if p23<0: p23=p23+m2
    if p21<0: p21=p21+m2
    rando.x20, rando.x21,rando.x22= rando.x21,rando.x22,p21-p23
    if rando.x22<0: rando.x22=rando.x22+m2
    if rando.x12<rando.x22: h=rando.x12-rando.x22+m
    else: h=rando.x12-rando.x22
    if h==0 : return 0.5
    else: return h*invm

rando.x10, rando.x11, rando.x12=12345,67890,13579
rando.x20, rando.x21, rando.x22=24680,98766,43210
def unif(low, high):
    return low+int((high-low+1)*rando())




