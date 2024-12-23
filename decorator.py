def dec1(func):
   def wrapper():
      print('*********')
      func()
      print('*********') 
   return wrapper
@dec1
def great():
   print('wellcome !')

great()   