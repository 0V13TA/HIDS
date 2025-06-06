from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("This is a custom widget")
        layout.addWidget(label)
        self.setLayout(layout)