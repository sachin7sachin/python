Bank Management System

This is a Bank Management System built using Python, which allows users to create accounts, perform various banking operations, and manage their transactions. The system is designed with key functionalities such as account creation, deposit, withdrawal, balance checking, transaction history, and user details modification. It leverages object-oriented programming (OOP) principles and maintains the customer and transaction data using dictionaries.

Features

- Account Creation: Allows users to create a bank account by providing necessary details like name, age, phone number, Aadhar, address, pin, and initial balance.
- Balance Checking: Users can check their bank balance by entering their account number and pin.
- Deposit: Users can deposit money into their account, and transaction details are recorded.
- Withdraw: Users can withdraw money from their account with balance verification, and transactions are logged.
- Pin Change: Users can change their account pin after verifying their identity.
- User Details Modification: Allows users to modify personal details like name, phone number, or age.
- Money Transfer: Facilitates transferring money between two accounts, verifying account details and balance.
- Mini Statement: Users can view their transaction history including the date, type of transaction, amount, and balance.


Key Features & Functions:

Account Management:

- Account creation with unique Aadhar number validation.
- Personal details such as name, phone, age can be modified.

Transactions:

- Deposit and withdraw money with detailed transaction records.
- Money transfer functionality using account numbers and IFSC code validation.

Security:

- PIN validation for performing sensitive actions like balance checking, withdrawals, and transfers.
- The system ensures only authenticated users can access their accounts.

Transaction History:

- Users can view their transaction history (mini statement) with details such as transaction type, date, and amount.

Technology Stack:

- Language: Python 3
- Concepts Used: Object-Oriented Programming (OOP), Data structures (Dictionary), Error handling, Date & Time handling

Example Usage:

- Creating a new account: The system asks for basic details (name, age, phone, etc.) and creates a new account with a unique account number.

- Deposit and Withdrawal: Users can deposit or withdraw money from their account by entering the amount. The system will validate if the transaction is possible and update the balance.

- Transfer Money: Users can transfer money to another account by entering the receiver's account number and IFSC code.

- Mini Statement: Users can view their transaction history with transaction type, date, and balance updates.

Installation:

Clone the repository:

- git clone https://github.com/yourusername/bank-management-system.git

Navigate to the project directory:

- cd bank-management-system

Run the Python script:

- python bank_system.py
