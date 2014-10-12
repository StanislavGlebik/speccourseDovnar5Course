from xml.dom.minidom import parse
import sqlite3

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

class EqualityFilter:
# for equality
  def __init__(self, values, dimension):
    self.values = values
    self.dimensionTable = dimension.table
    self.dimensionField = dimension.field

  def generateQueryString(self):
    res = " and (1=2"
    for value in self.values:
      res += " or " + self.dimensionTable + "." + self.dimensionField + "=" + '"' + value + '"'
    res += ")"
    return res

class Storage:
  def __init__(self, element):
    self.path = checkElementAttribute(element, "path")
    self.aggregatedValueName = checkElementAttribute(element, "aggregated_value_name")
    self.factTable = checkElementAttribute(element, "fact_table")
    self.aggregatedValueField = checkElementAttribute(element, "aggregated_value_field")
    self.dimensions = {}
    self.joins = ""

    dimensionsHolder = element.getElementsByTagName("dimensions")
    if len(dimensionsHolder) > 1:
      fail("Too many dimensions elements!")
    if len(dimensionsHolder) == 0 :
      fail("No dimensions elements!")

    dimensionsElements = dimensionsHolder[0].getElementsByTagName("dimension")
    for element in dimensionsElements:
      dimension = Dimension(element)
      self.joins += " join " + dimension.table + " on " + dimension.factFk + "=" + dimension.table + ".id"
      self.dimensions[dimension.name] = dimension

  def getDimensionByName(self, dimensionName):
    return self.dimensions[dimensionName]

  def getTable(self, dimensions, filters = []):
    connection = sqlite3.connect(self.path)
    query = "select "
    for dimensionName in dimensions:
      dimension = self.dimensions[dimensionName]
      query += dimension.table + "." + dimension.field + ", "
    query += "sum(" + self.aggregatedValueField + ") "
    query += " from " + self.factTable
    query += self.joins

    query += " where 1=1 "
    for f in filters:
      query += f.generateQueryString()

    query += " group by "
    for dimensionName in dimensions:
      dimension = self.dimensions[dimensionName]
      query += dimension.table + "." + dimension.field + ", "
    query = query[:-2]

    print query
    cursor = connection.execute(query)
    for row in cursor:
      print row[0], row[1], row[2]

def main():
  dom = parse("./config.xml")
  rootElement = dom.documentElement
  if rootElement.tagName != "storages":
    fail("Bad xml!")

  storageElements = rootElement.getElementsByTagName("storage")
  for element in storageElements:
    storage = Storage(element)
    storage.getTable(["Shops", "Kinds"], [EqualityFilter(["stash", "kolesov93"], storage.getDimensionByName("Customers")),])

if __name__ == "__main__":
  main()

