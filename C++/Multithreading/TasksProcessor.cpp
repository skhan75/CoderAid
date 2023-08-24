#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <functional>
#include <future> // represents a future result from an asynchronous operation
#include <list>

using namespace std;

class TaskProcessor {

private:
    vector<function<void()>> buffer;
    // Mutexes are used to ensure that only one thread can execute a particular section
    // of code at a time, thus avoiding race conditions or other concurrency-related issues.
    mutex mtx;
    const int BUFFER_LIMIT = 10;
    vector<thread> threadPool; // Pool to store threads
    const int MAX_THREADS = 5; // Max threads at any time

    void flushTasks() {
        // Capture tasks to be executed in this batch
        auto tasksToExecute = buffer;
        buffer.clear(); // clear the buffer

        // Create a newq thread to process this batch 
        thread worker([tasksToExecute]() {
            for(const auto& task : tasksToExecute) {
                task();
            }
        });

        // Add the thread to the thread pool
        threadPool.push_back(move(worker));

        // If too many threads, wait for all to finish before continuing
        if(threadPool.size() == MAX_THREADS) {
            for(auto& t : threadPool) t.join();
            threadPool.clear();
        }
       
    }

public:
    void runTask(const function<void()>& task) {
        {
            lock_guard<mutex> lock(mtx); // Lock for thread safety when modifhying the buffer
            buffer.push_back(task); // Add the task to the buffer
        }

        // Check if the buffer has reached the limit
        if(buffer.size() == BUFFER_LIMIT) {
            flushTasks(); // flush the tasks if buffer is full
        }
    }

    // Destructor to ensure any remaining tasks are processed when the object is destroyed
    ~TaskProcessor() {
        if (!buffer.empty()) {
            cout << "Flushing the remaining tasks.." << endl;
            flushTasks();
        }

        // Join any remaining threads
        for (auto& t : threadPool) {
            if (t.joinable()) t.join();
        }
    }
};

int main() {
    TaskProcessor processor;

      // Simulate adding tasks to the TaskProcessor
    for (int i = 0; i < 100; ++i) {
        processor.runTask([i]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(50)); // Simulating work
            std::cout << "Executing task " << i << " on thread " << std::this_thread::get_id() << "\n";
        });
    }

    // Allow some buffer time for tasks to finish if running asynchronously (not in this case, but added for completeness)
    std::this_thread::sleep_for(std::chrono::seconds(1));

    return 0;
}