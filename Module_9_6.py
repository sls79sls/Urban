def all_variants(text):
    i = 0
    while i != len(text):
        yield text[i]
        i += 1


a = all_variants("abc")
for i in a:
    print(i)
b = list(all_variants("abc"))
it = iter(all_variants("abc"))
print (next(it), next(it))
print (str(b[1]),str(b[2]))
c = list(all_variants("abc"))
print(str(c[0]),str(c[1]),str(c[2]))

