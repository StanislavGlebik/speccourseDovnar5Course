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

    cursor = connection.execute(query)
    resultDict = {}
    for row in cursor:
      d = resultDict.get(row[0], {})
      d[row[1]] = row[2]
      resultDict[row[0]] = d
    return resultDict

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
