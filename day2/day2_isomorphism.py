'''
파일명: day2_isomorphism.py
Description:
생성일 : 3/26/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''

def isIsomorphic(s: str, t: str) -> bool:
    if s==None or t==None or len(s)!= len(t):
        return False

    map = {}

    for i in range(0,len(s)):
        char_s = s[i:i+1]
        char_t = t[i:i+1]

        if char_s in map:
            if map.get(char_s) != char_t:
                return False
        else:
            if char_t in map.values():
                return False
            map[char_s] = char_t


    return True


def main():
    s = "foo"
    t = "egg"
    print(isIsomorphic(s,t))


main()
