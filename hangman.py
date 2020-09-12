import random
import time

class Hangman:

    def __init__(self):
        print("\n-: Welcome To Hangman Game :-")
        name = input("\nEnter Your Name : ")
        print("\nHello {}!, All The Best..!!".format(name))
        print("\nLet's Play..")
        time.sleep(1)

    def loop(self):
        x = (input("\nDo you want to play again(y/n) : ")).lower()
        if x == 'y' or x == '':
            self.main()
            self.play()
        else:
            print("\nBye.. Bye..!!")
            time.sleep(1)
            exit()
            
    def main(self):
        self.display = ''
        global guesses; guesses = []
        
        with open("words.txt",'r') as file:
            words = file.read().split()
        self.word = random.choice(words).lower()
        char = len(self.word)//3

        for i in range(char):
            hidden = random.choice(self.word)
            guesses.append(hidden)
        for letter in self.word:
            if letter in guesses:
                self.display += letter
            else:
                self.display += '_'
                
    def play(self):
        t = 0
        
        print("\nThis is the word : "+self.display) 
        while t < 5 and self.display != self.word:
            show = self.display
            guess = (input("\nEnter a character : ")).lower()
            if guess in self.word:
                if guess in guesses:
                    print("\nAlready Exist..!!")
                    print("\nThis is the word : "+show)
                else:
                    self.display = ''
                    guesses.append(guess)
                    for letter in self.word:
                        if letter in guesses:
                            self.display += letter
                        else:
                            self.display += '_'            
                    print("\nThis is the word : "+self.display)
            else:
                print("\nInvalid Character")
                if 4-t != 0:
                    print("\nRemaining {} attempt..".format(4-t))
                print("\nThis is the word : "+show)
                t += 1
        else:
            if self.display == self.word:
                print("\nYou Win..!!")
            else:
                print("\nYou Lost..!!")
                print("\nAnswer is : "+self.word)
        self.loop()
    
hangman = Hangman()
hangman.main()
hangman.play()
