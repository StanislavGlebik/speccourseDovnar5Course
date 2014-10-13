from common import fail
from common import checkElementAttribute

from filters import EqualityFilter
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
  f = EqualityFilter(["stash", "kolesov93"], storage.getDimensionByName("Customers"))
  report.setFilters([f])

  print report.executeQuery()
if __name__ == "__main__":
  main()

