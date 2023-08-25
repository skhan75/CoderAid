#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <chrono>

using namespace std;

const int numPhilosphers = 5;

class DiningPhilosphers {

private:
    vector<mutex> forks;

public:
    DiningPhilosphers() : forks(numPhilosphers) {}

    void dine(int philospher) {
        while(true) {
            think(philospher);
            eat(philospher);
        }
    }

    void think(int philospher) {
        cout << "Philospher " << philospher << " is thinking " << endl;
        this_thread::sleep_for(chrono::milliseconds(500));
    }
    
    void eat(int philospher) {
        int leftFork = philospher;
        int rightFork = (philospher + 1) % numPhilosphers;

        // Ensure the odering on the forks to prevent deadlock
        if(philospher == numPhilosphers - 1)
            swap(leftFork, rightFork);

        lock(forks[leftFork], forks[rightFork]);
        lock_guard<mutex> lockLeft(forks[leftFork], adopt_lock);
        lock_guard<mutex> lockRight(forks[rightFork], adopt_lock);

        cout << "Philosopher " << philospher << " is eating." << endl;
        this_thread::sleep_for(chrono::milliseconds(500));
    }

};

int main() {
    DiningPhilosphers philosophers;
    vector<std::thread> philosopherThreads;

    for (int i = 0; i < numPhilosphers; ++i)
        philosopherThreads.push_back(thread(&DiningPhilosphers::dine, &philosophers, i));

    for (int i = 0; i < numPhilosphers; ++i) 
        philosopherThreads[i].join();

    return 0;
}