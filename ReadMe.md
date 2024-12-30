# **Automated Testing Project**

## **Overview**
This project is an ongoing learning experience where I am practicing automated testing using **Python** and **Selenium**. I am using the free website [https://www.saucedemo.com/](https://www.saucedemo.com/), which simulates an online store, to test various functionalities such as login and shopping cart features. 

Currently, I am  working on improving my automation skills by writing test cases for:
- Login functionality.
- Adding and removing items from the shopping cart.
- Generating HTML reports to document the test results.

## **Features**
1. **Login Tests**:
   - Test login with **valid credentials**.
   - Test login with **incorrect password** but a valid username.
   - Test login with **incorrect username** but a valid password.
   
2. **Shopping Cart Tests**:
   - Test adding a product to the cart:
     - From the **homepage**.
     - From the **product details page**.
   - Test removing a product from the cart:
     - From the **homepage**.
     - From the **product details page**.

3. **HTML Reports**:
   - Generate detailed HTML reports after each test run to document results.

---

## **Setup and Installation**

### **1. Prerequisites**
- Python version **3.11** installed on your system.
- Recommended package manager: `pip` (can be installed via [Homebrew](https://brew.sh/) or Python).
- Google Chrome (or your preferred browser) and WebDriver for browser automation.

### **2. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-directory>
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```
**It should contain the following**:
- pytest==8.3.3
- selenium==4.27.1
- MarkupSafe==3.0.2
- jinja2==3.1.5
- pytest-html==4.1.1
- pytest-metadata==3.1.1
- pluggy>=1.3.0

---
## **Usage**

### **1. Run the Tests**
```bash
python3.11 -m pytest --html=report.html
```

### **2. View the Report**
```bash
open report.html  # macOS/Linux
start report.html  # Windows
```