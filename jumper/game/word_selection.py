import random

class WordSelection:
    '''Chooses the word that will be used for one round of the game.
    
    The responsibility of this class is to randomly choose a word from a list
    and compare the letters guessed by the user to the letters in the word.
    
    Arrtibutes:
        _word_list (List[strings]): list of words to be used in the game. 
        _selected_word (string): the word that will be used for the duration of the game. 
        _selected_word_list(List[strings]): the individual letters of the selected word.
        _hidden_word(List[strings]): list of letters found that will be shown to the user.
        _correct_guess(Boolean): Keeps track of whether the last user input was correct.  
        '''

    def __init__(self):
        '''Constructs a new word selection
        Args:
            self (word selection): an instance of WordSelection.
            '''
        self._word_list = ['start', 'hello', 'times', 'power', 'roles', 'river', 'drive', 'chair', 'light', 'faith']
        self._selected_word = self._word_list[random.randint(0, 9)]
        self._selected_word_list = []
        for i in range(len(self._selected_word)):
            letter = self._selected_word[i]
            self._selected_word_list.append(letter)
        self._hidden_word = ['_', '_', '_', '_', '_']
        self._correct_guess = True

    def get_selected_word(self):
        '''Get the selected word for the current instance. 
        Args:
            self (selected word): an instance of WordSelection'''
        return self._selected_word

    def get_hidden_word(self):
        '''Gets the hidden word to show to the user.
        Args:
            self (selected word): an instance of WordSelection'''
        single_string_hidden_word = ' '.join(self._hidden_word)
        return single_string_hidden_word

    def compare_letters(self, letters_guessed):
        '''Takes the letter the user input and tries to find it
        within the selected word. 
        Args:
            self(WordSelection): and instance of WordSelection
            letter: the letter the user input in the terminal'''
        
        letter = letters_guessed.get_guessed_letter()
        if letter in self._selected_word_list:
            letter_index = self._selected_word_list.index(letter)
            self._selected_word_list[letter_index] = '_'
            self._hidden_word[letter_index] = letter
            self._correct_guess = True
        else:
            self._correct_guess = False

    def word_found(self):
        '''Looks at the hidden word to see if a letter has not been guessed yet.
        Args:
            self (selected word): an instance of WordSelection'''
        space = '_'
        return (space in self._hidden_word)

    def get_correct_guess(self):
        '''Gets the boolean to see if the last guess was correct
        Args:
            self (selected word): an instance of WordSelection'''
        return self._correct_guess
