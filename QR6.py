def GetWordsFromUser(min, max):
    while True:
        try:
            sentence= str(input("Enter the word / words: "))
            words=sentence.split()
            for i, word in enumerate(words):
                if len(word) < min or len(word)> max:
                    raise Exception
                else:
                    words[i]=word.lower()
            return words
        except:
             print("Words out of range. Try again!!!") 
print(GetWordsFromUser(2,10))                   



