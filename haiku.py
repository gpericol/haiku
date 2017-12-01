# -*- coding: utf-8 -*-
"""
    haiku.py
    ~~~~~~~~
    A funny class that generates haiku in ITALIAN language
    using Markov Chains and some graceful brute force   
    :copyright: (c) 2017 by Gianluca Pericoli.
    :license: GPLv3
"""
import unicodedata
import markovify

class Haiku:
    input_file = "input.txt"
    # Some magic numbers here
    letters_per_syllable = 6 # keep in mind also spaces on character count 
    overlap_ratio = 0.8
    overlap_total = 25

    markov = {}
    used_sentences = []

    def __init__(self):
        with open(self.input_file) as f:
            text = f.read()

        self.markov = markovify.Text(text)
        
    
    def _strip_accents(self, word):
        """Strips accents of a word for syllable division"""
        try:
            word = unicode(word, 'utf-8')
        except NameError:
            pass
        word = unicodedata.normalize('NFD', word)
        word = word.encode('ascii', 'ignore')
        word = word.decode("utf-8")
        return str(word)

    def _is_vowel(self, c):
        """Return true if a letter is a vowel"""
        vowels = "AEIOU"
        return vowels.find(c) != -1

    def _get_char(self, word, index):
        """
        Get the character in index position on the word or return empty string
        used for avoiding out of range errors
        """
        if len(word) > 0 and index < len(word):
            return word[index]
        return ""

    def _divide(self, word):
        """Returns the coununt of syllables and the input word divided"""
        _sg = "SG"
        _rlh = "RLH"
        _i = "I"
        _qu = "QU"
        _iu = "IU"

        word = self._strip_accents(word).upper()
        result = ""
        index = 0
        count = 0

        while index < len(word):
            if not self._is_vowel( word[index] ):
                result += word[index]
            elif not self._is_vowel( self._get_char(word, index+1) ):
                if index+2 >= len(word):
                    result += word[index:index+2] + "-"
                    index += 1
                    count += 1
                elif self._is_vowel( self._get_char(word, index+2) ):
                    result += word[index] + "-"
                    count += 1
                elif self._get_char(word, index+1) == self._get_char(word, index+2):
                    result += word[index:index+2] + "-"
                    index += 1
                    count += 1
                elif _sg.find( self._get_char(word, index+1) ) != -1:
                    result += word[index] + "-"
                    count += 1
                elif _sg.find( self._get_char(word, index+2 )) != -1:
                    result += word[index] + "-"
                    count += 1
                else:
                    result += word[index:index+2] + "-"
                    index += 1
                    count += 1
            elif _i.find( self._get_char(word, index+1) ) != -1:
                if index > 1 and word[ index-1: index+1] == _qu and self._is_vowel( self._get_char(word, index+2) ):
                    result += word[index:index+2]
                    index += 1
                elif self._is_vowel( self._get_char(word, index+2) ):
                    result += word[index] + "-"
                    count += 1
                else:
                    result += word[index]
            elif _iu.find(word[ index ]) != -1:
                result += word[index]
            else:
                result += word[index] + "-"
                count += 1
            index += 1
        
        if self._get_char(result, -1) == "-":
            result = result[:-1]

        return [count, result]

    def _find_divided(self, tot_syllables):
        """Generates a sentence of tot_syllables syllables"""
        found = False

        while not found:
            sentence = self.markov.make_short_sentence(
                tot_syllables * self.letters_per_syllable, 
                tries = 100,
                max_overlap_ratio = self.overlap_ratio,
                max_overlap_total = self.overlap_total
            )
            
            # prevent None sencences
            if sentence == None:
                continue
            
            words = sentence.split()
            tot = 0
            for word in words:
                tot += self._divide(word)[0]
            if tot == tot_syllables and not sentence in self.used_sentences:
                found = True

        self.used_sentences.append(sentence)
        return sentence

    def generate(self):
        return [
            self._find_divided(5),
            self._find_divided(7),
            self._find_divided(5)

        ]

def main():
    h = Haiku()
    for i in range(10):
        sentences = h.generate()
        print "***"
        print sentences[0]
        print sentences[1]
        print sentences[2]
        print "*** \n\n"

if __name__ == "__main__":
    main()