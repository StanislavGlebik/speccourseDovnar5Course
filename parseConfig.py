from xml.dom.minidom import parse

def fail(message):
  print message
  exit(1)

def checkElementAttribute(element, attr):
  if not element.hasAttribute(attr):
    fail("No " + attr + " attribute in " + element.tagName)
  else:
    return element.getAttribute(attr)

class Dimension:
  def __init__(self, element):
    self.table = checkElementAttribute(element, "table")
    self.name = checkElementAttribute(element, "name")
    self.field = checkElementAttribute(element, "field")
    self.factFk = checkElementAttribute(element, "fact_fk")

class Storage:
  def __init__(self, element):
    self.pathValue = checkElementAttribute(element, "path")
    self.aggregatedValueName = checkElementAttribute(element, "aggregated_value_name")
    self.factTable = checkElementAttribute(element, "fact_table")
    self.aggregatedValueField = checkElementAttribute(element, "aggregated_value_field")
    self.dimension = []

    dimensionsHolder = element.getElementsByTagName("dimensions")
    if len(dimensionsHolder) > 1:
      fail("Too many dimensions elements!")
    if len(dimensionsHolder) == 0 :
      fail("No dimensions elements!")

    dimensionsElements = dimensionsHolder[0].getElementsByTagName("dimension")
    for element in dimensionsElements:
      dimension = Dimension(element)
      self.dimension.append(dimension)

def main():
  dom = parse("./config.xml")
  rootElement = dom.documentElement
  if rootElement.tagName != "storages":
    fail("Bad xml!")

  storageElements = rootElement.getElementsByTagName("storage")
  for element in storageElements:
    storage = Storage(element)


if __name__ == "__main__":
  main()
