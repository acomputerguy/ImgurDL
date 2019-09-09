from PyQt5.QtWidgets import QTableWidgetItem

class ActivityTab():
    def log2Table(self, tablewidget):
        with open("logs/activity.log") as fstream:
            for numLines, length in enumerate(fstream):
                pass
        numLines = numLines + 1
        del fstream
        tablewidget.setRowCount(numLines)
        activityFile = open("logs/activity.log", "r")
        i = 0
        for line in activityFile:
            lineContents = line.split("|")
            for j in range(0, 5):
                tablewidget.setItem(i, j, QTableWidgetItem(lineContents[j]))
                tablewidget.setItem(i, j, QTableWidgetItem(lineContents[j]))
                tablewidget.setItem(i, j, QTableWidgetItem(lineContents[j]))
                tablewidget.setItem(i, j, QTableWidgetItem(lineContents[j]))
                tablewidget.setItem(i, j, QTableWidgetItem(lineContents[j]))
            i += 1
