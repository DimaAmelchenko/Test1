def srt(a):
        d = {}
        for k in set(a):
            if k == " ":
                continue
            d[k] = a.count(k)
        return d

a = "Spam"
d = srt(a)
print(d)