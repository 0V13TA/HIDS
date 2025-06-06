from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QStackedWidget,
    QHBoxLayout,
)
from PySide6.QtCore import Qt, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OVIETA HIDS")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #ffffff;
            }
        """
        )

        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(30)

        # Big title
        title = QLabel("OVIETA HIDS")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            """
            font-size: 36px;
            font-weight: bold;
            color: #0d47a1;
            margin-top: 30px;
            margin-bottom: 20px;
        """
        )
        main_layout.addWidget(title)

        # Navigation buttons
        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(20)

        btn_page1 = QPushButton("Dashboard")
        btn_page2 = QPushButton("Settings")

        button_style = """
            QPushButton {
                background-color: #0d47a1;
                color: #fff;
                border-radius: 8px;
                padding: 16px 36px;
                font-size: 18px;
                font-weight: bold;
                border: 2px solid #0d47a1;
            }
            QPushButton:hover {
                background-color: #1976d2;
                border: 2px solid #1976d2;
            }
        """
        btn_page1.setStyleSheet(button_style)
        btn_page2.setStyleSheet(button_style)

        nav_layout.addStretch()
        nav_layout.addWidget(btn_page1)
        nav_layout.addWidget(btn_page2)
        nav_layout.addStretch()
        main_layout.addLayout(nav_layout)

        # Stacked widget for pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.page_dashboard())
        self.stacked_widget.addWidget(self.page_settings())
        main_layout.addWidget(self.stacked_widget)

        # Button actions
        btn_page1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        btn_page2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def page_dashboard(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Dashboard")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: #222;")
        layout.addWidget(label)
        page.setLayout(layout)
        return page

    def page_settings(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Settings Page")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: #222;")
        layout.addWidget(label)
        page.setLayout(layout)
        return page


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
