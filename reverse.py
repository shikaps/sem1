n = input("Enter a something to find its reverse")
size = 0
for _ in n:
 size = size + 1
i = size - 1
r = ""
while (i>=0) :
 r = r +n[i]
 i = i - 1
print (r)