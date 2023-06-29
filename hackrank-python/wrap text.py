import textwrap

def wrap(string, max_width):
    text = textwrap.fill(string, max_width)
    return text

''' textwrap is module for wrapping text. as for fill is stand from
    "\n".join(wrap(string, width)) so if you want to separate list of words with certain 
    length, you can easily use this modul instead of spending time to creating 
    unnecessary logic
'''

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)