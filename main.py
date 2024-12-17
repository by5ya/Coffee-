import sys
from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QHeaderView


class CoffeeWin(QWidget):
    def __init__(self):
        super().__init__()
        try:
            uic.loadUi("main.ui", self)
        except Exception as e:
            print(f"Ошибка загрузки UI: {e}")
            sys.exit(1)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")

        if not db.open():
            print(f"Ошибка открытия базы данных: {db.lastError().text()}")
            sys.exit(1)

        model = QSqlTableModel(self, db)
        # Исправленное имя таблицы — используйте тот же регистр, что и в БД!
        model.setTable("Coffee")  # <--- Важно!
        model.select()

        if model.lastError().isValid():
            print(f"Ошибка выбора данных: {model.lastError().text()}")  # Проверка ошибок во время select
            sys.exit(1)

        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


app = QApplication(sys.argv)
coffee = CoffeeWin()
coffee.show()
sys.exit(app.exec())

