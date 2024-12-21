// BankSystem.hh
#ifndef BANKSYSTEM_HH
#define BANKSYSTEM_HH

#include <string>

class IAccount {
public:
  virtual ~IAccount() = default;
  virtual const std::string& getAccountNumber() const = 0;
  virtual double getBalance() const = 0;
  virtual void deposit(double amount, const std::string& timestamp) = 0;
  virtual void pay(double amount, const std::string& timestamp) = 0;
  virtual void withdraw(double amount, const std::string& timestamp) = 0;
  virtual void displayAccountInfo() const = 0;
};

class IBankSystem {
public:
  virtual ~IBankSystem() = default;
  virtual std::string createAccount(const std::string& holder, double initialBalance) = 0;
  virtual void deposit(const std::string& accountNumber, double amount) = 0;
  virtual void withdraw(const std::string& accountNumber, double amount) = 0;
  virtual void pay(const std::string& accountNumber, double amount) = 0;
  virtual void transfer(const std::string& fromAccount, const std::string& toAccount, double amount) = 0;
  virtual void displayAccountInfo(const std::string& accountNumber) const = 0;
}; 

#endif // BANKSYSTEM_HH
