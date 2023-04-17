def swap_case(s):
    result = ''
    for x in s:
        if x.isupper() == True:
            x = x.lower()
        else:
            x = x.upper()
        result += x
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)