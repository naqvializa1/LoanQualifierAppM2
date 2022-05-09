# Automated Loan Qualifier

Applying for a loan can be an arduous and time consuming process. This automated loan qualifier allows users to upload a csv file of their choosing, containing a list of lenders, maximum loan amount, max loan to value ration (LTV), max debt to income ratio (DTI), min credit score and interest rate, input their personal financial details and run them through a calculator. The user then has the ability to save the list of qualified loans in the form of a csv directly to their machine.

---

## Technologies

Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.

This program leverages python 3.7+

To ensure all dependencies are installed and up-to-date, please run the following commands in your terminal once you have cloned the repository to your local machine.
run pip install -r requirements.txt

---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.
1. Copy this repository via the URL (SSH or HTTP)

<img width="907" alt="Screen Shot 2022-04-03 at 3 35 27 PM" src="https://user-images.githubusercontent.com/98444459/161445246-d4eecac4-44ae-452f-8e0c-ebaa9e523908.png">

2. Run a git clone command in your terminal or git bash under the desired local directory
<img width="721" alt="Screen Shot 2022-04-03 at 3 39 48 PM" src="https://user-images.githubusercontent.com/98444459/161445190-806f9755-d57a-45fd-9712-a6ab83629a1d.png">

3. If you receive errors, please review the dependencies above, install them and try again. 

---

## Usage

1. Navigate to the directory in either the Terminal, GitBash or in VS Code.

2. Run the command: python app.py
<img width="569" alt="Screen Shot 2022-04-03 at 3 56 28 PM" src="https://user-images.githubusercontent.com/98444459/161446187-cfb4a12e-9629-498e-8a06-fd9ad9b1e8cf.png">

3. Enter the path for the csv file containing the list of financial institutions, loan details and qualification criteria (there is one provided as an example: ./data/daily_rate_sheet.csv
<img width="569" alt="Screen Shot 2022-04-03 at 3 56 54 PM" src="https://user-images.githubusercontent.com/98444459/161446192-adb40530-51ce-46ee-8d15-80939d5cc616.png">

4. Follow the prompts to enter your financial details.
<img width="571" alt="Screen Shot 2022-04-03 at 3 57 34 PM" src="https://user-images.githubusercontent.com/98444459/161446210-8a55a398-6e16-4365-9bd5-69dcaab5372a.png">

5. The number of loans for which you are qualified will be displayed as an output, and you will be prompted to save the file.
<img width="573" alt="Screen Shot 2022-04-03 at 3 58 02 PM" src="https://user-images.githubusercontent.com/98444459/161446229-b12ec624-491b-47bd-b6a1-aa3fdfb54d2f.png">

6. If you would like to save the list of loans as a csv output, indicate the desired save location as well as the name of the file.
<img width="573" alt="Screen Shot 2022-04-03 at 3 58 02 PM" src="https://user-images.githubusercontent.com/98444459/161446404-b40d5c08-d2f7-4e0f-986e-1ca4b8f143d2.png">

---

## Contributors

Made by:
Ryan Anderson
  Email: m.anderson.ryan@gmail.com
  LinkedIn: https://www.linkedin.com/in/ryan-anderson-57b2b173

---

## License

No license is required to use this product.
