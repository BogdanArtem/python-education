""" Module for iterator implementation """

from string import ascii_letters


class SentenceIterator:
    """Iterator for Sentence"""
    def __init__(self, words):
        self.words = words
        self.counter = 0
        self.end = len(self.words)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.end:
            result = self.words[self.counter]
            self.counter += 1
            return result
        raise StopIteration


class Sentence:
    """Sentence that generates words form text dynamically"""
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("The type of variable is not str")
        # The sentence is finished
        if text[-1] not in ('!', '.', '?'):
            raise ValueError("Please, end your sentence")

        self.text = text[0:-1]

    def __getitem__(self, items):
        """Return items from sentence """
        return list(self._words())[items]

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def _words(self):
        """Generate infinite sequence of words from text"""
        word = ""
        for letter in self.text:
            if letter != " ":
                word += letter
            else:
                yield word
                word = ""
        yield word

    @property
    def words(self):
        """Filter out words that don't have ascii letters"""
        return [word for word in self._words() if set(word).issubset(set(ascii_letters))]

    @property
    def other_chars(self):
        """Filter out words that have ascii letters"""
        return [word for word in self._words() if not set(word).issubset(set(ascii_letters))]



if __name__ == '__main__':
    # Accepts only string
    print("*" * 50)
    try:
        Sentence(23534534)
    except TypeError:
        print("Calling Sentence(23534534)...")
        print("Raised TypeError")
    print("*" * 50)

    # Accepts only finished strings
    try:
        print("Calling Sentence('sdsd dfdfdf')")
        Sentence("sdsd dfdfdf")
    except ValueError:
        print("Raised ValueError")
    print("*" * 50)

    # Check __repr__
    print("String representation of 'lazy !!! fox d*6 &&& dog.'")
    print(Sentence("lazy !!! fox d*6 &&& dog."))
    print("*" * 50)

    # Lazy iterator
    print("Calling Sentence('lazy fox jumps over the brown dog.')._words()")
    print(Sentence("lazy fox jumps over the brown dog.")._words())
    print("*" * 50)

    # List of all words
    print("Calling Sentence('lazy !!! fox d*6 &&& dog.').words")
    print(Sentence("lazy !!! fox d*6 &&& dog.").words)
    print("*" * 50)

    # List of not words
    print("Calling Sentence('lazy !!! fox d*6 &&& dog.').other_chars")
    print(Sentence("lazy !!! fox d*6 &&& dog.").other_chars)
    print("*" * 50)

    # Index
    print("Calling Sentence('lazy !!! fox d*6 &&& dog.')[:]")
    print(Sentence('lazy !!! fox d*6 &&& dog.')[:])
    print("*" * 50)

    # Slice
    print("Calling Sentence('lazy fox jumps over the brown dog.')[0:2]")
    print(Sentence('lazy fox jumps over the brown dog.')[0:2])
    print("*" * 50)

    # Iterator
    print("Returning iterator from Sentence")
    print(type(iter(Sentence("lazy fox jumps over the brown dog."))))
    print("*" * 50)

    # For
    print("Calling Sentence('lazy fox !!! jumps .... over the brown dog.')")
    for item in Sentence("lazy fox !!! jumps .... over the brown dog."):
        print(item)
    print("*" * 50)
