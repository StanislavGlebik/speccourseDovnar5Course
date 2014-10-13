from common import checkElementAttribute
from common import fail

from filters import EqualityFilter

from xml.dom.minidom import getDOMImplementation

class Report:
  def setStorage(self, storage):
    self.storage = storage

  def setFilters(self, filters):
    self.filters = filters

  def setHorizontalDimension(self, horizontalDimension):
    self.horizontalDimension = horizontalDimension

  def setVerticalDimension(self, verticalDimension):
    self.verticalDimension = verticalDimension

  def initFromXmlElement(self, element, storages):
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
    return self.storage.getTable([self.horizontalDimension.name, self.verticalDimension.name], self.filters)

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

