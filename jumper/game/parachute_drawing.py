class ParachuteDrawing:
    '''Creates the initial drawing of the man and parachute. 
    
    The responsibility of the class is to do updates to the drawing
    as the game is played and let the director know when the game is 
    over because of too many wrong answers.
    
    Attributes:
         _drawing_parts(List(strings)): List of strings needed to create the drawing.'''


    def __init__(self):
        '''Constructs a new drawing
        Args: self (ParachuteDrawing): An instance of parachutedrawing'''

        self._drawing_parts = ['  ___', ' /___\\', ' \\   /', '  \\ /', '   0', '  /|\\', '  / \\', '', '^^^^^^^']

    def create_drawing(self):
        '''Iterates through the list of parts needed for the 
        drawing and prints the drawing for the user to see.
        
        Args:
            self(ParachuteDrawing): an instance of parachutedrawing'''
        for i in self._drawing_parts:
            print(i)

    def update_drawing(self, word_selection):
        '''Determines of the user guessed a letter correctly and updates
        the drawing if the guess was incorrect.
        
        Args:
            self(ParachuteDrawing): an instance of parachute drawing.
            word_selection: an instance of the word_selection class. '''
        if word_selection.get_correct_guess() == False:
            self._drawing_parts.pop(0)
        if len(self._drawing_parts) == 5:
            self._drawing_parts[0] = '   x'

    def parachute_gone(self):
        '''Returns a boolean to know if the parachute has been cut enough to
        end the game as a loss. 
        
        Args:
            self(ParachuteDrawing): and instance of parachute drawing.'''
        return (len(self._drawing_parts) == 5)

    
