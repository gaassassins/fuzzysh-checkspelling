import time

f = open('words.txt')

def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

def n_gramm(a):
    res = []
    for i in range(len(a) - 2):
        res.append(a[i:i + 3])
    return res


def compare(a, b):
    k = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] == a[j]):
                k += 1
                break
    return k

def algirithmLevi(a):
    minn = len(a) #len of word
    words = {} #empty dict
    for line in f:
        line = line[:-1]
        new_min = distance(a, line)
        if new_min <= minn:
            minn = new_min
            words[line] = new_min
    words = sorted(words.items(), key=lambda x: x[1])
    return list(map(lambda x: x[0], words[:10]))

dict_alp = {}
w = []

def pred_algirithmLeviirithmNGramm():
    global w
    f = open('words.txt')
    for line in f:
        line = line[:-1]
        if len(line) < 3:
            w.append(line)
        else:
            n_gramm_line = n_gramm(line)

            for j in n_gramm_line:
                    try:
                            dict_alp[j].append(line)
                    except KeyError:
                            dict_alp[j] = [line]


def algirithmLeviirithmNGramm(a):
    global w
    n_gramm_a = n_gramm(a)
    minn = len(a)
    for i in n_gramm_a:
        try:
            w += (dict_alp[i])
        except Error:
            pass
    w = sorted(list(set(w)))

    words = {}
    for line in w:
        new_min = distance(a, line)
        if new_min <= minn:
            minn = new_min
            words[line] = new_min
    words = sorted(words.items(), key=lambda x: x[1])
    return list(map(lambda x: x[0], words[:10]))


print("Write some word: ")
someword = input()

print("algorithm with ONLY Levi distance")
print()
start = time.time()
print(algirithmLevi(someword))

done = time.time()
currentime = done - start

print("Current time: ")
print(currentime)

print()
print("algorithm with Levi distance + ngram")
pred_algirithmLeviirithmNGramm()
start = time.time()

print(algirithmLeviirithmNGramm(someword))

done = time.time()
currentime = done - start
print("Current time: ")
print(currentime)
