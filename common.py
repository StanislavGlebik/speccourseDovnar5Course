
def fail(message):
  print message
  exit(1)

def checkElementAttribute(element, attr):
  if not element.hasAttribute(attr):
    fail("No " + attr + " attribute in " + element.tagName)
  else:
    return element.getAttribute(attr)
