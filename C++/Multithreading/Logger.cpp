/**
 *  Thread-Safe Logger System
    Imagine a distributed system where multiple services or modules are logging information simultaneously. Your task is to design and implement a thread-safe logger system that can handle concurrent log requests without causing any data corruption or race conditions.

    Implement the following class:

    class Logger {
    public:
        Logger();

        // Logs a message with a timestamp
        void log(int timestamp, const std::string& message);

        // Returns the logs starting from a given timestamp
        std::vector<std::string> getLogsSince(int timestamp);
    };

    Requirements:
    Thread-Safety: Multiple threads could be calling the log and getLogsSince methods concurrently. Ensure that the logger behaves correctly.

    Order Preservation: While logs might be written concurrently, they should be stored in the order of their timestamps. If two logs have the same timestamp, the order between them doesn't matter.

    Efficiency: Logging operations should be quick, and retrieving logs should be efficient based on the given timestamp.

    Example:

    Logger logger;

    // Thread A
    logger.log(1, "Started Module A");
    logger.log(3, "Processed data chunk X");

    // Thread B
    logger.log(2, "Started Module B");
    logger.log(4, "Processed data chunk Y");

    // Assuming the above calls, a call to:
    logger.getLogsSince(2);

    // Might return:
    ["Started Module B", "Processed data chunk X", "Processed data chunk Y"]
    Constraints:
    The log function will be called between 1 and 10^5 times.
    The getLogsSince function will be called between 1 and 10^4 times.
    Messages are not longer than 100 characters.
    Timestamps are positive integers and might not be in sequential order.
    Notes:
    Ensure that the implementation can handle the concurrency requirements without deadlocks or race conditions.
    Optimize the system for both logging and log retrieval.
    Consider scenarios where the volume of logs can be massive over time.
*/
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <shared_mutex>
#include <algorithm>

using namespace std;

class Logger {
private:
    map<int, vector<string>> logs;
    mutable shared_timed_mutex logMutex;

public:
    Logger() {}

    // Logs a message with a timestamp
    void log(int timestamp, const string& message) {
        unique_lock<shared_timed_mutex> lock(logMutex);
        logs[timestamp].push_back(message);
    }

    // Returns the logs starting from a given timestamp
    vector<string> getLogsSince(int timestamp) {
        shared_lock<shared_timed_mutex> lock(logMutex);
        vector<string> result;

       for (const auto& logEntry : logs) {
        int ts = logEntry.first;
        const vector<string>& logMessages = logEntry.second;

        if (ts >= timestamp)
            result.insert(result.end(), logMessages.begin(), logMessages.end());
    }

        return result;
    }
};

int main() {
    Logger logger;

    // Sample usage, can be expanded with std::thread for true multithreading demonstration
    logger.log(1, "Started Module A");
    logger.log(3, "Processed data chunk X");
    logger.log(2, "Started Module B");
    logger.log(4, "Processed data chunk Y");

    auto logs = logger.getLogsSince(2);
    for (const auto& log : logs) {
        cout << log << endl;
    }

    return 0;
}
