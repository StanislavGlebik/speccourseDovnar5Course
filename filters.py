from common import fail
from common import checkElementAttribute

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

class InequalityFilter:
  def __init__(self, dimension, kwargs):
    self.values = kwargs
    if not self.values.has_key('from') and not self.values.has_key('to'):
      fail("Bad inequality filter")
    self.dimension = dimension
    self.dimensionTable = dimension.table
    self.dimensionField = dimension.field

  def getElement(self, document):
    fElement = document.createElement("filter")
    fElement.setAttribute("dimension", self.dimension.name)
    fElement.setAttribute("type", "inequality")

    if self.values.has_key("from"):
      fElement.setAttribute("from", self.values["from"])

    if self.values.has_key("to"):
      fElement.setAttribute("to", self.values["to"])

    return fElement

  def generateQueryString(self):
    res = " and (1=1"
    if self.values.has_key('from'):
      res += " and " + self.dimensionTable + "." + self.dimensionField + ">=" + '"' + self.values['from'] + '"'
    if self.values.has_key('to'):
      res += " and " + self.dimensionTable + "." + self.dimensionField + "<=" + '"' + self.values['to'] + '"'
    res += ")"
    return res

