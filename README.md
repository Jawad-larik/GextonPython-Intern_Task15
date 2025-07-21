# GextonPython-Intern_Task15
Developed a Python script that uses Selenium to fill out and submit a web form using data from a CSV file.

```markdown
# Automated Web Form Submission with Selenium

This project automates the process of submitting a web form using data from a CSV file with the help of Python and Selenium.

## 🔧 Features

- Reads form input data (name, email, address, gender, subscribe) from a CSV file.
- Automatically fills and submits a local HTML form using Selenium WebDriver.
- Handles text inputs, radio buttons (gender), and checkboxes (subscribe).
- Logs each submission's success or failure to a log file.

## 📁 Project Structure

```

.
├── automate\_form.py          # Python script to run the automation
├── test\_form.html            # Local test form
├── form\_data.csv             # Input data file
├── submission\_log.txt        # Auto-generated log file

````

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install selenium
pip install pandas
````

### 2. Download ChromeDriver

Download the matching version of [ChromeDriver](https://sites.google.com/chromium.org/driver/) and place it in the same folder or your system PATH.

### 3. Run the Script

```bash
python automate_form.py
```

## 📝 Notes

* Ensure Chrome is installed.
* This project uses a local form (`test_form.html`). You can replace it with any actual form URL if needed.
* Make sure the `form_data.csv` has the following headers:

```
name,email,address,gender,subscribe
```

## 📩 Contact

Created by **Jawad Larik** — for internship automation task.

```
