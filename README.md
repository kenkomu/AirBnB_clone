**Description**
This is a team project to buila a clone of AirBnB
The console is a command interpreter that manages objects of distraction between objects and their storage.
The console creates a new object, retrieve an object from a file, do operations on objects and destroys an object.

All classes are handled by Storage engine in the FileStorage class.

**Installation**
git clone https://github.com/shiku-mwethukia/AirBnB_clone.git
cd to AirBnB and run the command:

./console.py

**Execution**

In interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

**Tests**

All tests are defined in the tests folder and the codes tested with the unittest module.

**Documentation**

*Modules:

'print(__import__("my module").__doc__)'

*Classes:

python3 -c 'print(__import__("my_module").MyClass.__doc__)'

*Functions(Inside and outside a class):

python3 -c 'print(__import__("my_module").my_function.__doc__)'

and

python3 -c 'print(__import__("my_module").MyClass.my_function.doc__)'

**Usage**

Start console in interactive mode:

$ ./console.py
(hbnb)

*Use help to see available commands:

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF all count create destroy help quit show update

(hbnb)

*Quit the console:

(hbnb) quit
$

Authors
*Mary Mwethukia marymwethukia65@gmail.com
*Kenneth Komu kenkomu@gmail.com
