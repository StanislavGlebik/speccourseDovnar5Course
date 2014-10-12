from xml.dom.minidom import parse
from xml.dom.minidom import getDOMImplementation
import sqlite3

def fail(message):
  print message
  exit(1)

def checkElementAttribute(element, attr):
  if not element.hasAttribute(attr):
    fail("No " + attr + " attribute in " + element.tagName)
  else:
    return element.getAttribute(attr)

class EqualityFilter:
# for equality
  def __init__(self, values, dimension):
    self.values = values
    self.dimension = dimension
    self.dimensionTable = dimension.table
    self.dimensionField = dimension.field

  def getElement(self, document):
    fElement = document.createElement("filter")
    fElement.setAttribute("dimension", self.dimension.name)
    fElement.setAttribute("type", "equality")
    for value in self.values:
      valueElement = document.createElement("equal")
      valueElement.setAttribute("value", value)
      fElement.appendChild(valueElement)

    return fElement

  def generateQueryString(self):
    res = " and (1=2"
    for value in self.values:
      res += " or " + self.dimensionTable + "." + self.dimensionField + "=" + '"' + value + '"'
    res += ")"
    return res

class Report:
  def __init__(self, element, storages):
    self.storageId = checkElementAttribute(element, "storage_id")
    self.filters = []
    self.storage = storages[self.storageId]

    verticals = element.getElementsByTagName("vertical")
    if len(verticals) != 1:
      fail("Bad amount of vertical dimensions")
    verticalDimensionName = checkElementAttribute(verticals[0], "dimension")
    self.verticalDimension = self.storage.getDimensionByName(verticalDimensionName)

    horizontals = element.getElementsByTagName("horizontal")
    if len(horizontals) != 1:
      fail("Bad amount of horizontal dimensions")
    horizontalDimensionName = checkElementAttribute(horizontals[0], "dimension")
    self.horizontalDimension = self.storage.getDimensionByName(horizontalDimensionName)

    filtersElements = element.getElementsByTagName("filters")
    if len(filtersElements) != 1:
      fail("Bad amount of filters elements")
    filters = filtersElements[0].getElementsByTagName("filter")

    for fElement in filters:
      dimensionName = checkElementAttribute(fElement, "dimension")
      curDimension = self.storage.getDimensionByName(dimensionName)
      filterType = checkElementAttribute(fElement, "type")
      if filterType == "equality":
        equalValueElements = fElement.getElementsByTagName("equal")
        equals = []
        for e in equalValueElements:
          equals.append(checkElementAttribute(e, "value"))
        self.filters.append(EqualityFilter(equals, curDimension))
      elif filterType == "inequality":
        fail("Not implemented")
      else:
        fail("Bad filter type")

  def executeQuery(self):
    self.storage.getTable([self.horizontalDimension.name, self.verticalDimension.name], self.filters)

  def saveToFile(self, filename):
    with open(filename, 'w') as output:
      impl = getDOMImplementation()
      document = impl.createDocument(None, 'report', None)
      root = document.documentElement
      root.setAttribute("storage_id", self.storageId)
      vertical = document.createElement("vertical")
      vertical.setAttribute("dimension", self.verticalDimension.name)
      root.appendChild(vertical)

      horizontal = document.createElement("horizontal")
      horizontal.setAttribute("dimension", self.horizontalDimension.name)
      root.appendChild(horizontal)

      filtersElement = document.createElement("filters")
      for f in self.filters:
        filtersElement.appendChild(f.getElement(document))

      root.appendChild(filtersElement)
      document.writexml(output)

  def getFilters(self):
    return self.filters

  def getHorizontalDimension(self):
    return self.horizontalDimension

  def getVerticalDimension(self):
    return self.verticalDimension

  def getHorizontalDimensionName(self):
    return self.horizontalDimension.name

  def getVerticalDimensionName(self):
    return self.verticalDimension.name

class Dimension:
  def __init__(self, element):
    self.table = checkElementAttribute(element, "table")
    self.name = checkElementAttribute(element, "name")
    self.field = checkElementAttribute(element, "field")
    self.factFk = checkElementAttribute(element, "fact_fk")

class Storage:
  def __init__(self, element):
    self.id = checkElementAttribute(element, "id")
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

  def getId(self):
    return self.id

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
  storages = {}
  for element in storageElements:
    storage = Storage(element)
    storages[storage.getId()] = storage
    storage.getTable(["Shops", "Kinds"], [EqualityFilter(["stash", "kolesov93"], storage.getDimensionByName("Customers")),])

  domReport = parse("./reports/report2.xml")
  report = Report(domReport.documentElement, storages)

  report.executeQuery()
  report.saveToFile("try.xml")

  domReport = parse("try.xml")
  report = Report(domReport.documentElement, storages)
  report.executeQuery()

if __name__ == "__main__":
  main()

