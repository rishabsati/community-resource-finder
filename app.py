# community resource finder app
# Author: Rishab Sati
# ASU Undergraduate 2027

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt
from services.places_api import search_places


class ResourceApp(QWidget):
    def __init__(self):
        super().__init__()

        # Main UI widgets
        self.app_label = QLabel("Community Resource Finder", self)
        self.subtitle_label = QLabel("Search by city or ZIP code", self)
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter city or ZIP code")
        self.search_button = QPushButton("Search", self)
        self.status_label = QLabel("", self)

        # Category selection
        self.category_label = QLabel("Choose a category:", self)
        self.category_dropdown = QComboBox(self)
        self.category_dropdown.addItems([
            "Food Banks", "Shelters", "Free Clinics",
            "Mental Health Services", "Job Help"
        ])

        # Results section
        self.results_label = QLabel("Search Results", self)
        self.results_box = QTextEdit(self)
        self.results_box.setReadOnly(True)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Community Resource Finder")
        self.setFixedSize(920, 680)

        # Main layout and search row
        main_layout = QVBoxLayout()
        search_row = QHBoxLayout()

        search_row.addWidget(self.search_input)
        search_row.addWidget(self.search_button)

        main_layout.addWidget(self.app_label)
        main_layout.addWidget(self.subtitle_label)
        main_layout.addLayout(search_row)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.category_label)
        main_layout.addWidget(self.category_dropdown)
        main_layout.addWidget(self.results_label)
        main_layout.addWidget(self.results_box)

        main_layout.setSpacing(12)
        main_layout.setContentsMargins(20, 20, 20, 20)

        search_row.setStretch(0, 4)
        search_row.setStretch(1, 1)

        self.setLayout(main_layout)

        # Alignment
        self.app_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.search_input.setAlignment(Qt.AlignLeft)
        self.status_label.setAlignment(Qt.AlignCenter)

        # Object names for stylesheet targeting
        self.app_label.setObjectName("app_label")
        self.subtitle_label.setObjectName("subtitle_label")
        self.search_input.setObjectName("search_input")
        self.search_button.setObjectName("search_button")
        self.status_label.setObjectName("status_label")
        self.category_dropdown.setObjectName("category_dropdown")
        self.results_label.setObjectName("results_label")
        self.results_box.setObjectName("results_box")

        # App styling
        self.setStyleSheet("""
            QWidget {
            background-color: #f7f8fa;
            }

            QLabel, QPushButton, QComboBox, QTextEdit, QLineEdit {
                font-family: Calibri;
            }

            QLabel#app_label {
                font-size: 28px;
                font-weight: bold;
                color: #1f2937;
                margin-bottom: 2px;
            }

            QLabel#subtitle_label {
                font-size: 16px;
                color: #6b7280;
                margin-bottom: 8px;
            }

            QLineEdit#search_input {
                font-size: 18px;
                padding: 10px;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                background-color: white;
            }

            QPushButton#search_button {
                font-size: 16px;
                font-weight: bold;
                padding: 10px 18px;
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
            }

            QPushButton#search_button:hover {
                background-color: #1d4ed8;
            }

            QLabel#status_label {
                font-size: 14px;
                color: #374151;
                margin-top: 4px;
                margin-bottom: 4px;
            }

            QLabel#results_label {
                font-size: 16px;
                font-weight: bold;
                color: #1f2937;
                margin-top: 6px;
            }

            QComboBox#category_dropdown {
                font-size: 16px;
                padding: 8px;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                background-color: white;
            }

            QTextEdit#results_box {
                font-size: 15px;
                padding: 10px;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                background-color: white;
            }
        """)

        # Run search when the button is clicked
        self.search_button.clicked.connect(self.search_resource)

    def search_resource(self):
        # Read user input
        location = self.search_input.text().strip()
        category = self.category_dropdown.currentText()

        # Update results section title
        self.results_label.setText(f"{category} Results:")

        # Validate input
        if not location:
            self.status_label.setText("Please enter a City or ZIP code.")
            return

        # Clear previous results
        self.results_box.clear()

        # Fetch matching places from the API
        results = search_places(location, category)

        # Handle empty results
        if not results:
            self.results_box.setText("No resources found")
            self.status_label.setText(f"No {category} results found for {location}")
            return

        # Build formatted output for the results box
        results_text = f"Results for {category} near {location}:\n\n"

        for index, place in enumerate(results, start=1):
            results_text += f"{index}. {place}\n\n"

        self.results_box.setText(results_text)
        self.status_label.setText(f"Showing {category} results for {location}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    resource = ResourceApp()
    resource.show()
    sys.exit(app.exec_())