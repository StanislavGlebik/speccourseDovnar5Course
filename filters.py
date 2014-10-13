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

