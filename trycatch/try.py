# try:
#   print(x)
# except:
#   print("An exception occurred")
  
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
  
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")



import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))