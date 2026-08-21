#include <iostream>
#include <iomanip>
#include <string>
#include <stdexcept>

// Use 128-bit integers to support numbers way past 18 quintillion
typedef unsigned __int128 uint128_t;

// Helper function to print 128-bit numbers to the screen
void print_u128(uint128_t n) {
    if (n == 0) { std::cout << "0"; return; }
    std::string s;
    while (n > 0) {
        s = char('0' + (n % 10)) + s;
        n /= 10;
    }
    std::cout << s;
}

// Helper function to safely read massive text strings into a 128-bit integer
uint128_t parse_u128(const std::string& s) {
    uint128_t result = 0;
    for (char c : s) {
        if (c < '0' || c > '9') {
            throw std::invalid_argument("Invalid character in 128-bit integer string");
        }
        result = result * 10 + (c - '0');
    }
    return result;
}

void check_collatz_loops_fast(uint128_t limit) {
    std::cout << "Starting high-performance C++ loop verification...\n";
    
    // We start checking from 2 up to our target limit
    for (uint128_t i = 2; i <= limit; ++i) {
        uint128_t n = i;
        uint128_t slow = i; // For Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
        bool cycle_detected = false;

        // Loop until the number drops below its starting point
        // If it drops below 'i', it's guaranteed safe because 1 to i-1 are already verified!
        while (n >= i) {
            // Advanced Cycle Detection: Tortoise moves 1 step, Hare (n) moves 2 steps
            if (n % 2 == 0) n /= 2;
            else n = 3 * n + 1;

            if (n % 2 == 0) n /= 2;
            else n = 3 * n + 1;

            if (slow % 2 == 0) slow /= 2;
            else slow = 3 * slow + 1;

            if (n == slow) {
                cycle_detected = true;
                break;
            }
        }

        if (cycle_detected) {
            std::cout << "\n🚨 ALERT: Hidden loop found starting at: ";
            print_u128(i);
            std::cout << "\n";
            return;
        }

        // Print progress every 10 million numbers so you know it's working
        if (i % 10000000 == 0) {
            std::cout << "Verified up to: ";
            print_u128(i);
            std::cout << "\n";
        }
    }

    std::cout << "\n✅ Verification complete up to limit! No hidden loops found.\n";
}

int main() {
    // Pass your 50 quintillion target limit safely as a string text
    uint128_t target_limit = parse_u128("50000000000000000000"); 
    
    // Note: For testing your compiler instantly, consider lowering this to "100000000" (100 million)
    check_collatz_loops_fast(target_limit);
    return 0;
}
