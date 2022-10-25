from curses.ascii import isdigit
from sre_compile import isstring
import random
from flask import Flask
app = Flask(__name__)
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favourite_animal(users_animal):
    """Display a message to the user that changes based on their favourite animal"""
    return f'Wow, {users_animal} is my favourite animal too!'

@app.route('/dessert/<users_dessert>')
def favourite_dessert(users_dessert):
    return f'How did you know I like {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):  
    return f"You are a truly {adjective} {noun}"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    is_num_1 = number1.isdigit()
    is_num_2 = number2.isdigit()
    if is_num_1 == False or is_num_2 == False:
        return f'Invalid Inputs. Please try again by entering 2 numbers!'
    else:
        number1 = int(number1)
        number2 = int(number2)
        total = number1 * number2
        return f"{number1} times {number2} is {total}."

    
@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
        is_word = word.isalpha()
        is_num = n.isdigit()
        
        if is_word == False or is_num == False:
            return f'Invalid input. Please try again by entering a word and a number!'
        else:
            n = int(n)
            answer = f'{word} '   
            answer = answer * n 
            return f'{answer}'

@app.route('/dicegame')
def dicegame():
    roll = random.randint(1,6)
    if roll == 6:
        return f'You rolled a {roll}. You won!'
    else:
        return f'You rolled a {roll}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)
