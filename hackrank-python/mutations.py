def mutate_string(string, position, character):
    teks = list(string)
    teks[position] = character
    teks = ''.join(teks)
    return teks

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)