#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>

using namespace std;

string simpleHash(string& input) {
    unsigned long long total = 0;
    int prime = 3; // a prime nuymber used in the hash function

    // Iterate over each character in the string and calculate the hash
    for(char c : input)
        total = total * prime + c;

    // Convert the hash into a hexadecimal string for consitent length output
    stringstream stream;
    stream << hex << total;
    string result(stream.str());

    // Padding the result to ensure a fixed length output
    while(result.length() < 32)
        result = "0" + result;

    return result.substr(0,32);
}

int main() {
    string input;
    cout << "Enter a string: ";
    cin >> input;
    cout << "Hash: " << simpleHash(input) << endl;
    return 0;    
}