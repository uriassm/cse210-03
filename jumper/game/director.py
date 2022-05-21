from game.word_selection import WordSelection
from game.parachute_drawing import ParachuteDrawing
from game.letters_guessed import LettersGuessed
from game.terminal_service import TerminalService

class Director:
    '''A person who directs the game.
    
    The responsibility of the director is to control the sequence of play.
    
    Attributes:
        _word_selector: The one who selects the word and compares the guessed letters
        _guessed_letters: the letters the user will input and where it is maintained
        _parachute_drawing: drawing that determines how long the game lasts
        _terminal_service: will get inputs and display outputs
        '''

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_selector = WordSelection()
        self._letters_guessed = LettersGuessed()
        self._parachute_drawing = ParachuteDrawing()
        self._terminal_service = TerminalService()
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            self._do_inputs()
            self._do_updates()
        self._do_outputs()

    def _do_outputs(self):
        '''Shows the user the parachute drawing as well as how many letters they
        have guessed. 
        
        Args:
            self(Director): an instance of director'''
        hidden_word = self._word_selector.get_hidden_word()
        self._terminal_service.write_text(hidden_word)
        self._parachute_drawing.create_drawing()

    def _do_inputs(self):
        '''Allows the user to guess a letter and updates what the current
        guessed letter is.
        
        Args:
            self(DIrector): and instance of director'''
        new_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self._letters_guessed.update_guessed_letter(new_letter)

    def _do_updates(self):
        '''Compares if the guessed letter is contained in the chosen word
        and updates the parachute drawing as needed. Also determines if 
        the game will continue. 
        
        Args:
            self (Director): and instance of director.'''
        self._word_selector.compare_letters(self._letters_guessed)
        self._parachute_drawing.update_drawing(self._word_selector)
        if self._word_selector.word_found() == False:
            self._is_playing = False
        if self._parachute_drawing.parachute_gone() == True:
            self._is_playing = False


