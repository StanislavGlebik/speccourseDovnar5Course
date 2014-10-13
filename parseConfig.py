from common import fail
from common import checkElementAttribute

from filters import EqualityFilter
from filters import InequalityFilter
from storage import parseConfigFile

from report import Report

def main():
  storages = parseConfigFile()
  for storageName in storages:
    storage = storages[storageName]
    print storage.path
  report = Report()

  report.setStorage(storage)
  report.setHorizontalDimension(storage.getDimensionByName("Shops"))
  report.setVerticalDimension(storage.getDimensionByName("Customers"))
  fKinds = EqualityFilter(["ranetki",], storage.getDimensionByName("Kinds"))
  f = InequalityFilter(storage.getDimensionByName('Customers'), {'from':'kolesov93', 'to':'kolesov93'})
  report.setFilters([f, fKinds])
  report.saveToFile("ololo.xml")
  print report.executeQuery()
  report = Report()
  report.initFromFile("reports/inequalityReport.xml", storages)
  print report.executeQuery()

if __name__ == "__main__":
  main()

