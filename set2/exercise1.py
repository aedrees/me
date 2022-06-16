"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"] 
# I think this will print "what, does, this, line, do, ?" by calling the lists variables
for word in some_words:
    print(word) #it printed what, does, this, line, do, ? as word.
# I think this will print the same: "what, does, this, line, do, ?" 
for x in some_words:
    print(x) #it printed what, does, this, line, do, ? same as above.
# I think this might print "what, does, this, line, do, ?" 
print(some_words) #it printed ['what', 'does', 'this', 'line', 'do', '?']
# I think this might print the text between the "".
if len(some_words) > 3:
    print("some_words contains more than 3 words") #it printed some_words contains more than 3 words.


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # it printed "uname_result(system='Darwin', node='z20.local', release='20.6.0', version='Darwin Kernel Version 20.6.0: Tue Feb 22 21:10:41 PST 2022; root:xnu-7195.141.26~1/RELEASE_X86_64', machine='x86_64')""


usefulFunction()
