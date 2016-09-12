def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print "No"
    else:
        print "Yes"

def output(working):
    if is_triangle(a) + is_triangle(b) <= is_triangle(c):
        print 'no'
    else:
        print 'yes'


a = raw_input("Please enter a number: ")
b = raw_input("Please enter a number: ")
c = raw_input("Please enter a number: ")
result = is_triangle(int(a,b,))
