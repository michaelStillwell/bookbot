COMP="""--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24613 times
The 'n' character was found 24367 times
The 's' character was found 21155 times
The 'r' character was found 20818 times
The 'h' character was found 19725 times
The 'd' character was found 16863 times
The 'l' character was found 12739 times
The 'm' character was found 10604 times
The 'u' character was found 10407 times
The 'c' character was found 9243 times
The 'f' character was found 8731 times
The 'y' character was found 7914 times
The 'w' character was found 7638 times
The 'p' character was found 6121 times
The 'g' character was found 5974 times
The 'b' character was found 5026 times
The 'v' character was found 3833 times
The 'k' character was found 1755 times
The 'x' character was found 677 times
The 'j' character was found 504 times
The 'q' character was found 324 times
The 'z' character was found 243 times
--- End report ---"""

def char_count(text):
    chars = {}

    for c in text:
        if not c.isalpha():
            continue

        if c.lower() in chars:
            chars[c.lower()] += 1
        else:
            chars[c.lower()] = 1

    return chars


def word_count(text):
    return len(text.split())


def main():
    res = []
    res.append("--- Begin report of books/frankenstein.txt ---")
    wc = None
    cc = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wc = word_count(file_contents)
        cc = char_count(file_contents)

    if wc is None:
        wc = 0
    if cc is None:
        cc = {}

    res.append(f"{wc} words found in the document")
    res.append("")
    for k in sorted(cc, key=cc.get, reverse=True):
        res.append(f"The '{k}' character was found {cc[k]} times")

    res.append("--- End report ---")
    print("\n".join(res))


    print()
    t = COMP == "\n".join(res)
    print(f"Same: {t}")

    print()
    if not t:
        cs = COMP.split("\n")
        print(range(0, len(cs)))
        for i in range(0, len(cs)):
                print(f"{cs[i]}\t|\t{res[i]}\t|\t{cs[i] == res[i]}")
    

main()
