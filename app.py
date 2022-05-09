# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""

# Import required libraries
import sys
import fire
import questionary
from pathlib import Path
import os

from sympy import true

from qualifier.utils.fileio import load_csv
from qualifier.utils.fileio import save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

# Function to load bank data from csv of a users choosing
def load_bank_data():

    # Prompt for csv
    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    # Check that the file entered by user exists and the path is correct
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    # Return bank data from sheet selected by user
    return load_csv(csvpath)

# Function to obtain credit, monthly debt, monthly income, desired loan amount and home value from applicant 
def get_applicant_info():

    # Prompts for obtaining applicant information
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    # Set variables with information input by applicant
    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    # Return financial information input by the applicant
    return credit_score, debt, income, loan_amount, home_value


# Function to determine for which loans the applicant is qualified based on financial information provided
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.
    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    # Indicate the number of loans for which the applicant is qualified
    print(f"Found {len(bank_data_filtered)} qualifying loans")

    # Return list of banks willing to underwrite the applicant's loan
    return bank_data_filtered


# Function to allow applicant to save qualified loans to a csv file
def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # Determine the number of loans in the list
    count_qualifying_loans = len(qualifying_loans)
    
    # Determine if applicant is qualified for any loans. If the number of loans for which they are qualified is zero, indicate they have not qualified for any and exit.
    if count_qualifying_loans > 0:

       # Prompt to confirm if user would like to save their list of loans
       confirm_csv_save = questionary.confirm("Would you like to save your list of qualified loans?").ask()
       if confirm_csv_save == True:
           
           # Prompt user to indicate where they would like to save the loan
           save_csvpath = questionary.text("Where would you like to save this file?").ask()
           
           # Check if directory exists. If yes, add file to existing directory, if no, create directory and add file. 
           if os.path.isdir(os.path.dirname(save_csvpath)):
              save_csvpath = Path(save_csvpath)
           else:
               os.mkdir(os.path.dirname(save_csvpath))
               save_csvpath = Path(save_csvpath)
    else:
        sys.exit("Sorry! You do not qualify for any loans.")
    
    header = ["Lender", "Max Loan Amount" , "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    
    # Pass 'qualifying_loan' list and 'save_csvpath' into the 'save_csv' function
    return save_csv(save_csvpath, qualifying_loans, header)   
 

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
