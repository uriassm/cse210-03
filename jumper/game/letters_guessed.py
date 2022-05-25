class LettersGuessed:

    def __init__(self):
        '''Constructs a new letter guessed
        
        Args:
        self: An instance of guessed letter.'''
        self._guessed_letter = ''


    def get_guessed_letter(self):
        '''Gets the most recent letter that was guessed.
        
        Args:
            self(LettersGuessed): an instance of lettersguessed.'''
        return self._guessed_letter

    def update_guessed_letter(self, letter):
        '''Updates what the most recent letter was.
        
        Args:
            self(LettersGuessed): an instance of lettersguessed.
            letter: the letter the user input in the terminal. '''
        self._guessed_letter = letter