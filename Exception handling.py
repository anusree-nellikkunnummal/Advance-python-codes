'''
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:
'''
# The try block lets you test a block of code for errors
# The critical operation which can raise an exception is placed inside the try clause
def div_num(num1,num2):

    try:
        print(num1/num2)
    # The except block lets you handle the error.
    except TypeError as e:
        print('invalid number', e)
    except ZeroDivisionError as e:
        print('Zero is not acceptable')
    except NameError as e:
        print('invalid parameter', e)
    except Exception as e:
        print('something went wrong')
    # The else block lets you execute code when there is no error.
    else:
         print('No exceptions')
    # The finally block lets you execute code, regardless of the result of the try- and except blocks.
    finally:
        print('program ends here..')

div_num(5,6)
div_num(5,0)
div_num('a', 'b')
div_num(10,-1)