from arraystack import ArrayStack

class Palindrome():
    def __init__(self):
        pass

    def isPalindrome(self, word):
        word = word.lower()
        s = ArrayStack()
        for i in range(len(word) // 2):
            s.push(word[i])
        if len(word) % 2 == 0:
            add = len(word) // 2
        else:
            add = len(word) // 2 + 1
        for i in range(len(word)//2):
            index = i + add
            #print(s.peek(), word[index])
            if(s.pop() != word[index]):
                return False
        return True

    def imp(self, words):
        file = open(words, "r", encoding="utf-8")
        lst = []
        for word in file.readlines():
            word = word[:-1]
            word = word.split()[0]
            if self.isPalindrome(word):
                lst.append(word)
        file.close()
        return lst


    def new(self, lst, output):
        file = open(output, "w")
        for i in lst:
            file.write(i + "\n")
        file.close()

p = Palindrome()
lst = p.imp("words.txt")
p.new(lst, "palindrome_en.txt")
lst = p.imp("base.lst")
p.new(lst, "palindrome_uk.txt")

