import sys

N = 0
chains = []

def shiritori(words, chain):
    global N
    word = chain[-1]
    tail = word[-1]
    flag = False
    for i, w in enumerate(words):
        if w[0] == tail:
            flag = True
            shiritori(words[:i]+words[i+1:], chain+[w])
    if not flag:
        if len(chain) > N:
            N = len(chain)
            chains.append(chain)

def main(lines):
    words = lines[1].split()
    words.sort()
    if all([len(w)==1 for w in words]):
        print(' '.join(words))
    else:
        for i, w in enumerate(words):
            shiritori(words[:i]+words[i+1:], [w])
        max = 0
        for chain in chains:
            if len(chain) > max:
                ans_chain = chain
                max = len(chain)

        ans = ''
        for word in ans_chain:
            ans += ' ' + word
            words.remove(word)
        print(ans.lstrip())
        if words:
            print(' '.join(words))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
