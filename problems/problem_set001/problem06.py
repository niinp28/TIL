# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    new_ord = 0
    new_word = ''
    for spellings in word:
        new_ord = ord(spellings) + n
        if new_ord > 122:
            new_ord -= 26
        new_word += chr(new_ord)
    return new_word
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx