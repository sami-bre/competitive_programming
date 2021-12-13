class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        numbers = []
        for i in range(len(words)):
            numbers.append(words[i][-1:])
            words[i] = words[i][:-1]
            
        # do a bubble sort on numbers but also shuffle the words
        for number in numbers:
            for i in range(len(numbers)):
                if(i == len(numbers)-1):
                    continue
                if(numbers[i] > numbers[i+1]):
                    # swap both in the numbers and words arrays
                    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                    words[i], words[i+1] = words[i+1], words[i]
                           
        return " ".join(words)
