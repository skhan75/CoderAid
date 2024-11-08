/**
 * Image Manipulation - Grayscale and Rotation
 * 
 * Description: Create a program that manages a dynamically allocated 2D buffer representing a
 * grayscale image. Each pixel is a single byte (uint8_t). Implement the functions to:
 * 
 * 1. Convert the image to grayscale
 * 2. Rotate the image by 90 degrees
 * 3. Crop the rectangular portion of the image
 * 
 * Key Concepts:
 * 1. 2D memory management with pointers
 * 2. Working with dynamically allocated buffers.
 * 3. Rotation and manipulation of 2D data.
 * 
 * Input:
 * * A 1D uint8_t array (uint8_t*) representing a 2D grayscale image.
 * * Image width and height.
 * * For the crop function: starting coordinates (x, y) and dimensions (crop_width, crop_height).
 * 
 * Hints:
 * * Use a buffer with `width * height` dimensions and manipulate it by calculating offsets.
 * * Rortation will involve re-mapping `(x,y)` coordinates to the rotated position.
 */

#include <iostream>
#include <cstdint>
#include <stdexcept>
#include <cstring>

class ImageManipulation {
public:
    uint8_t* buffer;    // Pointer to the image buffer
    size_t width;       // Width of the image 
    size_t height;      // Height of the image

    ImageManipulation(uint8_t* src_buffer, size_t img_width, size_t img_height) : width(img_width), 
    height(img_height) {
        // Allocate memory for the buffer and copy the source image data
        buffer = new uint8_t[width * height];
        std::memcpy(buffer, src_buffer, width*height);
    }

    ~ImageManipulation() {
        delete[] buffer;
    }

    // Modify th the brightness of each pixel while ensuring that the result pixel
    // value remains withing the valid grayscale range of 0 to 255
    void adjustBrightness(int adjustment) {
        for(size_t i=0; i<width*height; i++) {
            int newValue = buffer[i] + adjustment;
            buffer[i] = static_cast<uint8_t>(std::max(0, std::min(255, newValue))); // clamp between 0 and 255
        }
    }

    // Rotate the image by 90 degrees
    uint8_t* rotate90Degrees() {
        // Allocate a new buffer for the rotated image
        uint8_t* rotatedBuffer = new uint8_t[width * height];

        // Map (i,j) in the original buffer image to (j, N-1-i) in the rotated image
        for(size_t i=0; i<height; i++) {
            for(size_t j=0; j<width; j++) {
                // (j*height) represents the row in the 1d buffer
                rotatedBuffer[j*height+(height-1-i)] = buffer[i * width + j];
            }
        }

        // Swap the width and height for the rotated buffer
        std::swap(width, height);

        // Delete old buffer and update with rotated buffer
        delete[] buffer;
        buffer = rotatedBuffer;

        return buffer;
    }

    void printBuffer() const {
        for(size_t i=0; i<height; i++) {
            for(size_t j=0; j<width; j++) {
                std::cout << static_cast<int>(buffer[i * width + j]) << " ";
            }
            std::cout << std::endl;
        }
    }

    // Crop a region from the image
    uint8_t* crop(size_t x, size_t y, size_t crop_width, size_t crop_height) {
        if (x + crop_width > width || y + crop_height > height) {
            throw std::out_of_range("Crop dimensions are out of bounds of the original image");
        }

        // Allocate new buffer for cropped image
        uint8_t* croppedBuffer = new uint8_t[crop_width * crop_height];

        // Copy each row within the specified crop region
        for (size_t i = 0; i < crop_height; i++) {
            // Calculate the start index in the source and destination
            uint8_t* src_ptr = buffer + (y + i) * width + x;
            uint8_t* dst_ptr = croppedBuffer + i * crop_width;

            // Copy the row from the source to the cropped buffer
            std::memcpy(dst_ptr, src_ptr, crop_width);
        }

        return croppedBuffer;
    }

};


int main() {
    // Create a sample 4x4 image with values from 0 to 15
    size_t width = 4;
    size_t height = 4;
    uint8_t src_buffer[] = {
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9 ,10, 11,
        12, 13, 14, 15
    };

    ImageManipulation image(src_buffer, width, height);

    std::cout << "Original Image" << std::endl;
    image.printBuffer();

    // Adjust the brightness
    image.adjustBrightness(50);
    std::cout << "After Brightness Adjustment" << std::endl;
    image.printBuffer();

    // Rotate the image by 90 degrees
    image.rotate90Degrees();
    std::cout << "\nAfter 90 Degrees Rotation:" << std::endl;
    image.printBuffer();

    // Crop a 2x2 region from (1,1) 
    uint8_t* croppedImage = image.crop(1, 1, 2, 2);
    std::cout << "\nCropped Image (2x2 from, (1,1)):" << std::endl;
    for (size_t i = 0; i < 2; ++i) {
        for (size_t j = 0; j < 2; ++j) {
            std::cout << static_cast<int>(croppedImage[i * 2 + j]) << " ";
        }
        std::cout << std::endl;
    }

    // Free cropped image memory
    delete[] croppedImage;

    return 0;


}