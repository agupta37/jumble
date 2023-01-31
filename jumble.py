class Jumble:
    def __init__(self, word_list, word):
        self.word_list = word_list
        self.word = word
        self.char_dict = {}

    def gen_char_dict(self):
        for ch in self.word:
            if ch in self.char_dict:
                self.char_dict[ch] += 1  # if a char repeats, the frequency is increased
            else:
                self.char_dict[ch] = 1

    def gen_sub_anagrams(self):
        for word in self.word_list:
            # creating a shallow copy of the dict else the main object will get affected
            char_dict_copy = self.char_dict.copy()
            match = True
            for ch in word:
                # to check if char exists in dict and if it had sufficient number of same characters needed
                if ch in char_dict_copy and char_dict_copy[ch] > 0:
                    char_dict_copy[ch] -= 1
                else:
                    match = False
                    break
            if match and word != self.word:
                print(word)
