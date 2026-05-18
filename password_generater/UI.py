from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QLabel, QCheckBox, QPushButton, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt
from logic import generate_password, get_strength


class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setMinimumSize(400, 400)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # --- Title ---
        title = QLabel("🔐 Password Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("title")
        main_layout.addWidget(title)

        # --- Length Input ---
        length_label = QLabel("Password Length (4-32):")
        length_label.setObjectName("sectionLabel")
        main_layout.addWidget(length_label)

        self.length_input = QLineEdit()
        self.length_input.setText("12")
        self.length_input.setObjectName("lengthInput")
        main_layout.addWidget(self.length_input)

        # --- Checkboxes ---
        self.check_upper = QCheckBox("Uppercase Letters (A-Z)")
        self.check_lower = QCheckBox("Lowercase Letters (a-z)")
        self.check_numbers = QCheckBox("Numbers (0-9)")
        self.check_special = QCheckBox("Special Characters (!@#...)")

        self.check_upper.setChecked(True)
        self.check_lower.setChecked(True)
        self.check_numbers.setChecked(True)
        self.check_special.setChecked(False)

        main_layout.addWidget(self.check_upper)
        main_layout.addWidget(self.check_lower)
        main_layout.addWidget(self.check_numbers)
        main_layout.addWidget(self.check_special)

        # --- Generate Button ---
        self.generate_btn = QPushButton("Generate Password")
        self.generate_btn.setObjectName("generateBtn")
        self.generate_btn.clicked.connect(self.generate)
        main_layout.addWidget(self.generate_btn)

        # --- Password Display ---
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Your password will appear here...")
        self.password_display.setObjectName("passwordDisplay")
        main_layout.addWidget(self.password_display)

        # --- Strength Label ---
        self.strength_label = QLabel("Strength: ")
        self.strength_label.setAlignment(Qt.AlignCenter)
        self.strength_label.setObjectName("strengthLabel")
        main_layout.addWidget(self.strength_label)

    def generate(self):
        length_text = self.length_input.text()

        try:
            length = int(length_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number for length.")
            return

        if length < 4 or length > 32:
            QMessageBox.warning(self, "Error", "Length must be between 4 and 32.")
            return

        use_upper = self.check_upper.isChecked()
        use_lower = self.check_lower.isChecked()
        use_numbers = self.check_numbers.isChecked()
        use_special = self.check_special.isChecked()

        Password = generate_password(length, use_upper, use_lower, use_numbers, use_special)

        if Password is None:
            QMessageBox.warning(self, "Oops!", "Please select at least one character type.")
            return

        self.password_display.setText(Password)

        strength, color = get_strength(Password)
        self.strength_label.setText("Strength: " + strength)
        self.strength_label.setStyleSheet("color: " + color + "; font-weight: bold; font-size: 14px;")

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QWidget {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-size: 13px;
            }
            QLabel#title {
                font-size: 22px;
                font-weight: bold;
                color: #cba6f7;
                padding: 10px;
            }
            QLabel#sectionLabel {
                font-size: 13px;
                color: #89b4fa;
                margin-top: 8px;
            }
            QCheckBox {
                spacing: 8px;
                padding: 4px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QPushButton#generateBtn {
                background-color: #cba6f7;
                color: #1e1e2e;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
                margin-top: 10px;
            }
            QPushButton#generateBtn:hover {
                background-color: #b4befe;
            }
            QLineEdit#passwordDisplay {
                background-color: #313244;
                color: #a6e3a1;
                font-size: 15px;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #45475a;
            }
            QLineEdit#lengthInput {
                background-color: #313244;
                color: #cdd6f4;
                padding: 6px;
                border-radius: 6px;
                border: 1px solid #45475a;
            }
        """)