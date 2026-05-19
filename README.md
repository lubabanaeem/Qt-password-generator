# Password Generator (PySide6 Desktop App)

A simple desktop application built with **Python + PySide6** that generates secure passwords based on user-selected criteria and evaluates password strength in real time.

---

## Features

- Generate random passwords of custom length (4–32 characters)
- Toggle character sets:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special characters (!@#…)
- Instant password strength evaluation:
  - Weak
  - Medium
  - Strong
  - Very Strong
- Modern dark-themed GUI
- One-click password generation

---

## Tech Stack

- Python 3
- PySide6 (Qt for Python)
- Standard libraries:
  - `random`
  - `string`

---

## Project Structure

project/
│── main.py # Runs the application
│── ui.py # PySide6 GUI (PasswordGeneratorApp)
│── logic.py # Password generation + strength logic

## How It Works

1. User selects password length
2. User chooses character types via checkboxes
3. App generates a random password using selected rules
4. Password strength is calculated based on:
   - Length
   - Variety of character types
5. Strength label updates with color feedback

---

## Password Strength Logic

- **Weak** → short length or very limited character types  
- **Medium** → moderate length or partial character variety  
- **Strong** → good length + multiple character types  
- **Very Strong** → long + full character variety  


