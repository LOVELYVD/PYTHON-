import logging
from abc import abstractmethod

from eliza import Eliza

class ElizaState():
    def __init__(self, hystericeliza):
        self.hystericeliza = hystericeliza

    @abstractmethod
    def switch_state(self, output):
        """ Decide how to react next based on the current output """
 
    @abstractmethod
    def process_output(self, output):
        """ React on the current output by formatting it according to the state """

"""implementing class Sad """
class Sad(ElizaState):
    """ answer only in lowercase (use String.lower() to do this) """
    def switch_state(self,output):
        if output.startswith("Do "):
           self.hystericeliza.upgraded_state(Normal(self.hystericeliza))

    def process_output(self, output):
       return output.lower()

"""implementing class Angry """
class Angry(ElizaState):
    """ ANSWER ONLY IN UPPERCASE (use String.upper() to do this) """
    def switch_state(self,output):
        if output.startswith("Do you") or output.startswith("Please"):
           self.hystericeliza.upgraded_state(Normal(self.hystericeliza))
        elif output.startswith("Why"):
           self.hystericeliza.upgraded_state(Sad(self.hystericeliza))

    def process_output(self, output):
       return output.upper()

"""implementing class Normal """
class Normal(ElizaState):
    """ Answer normally """
    def switch_state(self,output):
       if output.startswith("Please"):
           self.hystericeliza.upgraded_state(Sad(self.hystericeliza))
       elif "n't " in output:
           self.hystericeliza.upgraded_state(Angry(self.hystericeliza))

    def process_output(self, output):
       return output
           
class HystericEliza():
    def __init__(self):
        self.eliza = Eliza()
        self.state = Normal(self)
    def upgraded_state(self,state):
        self.state = state
    def load(self, replies):
        self.eliza.load(replies)
        
        """Change process_output to a more object-oriented variant
          implementing the statepattern and not relying on hardcoded strings anymore"""
        """ implemented switching states in process_output to be  flexible"""

    def process_output(self, output):
        self.state.switch_state(output)
        return self.state.process_output(output)
        
    def run(self):
        initial = self.process_output(self.eliza.initial())
        print(initial)

        while True:
            sent = input('> ')

            output = self.eliza.respond(sent)
            if output is None:
                break
            
            formatted = self.process_output(output)
            print(formatted)

        final = self.process_output(self.eliza.final())
        print(final)

def main():
    eliza = HystericEliza()
    eliza.load('doctor.txt')
    eliza.run()

if __name__ == '__main__':
    logging.basicConfig()
    main()
