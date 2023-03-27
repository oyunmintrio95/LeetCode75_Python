'''
파일명: day2_isSubsequence.py
Description:
생성일 : 3/27/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''

def isSubsequence(s: str, t: str) -> bool:
    s_len = len(s)
    t_len = len(t)

    i = 0
    j = 0

    if s_len<1:
        return True

    while i < t_len:
        if t[i:i+1]==s[j:j+1]:
            j+=1
        i+=1

        if j == s_len:
            return True

    return False

def main():
    s= 'abc'
    t = 'ahbgdc'

    print(isSubsequence(s,t))


main()
