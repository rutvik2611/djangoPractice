x = "there is an interview"


def flip(p):
    p=p[::-1]
    return p

def final(x):
    t=[]
    y=x.split()
    for i in y:
        save=flip(i)
        t.append(save)
    return ' '.join(t)

print(final(x))