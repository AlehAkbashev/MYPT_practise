import turtle

input_files = open('list_of_commands.txt', 'r', encoding='UTF-8')
mail_index = input()
commands = input_files.readlines()
turtle.penup()

for number in mail_index:
    draw_rules = commands[int(number)].split(',')
    for rule in draw_rules:
        eval(rule)


input_files.close()
