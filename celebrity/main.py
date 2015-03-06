import celebrity
import numpy
import sys

# helper functions

def print_usage():
    print("Usage: main.py [options] number_of_people")
    print("")
    print("Options:")
    print("  --help              Print this help.")
    print("  --linear            Solve with linear algorithm (optional).")
    print("  --quadratic         Solve with quadratic algorithm (optional).")
    print("")
    print("Arguments:")
    print("  number_of_people    Number of people (mandatory).")

def random_relationships(people):
    rand_rel = numpy.random.random_integers(0,1,(people,people))
    for i in range(0,people):
        rand_rel[i][i] = 888 # just for printing purposes
    return rand_rel

# check arguments

if len(sys.argv) < 2:
    print_usage()
    exit(0)

# parse parameters

people        = -1
use_linear    = False
use_quadratic = False

for i in range(1,len(sys.argv)):
    if sys.argv[i] == "--help":
        print_usage()
        exit(0)
    elif sys.argv[i] == "--linear":
        use_linear = True
    elif sys.argv[i] == "--quadratic":
        use_quadratic = True
    else:
        try:
            people = int(sys.argv[i])
        except (TypeError, ValueError):
            print("ERROR: \"%s\" is not a valid argument." % (sys.argv[i]))
            print("Call with --help for usage hints.")
            exit(1)

# if no algorithm specified, use both
if not use_linear and not use_quadratic:
    use_linear = True
    use_quadratic = True

# execute

relationships = random_relationships(people)
print(relationships, end="\n\n")

if use_linear:
    result = celebrity.solve_linear(relationships)
    if result < 0:
        print("Linear...: there is no celebrity in this group")
    else:
        print("Linear...: the celebrity is person", result)

if use_quadratic:
    result = celebrity.solve_quadratic(relationships)
    if result < 0:
        print("Quadratic: there is no celebrity in this group")
    else:
        print("Quadratic: the celebrity is person", result)
