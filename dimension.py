from common import checkElementAttribute

class Dimension:
  def __init__(self, element):
    self.table = checkElementAttribute(element, "table")
    self.name = checkElementAttribute(element, "name")
    self.field = checkElementAttribute(element, "field")
    self.factFk = checkElementAttribute(element, "fact_fk")
