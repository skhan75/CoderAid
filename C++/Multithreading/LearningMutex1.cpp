#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

/**
 * Mutexes are used to ensure that only one thread can execute a particular section of code at a time, 
 * thus avoiding race conditions or other concurrency-related issues.
 * Consider two threads trying to increment a global counter. Without synchronization, 
 * we might not get the expected result because of the way multi-threading operations are interleaved.
*/
int counter1 = 0, counter2 = 0;

void incrementWithoutSynchronization() {
    for (int i = 0; i < 100000; ++i) ++counter1;
}

mutex mtx;
void incrementWithSynchronization() {
    for(int i=0; i<100000; ++i) {
        mtx.lock();
        ++counter2;
        mtx.unlock();
    }
}

int main() {
    std::thread t1(incrementWithoutSynchronization);
    std::thread t2(incrementWithoutSynchronization);

    t1.join();
    t2.join();

    std::cout << "Counter: " << counter1 << std::endl;

    std::thread t3(incrementWithSynchronization);
    std::thread t4(incrementWithSynchronization);

    t3.join();
    t4.join();

    std::cout << "Counter: " << counter2 << std::endl;
    return 0;
}