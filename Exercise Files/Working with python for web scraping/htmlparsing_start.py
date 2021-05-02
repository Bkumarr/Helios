# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print ("Encountered comment:", data)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])




def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
    # open the sample HTML file and read it
  f = open("samplehtml.html")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)
  
  print ("%d meta tags encountered" % metacount)

main()
  