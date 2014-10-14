import sys

from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt4.QtGui import QTableWidget, QTableWidgetItem, QDialog, QAbstractItemView
from PyQt4.QtGui import QHBoxLayout

from mainwindow import Ui_MainWindow
from storage import parseConfigFile
from report import Report
from filters import InequalityFilter, EqualityFilter
from add_filter_dialog import Ui_Dialog

def translateReport(report):
    horizontal = report.keys()
    vertical_keys = set()
    for k, v in report.iteritems():
        for x in v:
            vertical_keys.add(x)
    vertical = list(vertical_keys)

    result = list()
    for hkey in horizontal:
        row = list()
        for vkey in vertical:
            if vkey in report[hkey]:
                row.append(report[hkey][vkey])
            else:
                row.append('0')
        result.append(row)
    return horizontal, vertical, result

class Table(QDialog):
    def __init__(self, parent=None, vertical_header=list(), horizontal_header=list(), data=list()):
        super(Table, self).__init__(parent)
        layout = QHBoxLayout()
        resultTable = QTableWidget()

        resultTable.setRowCount(len(vertical_header))
        resultTable.setColumnCount(len(horizontal_header))
        resultTable.setHorizontalHeaderLabels(horizontal_header)
        resultTable.setVerticalHeaderLabels(vertical_header)
        resultTable.horizontalHeader().setResizeMode(1)
        resultTable.verticalHeader().setResizeMode(1)
        resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for x, row in enumerate(data):
            for y, item in enumerate(row):
                resultTable.setItem(x, y, QTableWidgetItem(str(item)))
        self.table = resultTable
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.setMinimumWidth(min(len(horizontal_header) * 250, 800))
        self.setMinimumHeight(min(len(vertical_header) * 70, 800))
        self.setWindowTitle("Report result")

class AddFilterDialog(QDialog):
    def __init__(self, parent, accepting_slot):
        QDialog.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.storage = None
        self.accepted.connect(self.return_result)
        self.accepting_slot = accepting_slot

        self.ui.chooseDimension.currentIndexChanged.connect(self.show_values)

    def return_result(self):
        self.accepting_slot(str(self.ui.chooseDimension.currentText()), str(self.ui.chooseSign.currentText()), str(self.ui.chooseValue.currentText()))

    def show_values(self):
        self.ui.chooseValue.clear()
        if self.storage is None:
            return
        dimension_name = str(self.ui.chooseDimension.currentText())
        self.ui.chooseValue.addItems(self.storage.getDimensionValues(dimension_name))

    def apply_storage(self, storage):
        self.storage = storage
        self.ui.chooseDimension.clear()
        self.ui.chooseDimension.addItems(storage.dimensions.keys())
        self.ui.chooseSign.clear()
        self.ui.chooseSign.addItems(['<=', '=', '>='])
        self.show_values()

