#include <cstdint>
#include <stdexcept>
#include <cstring>
#include <iostream>

using namespace std; 

class RectBuffer {
public:
    uint8_t* buffer;    // Pointer to the new buffer
    size_t width;       // Width of the new buffer (x_width)
    size_t height;      // Height of the new buffer (y_width)

    RectBuffer(uint8_t* src_buf, size_t row_size, size_t src_width, size_t src_height, 
            size_t x, size_t y, size_t x_width, size_t y_height) {

        // Validate inputs 
        if(!src_buf) {
            throw::invalid_argument("Source buffer is null");
        }        

        if(x + x_width > src_width || y + y_height > src_height) {
            throw::out_of_range("Requested rectangle is out of source buffer bounds");
        }

        if(row_size > src_width) {
            std::invalid_argument("Row size is less than source width");
        }

        // Initialize width and height
        width = x_width;
        height = y_height;

        // Allocate new buffer
        buffer = new uint8_t[width * height];

        // Copy data row by row
        for(size_t row = 0; row < height; ++row) {
            // Source pointer: start of the desired row in the source buffer
            uint8_t* src_ptr = src_buf + (y + row) * row_size + x;

            // Destination pointer: start of the row in the new buffer
            uint8_t* dst_ptr = buffer + row * width;

            // Copy x_width bytes from source to destination
            memcpy(dst_ptr, src_ptr, width);
        }
    }

    // Destructor
    ~RectBuffer() {
        delete[] buffer;
    }

    // Copy Constructor
    RectBuffer(const RectBuffer& other) : width(other.width), height(other.height) {
        buffer = new uint8_t[width * height];
        memcpy(buffer, other.buffer, width * height);
    }

    // Assignment operator
    RectBuffer& operator=(const RectBuffer& other) {
        if (this != &other) {
            delete[] buffer;
            width = other.width;
            height = other.height;
            buffer = new uint8_t[width * height];
            std::memcpy(buffer, other.buffer, width * height);
        }
        return *this;
    }

    // Move constructor
    RectBuffer(RectBuffer&& other) noexcept
        : buffer(other.buffer), width(other.width), height(other.height) {
        other.buffer = nullptr;
        other.width = 0;
        other.height = 0;
    }

    // Move assignment operator
    RectBuffer& operator=(RectBuffer&& other) noexcept {
        if (this != &other) {
            delete[] buffer;
            buffer = other.buffer;
            width = other.width;
            height = other.height;
            other.buffer = nullptr;
            other.width = 0;
            other.height = 0;
        }
        return *this;
    }

};

// Function to print the buffer for demonstration purposes
void printBuffer(uint8_t* buffer, size_t width, size_t height) {
    for (size_t row = 0; row < height; ++row) {
        for (size_t col = 0; col < width; ++col) {
            std::cout << static_cast<int>(buffer[row * width + col]) << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    // Example source buffer (simulated)
    size_t src_width = 8;     // Width of the source buffer
    size_t src_height = 6;    // Height of the source buffer
    size_t row_size = 8;      // Row size (stride) in bytes
    uint8_t src_buf[48];      // Source buffer (8 columns * 6 rows)

    // Initialize the source buffer with some data
    for (size_t i = 0; i < src_width * src_height; ++i) {
        src_buf[i] = static_cast<uint8_t>(i);
    }

    // Define the rectangle to copy
    size_t x = 2;             // Starting x offset in source buffer
    size_t y = 1;             // Starting y offset in source buffer
    size_t x_width = 4;       // Width of the rectangle to copy
    size_t y_height = 3;      // Height of the rectangle to copy

    try {
        // Create a RectBuffer object to copy the rectangle
        RectBuffer rect(src_buf, row_size, src_width, src_height, x, y, x_width, y_height);

        // Print the source buffer for reference
        cout << "Source Buffer:" << std::endl;
        printBuffer(src_buf, src_width, src_height);

        // Print the copied rectangle buffer
        std::cout << "\nCopied Rectangle Buffer:" << std::endl;
        printBuffer(rect.buffer, rect.width, rect.height);

    } catch (const std::exception& e) {
        // Handle any exceptions that may occur
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    // The RectBuffer destructor will automatically clean up the memory
    return 0;
}
