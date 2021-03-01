import random
import string

class SolitaireCipher:
    __deck= []
    __stream = []
    __originalText = ''
    __encryptedText = ''
    __decryptedText = ''
    __alphabet = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
    }

    def __init__(self, message, stream=[]):
        self.__originalText = message
        if len(self.__stream) == 0:
            self.__fill_deck()

    def __fill_deck(self):
        for i in range(1, 29):
            num_insert = random.randint(1, 28)
            while num_insert in self.__deck:
                num_insert = random.randint(1, 28)
            self.__deck.append(num_insert)


    def __generate_keystream(self):
        # find the joker A
        joker_a = self.__deck.index(27)
        if joker_a == len(self.__deck) - 1 :
            extra = self.__deck[0]
            self.__deck[0] = self.__deck[joker_a]
            self.__deck[joker_a] = extra
            joker_a = 0
        else:
            extra = self.__deck[joker_a+1]
            self.__deck[joker_a+1] = self.__deck[joker_a]
            self.__deck[joker_a] = extra
            joker_a = joker_a + 1
        # find the joker B
        joker_b = self.__deck.index(28)
        if joker_b + 2 > len(self.__deck) - 1:
            for i in range(0, 2):
                extra = self.__deck[i]
                self.__deck[i] = self.__deck[joker_b]
                self.__deck[joker_b] = extra
                joker_b = i
        else:
            for i in range(joker_b+1, joker_b+3):
                extra = self.__deck[i]
                self.__deck[i] = self.__deck[joker_b]
                self.__deck[joker_b] = extra
                joker_b = i
        # triple cut
        if joker_a < joker_b: # a joker is closer to top
            top = self.__deck[0:joker_a]
            middle = self.__deck[joker_a:joker_b+1]
            bottom = self.__deck[joker_b+1: len(self.__deck)]
            self.__deck = bottom + middle + top
        else: # b joker is coler to top
            top = self.__deck[0:joker_b]
            middle = self.__deck[joker_b:joker_a+1]
            bottom = self.__deck[joker_a+1: len(self.__deck)]
            self.__deck = bottom + middle + top
        # count from bottom card
        last_num = self.__deck[len(self.__deck)-1]
        if last_num == 28:
            last_num == 27
        top = self.__deck[0:last_num]
        bottom = self.__deck[last_num:len(self.__deck)-1]
        self.__deck = bottom + top
        self.__deck.append(last_num)
        # count from first card
        first_num = self.__deck[0]
        NEXT = self.__deck[first_num-1]
        return NEXT

    def __get_Key(self, val):
        for key, value in self.__alphabet.items():
            if val == value:
                return key
        return "missing"

    def encrypt(self):
        self.__stream = []
        self.__originalText=self.__originalText.translate({ord(c): None for c in string.whitespace})
        self.__originalText=self.__originalText.upper()
        num = len(self.__originalText)
        if len(self.__stream) == 0:
            for i in range(num):
                key = self.__generate_keystream()
                while(key == 27 or key == 28):
                    key = self.__generate_keystream()
                self.__stream.append(key)
        # encrypted message
        for i in range(num):
            value = self.__alphabet[self.__originalText[i]]
            valueStream = self.__stream[i]
            sum = value + valueStream
            if sum > 26:
                sum = sum - 26
            letter = self.__get_Key(sum)
            self.__encryptedText += letter

    def get_encryption(self):
        return self.__encryptedText

    def decrypt(self):
        num = len(self.__encryptedText)
        for i in range(num):
            value = self.__alphabet[self.__encryptedText[i]]
            valueStream = self.__stream[i]
            if value <= valueStream:
                value = value + 26
            sub = value - valueStream
            letter = self.__get_Key(sub)
            self.__decryptedText += letter

    def get_decryption(self):
        return self.__decryptedText

    def get_stream(self):
        return self.__stream
