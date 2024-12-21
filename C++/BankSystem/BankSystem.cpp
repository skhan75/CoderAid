#include "BankSystem.hh"
#include <_time.h>
#include <chrono>
#include <iostream>
#include <string>
#include <unordered_map>
#include <stdexcept>
#include <iomanip>

class Account : public IAccount {
  
private:
  std::string accountHolder;
  std::string accountNumber;
  double balance;

public:
  Account(const std::string& accountHolder, const std::string& accountNumber, double initialBalance) : accountHolder(accountHolder), accountNumber(accountNumber), balance(initialBalance) {
    if(initialBalance < 0) {
      throw std::invalid_argument("Initial balance cannot be negative.");
    }
  }

  const std::string& getAccountNumber() const override {
    return accountNumber;
  }

  double getBalance() const override {
    return balance;
  }

  void deposit(double amount, const std::string& timestamp) override {
    if(amount <= 0) {
      throw std::invalid_argument("Deposit amount shhould be greater than 0");
    }

    balance += amount;
    std::cout << "[" << timestamp << "] Deposit: " << amount << " to account " << accountNumber << std::endl;
  }

  void withdraw(double amount, const std::string& timestamp) override {
    if(balance <= 0) {
      throw std::runtime_error("Zero balance.");
    }

    if(amount <= 0) {
      throw std::invalid_argument("Invalid amount - should be a positive number");
    }

    if(amount > balance) {
      throw std::runtime_error("Insufficient balance");
    }

    balance -= amount;
    std::cout << "[" << timestamp << "] Withdraw: " << amount << " from account " << accountNumber << std::endl;
  }

  void pay(double amount, const std::string& timestamp) override {
    withdraw(amount, timestamp);
  }
  
  void displayAccountInfo() const override {
    std::cout << "Account Holder: " << accountHolder << std::endl;
    std::cout << "Account Number: " << accountNumber << std::endl;
    std::cout << "Balance: $" << std::fixed << std::setprecision(2) << balance << std::endl;
  }
};


class BankSystem : public IBankSystem {
private:
  std::unordered_map<std::string, Account> accounts;

  std::string generateAccountNumber() {
    static int counter = 1000;
    return "ACC" + std::to_string(counter++);
  }

  std::string getCurrentTimestamp() const {
    auto now = std::chrono::system_clock::now();
    auto time = std::chrono::system_clock::to_time_t(now);
    char buffer[26];
    ctime_r(&time, buffer);
    buffer[24] = '\0'; // Remove newline character
    return std::string(buffer);
  }  

public:
  std::string createAccount(const std::string& holder, double initialBalance) override {
    std::string accountNumber = generateAccountNumber();
    std::string timestamp = getCurrentTimestamp();
    accounts.emplace(accountNumber, Account(holder, accountNumber, initialBalance));
    std::cout << "[" << timestamp << "] Account created: " << accountNumber << " for " << holder << std::endl;
    return accountNumber;
  }

  void deposit(const std::string& accountNumber, double amount) override {
    auto it = accounts.find(accountNumber);
    if(it == accounts.end()) {
      throw std::runtime_error("Account not found!");
    }
    std::string timestamp = getCurrentTimestamp();
    it->second.deposit(amount, timestamp);
  }

  void withdraw(const std::string& accountNumber, double amount) override {
    auto it = accounts.find(accountNumber);
    if(it == accounts.end()) {
      throw std::runtime_error("Account not found!");
    }
    std::string timestamp = getCurrentTimestamp();
    it->second.withdraw(amount, timestamp);
  }

  void pay(const std::string& accountNumber, double amount) override {
    std::string timestamp = getCurrentTimestamp();
    withdraw(accountNumber, amount);
  }
  
  void transfer(const std::string& fromAccount, const std::string& toAccount, double amount) override {
    auto fromIt = accounts.find(fromAccount);
    auto toIt = accounts.find(toAccount);

    if (fromIt == accounts.end() || toIt == accounts.end()) {
      throw std::runtime_error("One or both accounts not found.");
    }

    std::string timestamp = getCurrentTimestamp();
    fromIt->second.withdraw(amount, timestamp);
    toIt->second.deposit(amount, timestamp);

    std::cout << "[" << timestamp << "] Transfer: " << amount << " from account " << fromAccount << " to account " << toAccount << std::endl;
  }

  void displayAccountInfo(const std::string& accountNumber) const override {
    auto it = accounts.find(accountNumber);
    if (it == accounts.end()) {
      throw std::runtime_error("Account not found.");
    }
    it->second.displayAccountInfo();
  }
};

void runTests() {
  BankSystem bank;

  try {
    // Test creating accounts
    std::string acc1 = bank.createAccount("Alice", 1000.0);
    std::string acc2 = bank.createAccount("Bob", 500.0);

    // Test displaying account info
    bank.displayAccountInfo(acc1);
    bank.displayAccountInfo(acc2);

    // Test deposit
    bank.deposit(acc1, 200.0);
    bank.displayAccountInfo(acc1);

    // Test withdrawal
    bank.withdraw(acc2, 100.0);
    bank.displayAccountInfo(acc2);

    // Test transfer
    bank.transfer(acc1, acc2, 150.0);
    bank.displayAccountInfo(acc1);
    bank.displayAccountInfo(acc2);

    // Test invalid scenarios
    try {
      bank.withdraw(acc2, 1000.0); // Should throw insufficient balance
    } catch (const std::exception& e) {
      std::cerr << "Caught expected exception: " << e.what() << std::endl;
    }

    try {
      bank.deposit("INVALID_ACC", 100.0); // Should throw account not found
    } catch (const std::exception& e) {
      std::cerr << "Caught expected exception: " << e.what() << std::endl;
    }

    try {
      bank.transfer(acc1, "INVALID_ACC", 50.0); // Should throw account not found
    } catch (const std::exception& e) {
      std::cerr << "Caught expected exception: " << e.what() << std::endl;
    }

  } catch (const std::exception& e) {
    std::cerr << "Error during testing: " << e.what() << std::endl;
  }
}

int main() {
  runTests();
  return 0;
}




