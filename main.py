# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#create Quiq class

class QuizApp:

    def __init__(self):
        self.username =""


    def startup(self):
        self.greeting()
        self.username = input("What is your name?")
        print(f"Welcome {self.username}!")
        print()


    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("-~-~-~-~-~-Welcome to PyQuiz-~-~-~-~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()


    def menu_header(self):
        print("------------------------------------")
        print("Please Make a selection:")
        print("(M): Repeat this menu")
        print("(L): List the quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")


    def menu(self):
        self.menu_header()

        #run unti the uxer exits the app
        selection =""
        while True:
            selection=input("Selection?")
            if(len(selection) == 0):
                self.menu_error()
                continue

            selection = selection.capitalize()
            if selection[0] == 'E':
                self.goodbye()
                break

            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == 'L':
                print("\nAvaialble quizzez are:")
                #Todo list the quiz
                print("-----------------------------")
                continue
            elif selection[0] == 'T':
                try:
                    quiznumber = int(input('quiznumber'))
                    print(f"You have selected quiz {quiznumber}")
                    #TODO start quiz
                except:
                    self.menu_error()

            else:
                self.menu_error()

    def run(self):
        #execute the startup routine - ask for name, print greetings, etc
        self.startup()
        #start the main program menu and run until the use exits
        self.menu()

if __name__ =="__main__":
    app = QuizApp()
    app.run()


#create QuizManager Class