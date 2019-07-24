from pptree import *
import os


def get_first_word(line):
    if line is "":
        return
    words = line.split()
    if len(words) > 0:
        first_word = words[0]
        return first_word


def add_node(current, line):
    if current is None:
        return Node("head" + line, None)
    else:
        return Node(line, current)


with open("/home/vagrant/openu/prolog/trace_monkey.txt", 'r') as trace_file:
    current = None

    while True:
        line = trace_file.readline()
        if line.strip() == "":  # run till it face an empty string.
            break
        first_word = get_first_word(line)
        if current is None:
            call_tree = add_node(current, line)
            current = call_tree
        elif first_word == "Call:":
            current = add_node(current, line)
        elif first_word == "Exit:":
            add_node(current, line)  # get_assignment(line))
            current = current.parent
        elif first_word == "Fail:":
            add_node(current, line)
            current = current.parent
        elif first_word == "Redo:":
            current = add_node(current, line)

print_tree(call_tree)
