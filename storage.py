from common import checkElementAttribute
from common import fail

from dimension import Dimension

from xml.dom.minidom import parse

import sqlite3

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

  def getDimensionValues(self, dimensionName):
    dimension = self.dimensions[dimensionName]
    query = "select "
    query += dimension.table + "." + dimension.field + " "
    query += "from " + dimension.table
    connection = sqlite3.connect(self.path)
    res = connection.execute(query)
    return map(lambda x: x[0], res)

  def getNamesForOneDimension(self, dimension, filters):
    query = "select "
    query += dimension.table + "." + dimension.field + " "
    query += "from " + dimension.table
    query += " where 1=1 "
    for f in filters:
      query += f.generateQueryString()

    connection = sqlite3.connect(self.path)
    res = connection.execute(query)
    return map(lambda x: x[0], res)


  def getTable(self, dimensions, filters = []):
    if len(dimensions) != 2:
      fail("Bad dimensions size")

    horizontalFilters = []
    verticalFilters = []
    for f in filters:
      if f.dimension.name == self.dimensions[dimensions[0]].name:
        horizontalFilters.append(f)
      if f.dimension.name == self.dimensions[dimensions[1]].name:
        verticalFilters.append(f)
    horizontalNames = self.getNamesForOneDimension(self.dimensions[dimensions[0]], horizontalFilters)
    verticalNames = self.getNamesForOneDimension(self.dimensions[dimensions[1]], verticalFilters)

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

    cursor = connection.execute(query)
    resultDict = {}
    for row in cursor:
      d = resultDict.get(row[0], {})
      d[row[1]] = row[2]
      resultDict[row[0]] = d

    ans = []
    for h in horizontalNames:
      last = []
      for v in verticalNames:
        if resultDict.has_key(h) and resultDict[h].has_key(v):
          last.append(resultDict[h][v])
        else:
          last.append(0)
      ans.append(last)

    return horizontalNames, verticalNames, ans

def parseConfigFile(filename="./config.xml"):
  dom = parse(filename)
  rootElement = dom.documentElement
  if rootElement.tagName != "storages":
    fail("Bad xml!")

  storageElements = rootElement.getElementsByTagName("storage")
  storages = {}
  for element in storageElements:
    storage = Storage(element)
    storages[storage.getId()] = storage

  return storages
