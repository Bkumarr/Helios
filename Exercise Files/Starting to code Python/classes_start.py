#
# Example file for working with classes
#
class learn_py():

  def method1(self):
    print("my pythonista method")
  
  def method2(self, somestring):
    print("one more method" +" " +somestring)
  
class learn_py3(learn_py):

  def method1(self):
    learn_py.method1(self)
    print("MY PYTHONISTA CLASS")
  
  def method2(self, somestring):
    print("one more method" +" " +somestring)

def main():
  rt = learn_py()
  rt.method1()
  rt.method2('Happy code day!')

  l2 = learn_py3()
  l2.method1()
  l2.method2("HAPPY CODE DAY!")


main()
