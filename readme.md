# Python Selenium Web Testing for Sauce Demo

This repository contains a Selenium WebDriver script written in Python, designed to test the functionality of the [Sauce Demo](https://www.saucedemo.com/) website. Sauce Demo is a practice e-commerce site specifically created for testing automation tools. 

The script demonstrates the use of Selenium for:
- **End-to-end web application testing**.
- **Login validation** (valid and invalid credentials).
- **Product sorting and validation**.
- **Cart operations**, including adding, removing, and validating items.
- **Checkout workflow automation**.
- **Responsive design testing**.

This repository is perfect for learning Selenium automation and understanding how to write robust, reusable test scripts.

---

## Features

### 1. Login Tests
- Validates login functionality using correct credentials.
- Tests error handling for invalid credentials.

### 2. Sorting Products
- Tests sorting options (Name A-Z, Name Z-A, Price Low to High, Price High to Low).
- Validates that the sorting is applied correctly.

### 3. Cart Operations
- Adds products to the cart.
- Verifies cart contents.
- Removes items from the cart.

### 4. Checkout Process
- Automates the checkout workflow by filling in user details and completing the order.

### 5. Responsive Design Testing
- Tests website layout and functionality at various screen resolutions (desktop, tablet, mobile).

---

## Prerequisites
To run the script, ensure you have the following installed:
1. **Python 3.8 or later**: [Download Python](https://www.python.org/downloads/)
2. **Google Chrome**: [Download Chrome](https://www.google.com/chrome/)
3. **pip**: Python's package installer, included with Python 3.

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/your-username/python-selenium-web-testing.git
cd python-selenium-web-testing
```

### 2. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Run the Test Script
Run the Selenium test script using:
```bash
python test.py
```

---

## Detailed Script Explanation

### **1. Test Cases Included**
#### Login Tests
- **Valid Login**: Logs into the website using valid credentials and verifies success.
- **Invalid Login**: Tests incorrect credentials and validates the error message.

#### Sorting Products
- Sorts products by name and price.
- Extracts and validates sorted product names or prices.

#### Cart Operations
- Adds two products to the cart.
- Validates the number of items in the cart.
- Removes a product and verifies the cart updates correctly.

#### Checkout Process
- Completes the checkout process by filling in user details and submitting the order.

#### Responsive Design Testing
- Adjusts the browser window size to test layouts on desktop, tablet, and mobile resolutions.

---

## Files in the Repository

- **`sauce_demo_test.py`**: The main Selenium script containing all test cases.
- **`requirements.txt`**: Lists all Python dependencies required to run the script.
- **`screenshots/`**: (Optional) Folder where screenshots captured during test execution are saved.

---

## Python Dependencies

The required dependencies are listed in the `requirements.txt` file:
```txt
selenium==4.27.1
webdriver-manager==3.8.6
```

Install them with:
```bash
pip install -r requirements.txt
```

---

## Screenshots

Screenshots are automatically captured during the test execution and saved with descriptive filenames. They can be found in the `screenshots/` folder (or the current directory if the folder isn't created).

---

## Example Output

When running the script, you will see outputs like:
- **Login Successful**: If valid credentials are used.
- **Error Message Displayed**: If invalid credentials are used.
- **Products Sorted by Price**: A list of prices will be printed to validate sorting.
- **Cart Operations**: Confirmation of products added or removed.
- **Checkout Successful**: Final confirmation after completing the order.

---

## Contributing

If you'd like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation.

---

## License

You are free to copy, modify, and/or distribute as long as for educational purposes only / for practice.
Mr-LuaM
