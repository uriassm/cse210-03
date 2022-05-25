class LettersGuessed:

    def __init__(self):
        '''Constructs a new letter guessed
        
        Args:
        self: An instance of guessed letter.'''
        self._guessed_letter = ''


    def get_guessed_letter(self):
        return self._guessed_letter

    def update_guessed_letter(self, letter):
        self._guessed_letter = letter
        #self._past_letters.append(letter)