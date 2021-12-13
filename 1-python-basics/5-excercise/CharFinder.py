# TODO: Fix this mess of a naming

# Little demo I can do with them, purpose to see if they got the basics...

# Make this program, Ask a user for a char then a sentence to count the
# times that char occurred in the sentence.

# BONUS: Ask for a word, search a text and count the times you find that word in the text.
# Extra bonus make a GUI

# Makes sense:
new_lines = '\n\n\n\n'
ask_correct_input = 'Is this correct? [Y/n]'
ask_user_char = 'Please fill in a char\n'
ask_user_string = 'Please give a string of chars: '
flag_correct_input = 'Y'


# Ask user for char input:

while True:
    search_char_value = input(ask_user_char)[:1]
    print(F'{"Chosen value is: "} {search_char_value}')
    is_correct_char = input(ask_correct_input)[:1]
    if is_correct_char == flag_correct_input:
        print('Hooray!')
        break
    else:
        print(new_lines)

# Ask user for a searchable sentence:

while True:
    search_sentence_value = input(ask_user_string)
    is_correct_sentence = input(ask_correct_input)
    if is_correct_sentence == flag_correct_input:
        break
    else:
        print(new_lines)

print(F'{"The char:"} {search_char_value} {"has occurred:"} {search_sentence_value.count(search_char_value)}{"times."}')