class ApplesApplication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen_configuration.triggered.connect(self.load_config)
        self.ui.actionOpen_report.triggered.connect(self.load_report)
        self.ui.showButton.clicked.connect(self.build_report)
        self.ui.deleteButton.clicked.connect(self.remove_rows)
        self.ui.addButton.clicked.connect(self.add_filter)
        self.ui.actionSave_report.triggered.connect(self.save_report)
        self.ui.chooseStorage.currentIndexChanged.connect(self.storage_changed)
        self.ui.actionExit.triggered.connect(self.close)
        self.name2storage = dict()
        self.storages = dict()
        self.dimensions = []
        self.filter = []

        self.do_load_config('config.xml')

    def add_filter(self):
        storage_name = str(self.ui.chooseStorage.currentText())
        current_storage = self.name2storage[storage_name]
        filter_dialog = AddFilterDialog(self, self.do_add_filter)
        filter_dialog.apply_storage(current_storage)
        filter_dialog.setModal(True)
        filter_dialog.show()

    def do_add_filter(self, dimension, sign, value):
        row_index = self.ui.filterTable.rowCount()
        self.ui.filterTable.insertRow(row_index)
        self.ui.filterTable.setItem(row_index, 0, QTableWidgetItem(dimension))
        self.ui.filterTable.setItem(row_index, 1, QTableWidgetItem(sign))
        self.ui.filterTable.setItem(row_index, 2, QTableWidgetItem(value))

    def save_report(self):
        file_dialog = QFileDialog()
        report_filename = file_dialog.getSaveFileName(self, 'Save report', filter='*.xml')
        if report_filename == '' or report_filename is None:
            return
        report = self.gather_report()
        report.saveToFile(report_filename)


    def clear_filters(self):
        for x in xrange(self.ui.filterTable.rowCount()):
            self.ui.filterTable.removeRow(0)
        self.filter = []

    def storage_changed(self):
        self.clear_filters()
        self.dimensions = []
        self.load_dimensions()

    def remove_rows(self):
        for row in sorted(list({item.row() for item in self.ui.filterTable.selectedItems()}), reverse=True):
            self.ui.filterTable.removeRow(row)

    def load_config(self):
        file_dialog = QFileDialog()
        config_filename = file_dialog.getOpenFileName(self, 'Open configuration', filter='*.xml')
        if config_filename == '' or config_filename is None:
            return
        self.do_load_config(config_filename)

    def do_load_config(self, filename):
        try:
            self.storages = parseConfigFile(str(filename))
            self.name2storage = {v.path: v for k, v in self.storages.iteritems()}
        except Exception as ex:
            QMessageBox.critical(self, 'Error while loading config', 'Error while loading config: %s' % ex.message);
            return

        self.ui.chooseStorage.clear()
        self.ui.chooseStorage.addItems(self.name2storage.keys())
        self.ui.chooseStorage.setCurrentIndex(0);

    def load_report(self):
        file_dialog = QFileDialog()
        report_filename = file_dialog.getOpenFileName(self, 'Open report', filter='*.xml')
        if report_filename == '' or report_filename is None:
            return
        self.do_load_report(str(report_filename))

    def do_load_report(self, filename):
        report = Report()
        try:
            report.initFromFile(filename, self.storages)
        except Exception as ex:
            QMessageBox.critical(self, 'Error while loading report', 'Error while loading report: %s' % ex.message);
            return
        self.filters = []
        for filter in report.filters:
            self.filters.extend(filter.get_trivial())

        self.show_filters()

    def show_filters(self):
        self.clear_filters()
        self.ui.filterTable.setRowCount(len(self.filters))
        for x, filter in enumerate(self.filters):
            if type(filter) is InequalityFilter:
                self.ui.filterTable.setItem(x, 0, QTableWidgetItem(str(filter.dimension.name)))
                self.ui.filterTable.setItem(x, 1, QTableWidgetItem(str(filter.sign)))
                self.ui.filterTable.setItem(x, 2, QTableWidgetItem(str(filter.value)))
            else:
                self.ui.filterTable.setItem(x, 0, QTableWidgetItem(str(filter.dimension.name)))
                self.ui.filterTable.setItem(x, 1, QTableWidgetItem(str(filter.sign)))
                self.ui.filterTable.setItem(x, 2, QTableWidgetItem(str(filter.value)))

    def load_dimensions(self):
        storage_name = str(self.ui.chooseStorage.currentText())
        self.dimensions = self.name2storage[storage_name].dimensions.keys()
        self.ui.chooseVerticalDimension.clear()
        self.ui.chooseHorizontalDimension.clear()
        self.ui.chooseVerticalDimension.addItems(self.dimensions)
        self.ui.chooseHorizontalDimension.addItems(self.dimensions)
        self.ui.chooseVerticalDimension.setCurrentIndex(0)
        self.ui.chooseHorizontalDimension.setCurrentIndex(1)

    def gather_filters(self):
        storage_name = str(self.ui.chooseStorage.currentText())
        current_storage = self.name2storage[storage_name]
        result = []
        for row in xrange(self.ui.filterTable.rowCount()):
            dimension = current_storage.getDimensionByName(str(self.ui.filterTable.item(row, 0).text()))
            sign = str(self.ui.filterTable.item(row, 1).text())
            value = str(self.ui.filterTable.item(row, 2).text())
            if sign == '=':
                result.append(EqualityFilter([value], dimension))
            elif sign == '<=':
                result.append(InequalityFilter(dimension, {'to': value}))
            else:
                result.append(InequalityFilter(dimension, {'from': value}))
        return result

    def gather_report(self):
        storage_name = str(self.ui.chooseStorage.currentText())
        vertical_dimension = str(self.ui.chooseVerticalDimension.currentText())
        horizontal_dimension = str(self.ui.chooseHorizontalDimension.currentText())
        if vertical_dimension == horizontal_dimension:
            raise Exception('Build report error: You must specify different '
                                                'horizontal and vertical dimensions')
            return

        current_storage = self.name2storage[storage_name]
        report = Report()
        report.setStorage(current_storage)
        report.setHorizontalDimension(current_storage.getDimensionByName(horizontal_dimension))
        report.setVerticalDimension(current_storage.getDimensionByName(vertical_dimension))
        report.setFilters(self.gather_filters())
        return report

    def set_fixed_size(self):
        self.setFixedHeight(420)
        self.setFixedWidth(420)

    def build_report(self):
        report = self.gather_report()
        result = report.executeQuery()
        horizontal_header, vertical_header, data = result

        resultTable = Table(self, horizontal_header, vertical_header, data)
        resultTable.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ApplesApplication()
    window.show()
    window.set_fixed_size()
    sys.exit(app.exec_())
