#EXERCISE 1
zipcode = "02132"
#print (zipcode)

#Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'
#For each of the following expressions, write the value of the expression and the type (of the
#value of the expression).
#• 'width/2'
#• 'width/2.0'
#• 'height/3'
#• '1 + 2 * 5'
#• 'delimiter * 5'
#Use the Python interpreter to check your answers.

new_width = width/2
#print (new_width)

new_width2 = width/2.0
#print(new_width2)

new_height = height/3
#print(new_height)

num = 1 + 2 * 5
#print(num)

new_del = delimiter * 5
#print(new_del)

#USING PYTHON INTERPRETER TO CHECK ANSWERS
type(new_del)

#type new width
type(new_width)

#type new_width2
type(new_width2)

#type new_height
type(new_height)

#type num
type(num)

#type new_del
type(new_del)



#EXERCISE 4





#EXERCISE 1

#NAME ERROR: name 'repeat_lyrics' is not defined 


#EXERCISE 2

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I‚m a lumberjack, and I‚m okay.")
    print("I sleep all night and I work all day.")

#repeat_lyrics()


def cat_twice(part1, part2):
    cat = part1 + part2
    print(cat)
    print(cat)
#cat_twice(5, 7)



#EXERCISE 3
    
def right_justify(s):
    print('                                                                  ' + s)
#right_justify('allen')



#EXERCISE 4
    
def do_twice():
    #print('Box')
    #print_spam() 
    #print_spam()
    print_twice()
def print_spam():
    print('spam')


def do_four(value):
    print_twice()
    print_twice()
def print_twice():
    print('Hello')
    print('Hello')

#do_four('hello')


#EXERCISE 5
def box():
    print('+--------+--------+')
    print('/        '      '/        '      '/')
    print('/        '      '/        '      '/')
    print('/        '      '/        '      '/')
    print('/        '      '/        '      '/')
    print('+--------+--------+')
    print('/        '      '/        '      '/')
    print('/        '      '/        '      '/')
    print('/        '      '/        '      '/')
    print('/        '      '/        '      '/')
    print('+--------+--------+')

#box()
