#include <string>
#include <iostream>
#include <thread>
#include <vector>
using namespace std;

void print(int n, const string &str) {
    cout<< "Printing Integer: " << n << endl;
    cout<< "Printing String: "<< str << endl;
}

int main() {
    vector<string> s = {
        "Educative.blog",
        "Educative",
        "courses",
        "are great"
    };

    vector<thread> threads;

    for(int i=0; i<s.size(); i++)
        threads.push_back(thread(print, i, s[i]));
    
    // Joining all the threads, which ever finishes first
    for(auto &th: threads)
        th.join();
    
    return 0;
}