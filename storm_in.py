# Stormy Vowels
# 2/9/18
# Inventory Sort
#

print("Welcome to inventory sort!")
print("--------------------------\n")

inventory = {"abc111":12, "abc222":20, "abc333":24, "abc456":32,
"abc042":42, "bob001":22, "nic332":24, "van001":33, "jan444":16,
"gen001":24, "mar335":32, "jen888":38, "fun001":20, "fun002":26,
"lan001":22, "lan003":44, "jun333":22, "kit777":28, "why222":64,
"uti888":37, "bil444":32, "cor444":24}

s1 = {}
s2 = {}
s3 = {}
s4 = {}
s5 = {}
s6 = {}

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

wid = 120

for i, v in inventory.items():
    if (c1 + v) < wid:
        s1[i] = v              # Adds a new item to s1 dictionary
        c1 += v
    elif (c2 + v) < wid:
        s2[i] = v
        c2 += v
    elif (c3 + v) < wid:
        s3[i] = v
        c3 += v
    elif (c4 + v) < wid:
        s4[i] = v
        c4 += v
    elif (c5 + v) < wid:
        s5[i] = v
        c5 += v
    elif (c6 + v) < wid:
        s6[i] = v
        c6 += v
    else:
        print("No shelf for:", i, "\n")
        print(v, "inches of shelf space needed\n")

print("First shelf:\n", s1)
print("Second shelf:\n", s2)
print("Third shelf:\n", s3)
print("Fourth shelf:\n", s4)
print("Fifth shelf:\n", s5)
print("Sixth shelf:\n", s6)
