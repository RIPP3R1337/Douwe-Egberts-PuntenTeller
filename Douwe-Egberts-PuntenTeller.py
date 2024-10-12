from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
import sys
import os

class DouweEgbertsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Douwe Egberts Punten Teller')
        self.setWindowIcon(QIcon('voucher.ico'))
        self.setFixedSize(700, 700)

        # Set layout
        layout = QVBoxLayout()

        # Title Label
        self.title = QLabel("Douwe Egberts Punten naar Euro")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont('Arial', 20))
        layout.addWidget(self.title)

        # Input fields for different point types, stacked vertically
        self.point_inputs = {}
        self.create_input(layout, "100 Douwe Egberts punten", "100")
        self.create_input(layout, "40 Douwe Egberts punten", "40")
        self.create_input(layout, "20 Douwe Egberts punten", "20")
        self.create_input(layout, "15 Douwe Egberts punten", "15")
        self.create_input(layout, "10 Douwe Egberts punten", "10")
        self.create_input(layout, "8 Douwe Egberts punten", "8")
        self.create_input(layout, "4 Douwe Egberts punten", "4")

        # Conversion Button
        self.convert_button = QPushButton("Omzetten naar Euro", self)
        self.convert_button.setFont(QFont('Arial', 14))
        self.convert_button.setFixedSize(250, 50)
        self.convert_button.clicked.connect(self.convert_to_euro)
        layout.addWidget(self.convert_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Horizontal layout for bottom buttons
        bottom_layout = QHBoxLayout()

        # Save Button for saving sticker counts
        self.save_button = QPushButton("Stickers opslaan", self)
        self.save_button.setFont(QFont('Arial', 14))
        self.save_button.setFixedSize(150, 50)
        self.save_button.clicked.connect(self.save_sticker_amounts)

        # Load Button for loading previously saved sticker counts
        self.load_button = QPushButton("Stickers laden", self)
        self.load_button.setFont(QFont('Arial', 14))
        self.load_button.setFixedSize(150, 50)
        self.load_button.clicked.connect(self.load_sticker_amounts)


        # Reset button
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.setFont(QFont('Arial', 14))
        self.reset_button.setFixedSize(100, 50)
        self.reset_button.clicked.connect(self.reset_stickers)



        # Add both buttons to the horizontal layout (aligned left)
        bottom_layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignLeft)
        bottom_layout.addWidget(self.reset_button, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_layout.addWidget(self.load_button, alignment=Qt.AlignmentFlag.AlignRight)

        # Add the horizontal layout at the end of the main layout
        layout.addLayout(bottom_layout)

        # Result Label
        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont('Arial', 14))
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def create_input(self, layout, label_text, point_value):
        """ Helper to create label + input box for point types, stacked vertically """
        label = QLabel(label_text, self)
        label.setFont(QFont('Arial', 12))
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(f"Vul in hoeveel {point_value}-Punten Douwe Egberts Kaarten je hebt")
        self.point_inputs[point_value] = input_field
        layout.addWidget(label)
        layout.addWidget(input_field)

    def convert_to_euro(self):
        # Get inputs and calculate the total points
        total_points = 0
        point_values = {'100': 100, '40': 40, '20': 20, '15': 15, '10': 10, '8': 8, '4': 4}

        try:
            for point_type, point_value in point_values.items():
                quantity = int(self.point_inputs[point_type].text() or 0)
                total_points += quantity * point_value

            # Convert points to euros (200 points = 1 euro)
            euros = total_points / 200
            self.result_label.setText(f"{total_points} punten met een waarde van €{euros:.2f}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers for all fields.")

    def save_sticker_amounts(self):
        confirmation = QMessageBox.question(self, "Bevestiging",
                                            "Weet je zeker dat je de gegevens wilt opslaan?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if  confirmation == QMessageBox.StandardButton.Yes:
            try:
                with open("sticker_counts.txt", "w") as file:
                    for point_type, input_field in self.point_inputs.items():
                        count = input_field.text() or "0"
                        
                        if not count.replace('.', '').replace('-', '').isdigit():
                            raise ValueError(f"Ongeldige cijfer bij {point_type}: >> {count} <<")
                        
                        
                        file.write(f"{point_type}-Punten: {count} stickers\n")

                self.result_label.setText("Kaarten succesvol opgeslagen!")
            except ValueError as ve:
                self.result_label.setText(f"Error: {ve}")
            except Exception as e:
                self.result_label.setText(f"Error saving sticker amounts: {e}")

    def load_sticker_amounts(self):
        if not os.path.exists("sticker_counts.txt"):
            self.result_label.setText("No saved sticker counts found.")
            return

        try:
            with open("sticker_counts.txt", "r") as file:
                for line in file:
                    if '-' in line:
                        point_type, count = line.split("-Punten:")
                        point_type = point_type.strip()
                        count = count.split()[0].strip()  # Get the number before "stickers"
                        if point_type in self.point_inputs:
                            self.point_inputs[point_type].setText(count)

            self.result_label.setText("Kaarten succesvol geladen!")
        except Exception as e:
            self.result_label.setText(f"Error loading sticker amounts: {e}")

    def reset_stickers(self):
        reset_confirmation = QMessageBox.warning(self, "Bevestiging",
                                            "Weet je zeker dat je op de reset knop wilt klikken?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if  reset_confirmation == QMessageBox.StandardButton.Yes:
            for input_field in self.point_inputs.values():
                input_field.setText("")
            self.result_label.setText("")




# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DouweEgbertsApp()
    window.show()
    sys.exit(app.exec())
