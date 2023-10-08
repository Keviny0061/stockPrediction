#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <map>
int leave = 0;
// Function to calculate the number of days between two dates
// Function to calculate the number of days between two dates
int daysBetweenDates(const std::string& dateStr) {
    std::tm tmReferenceDate = { 0, 0, 0, 8, 1, 113 }; // February 8, 2013
    std::tm tmDate = { 0, 0, 0, 0, 0, 0 }; // Initialize to zero

    std::string numericDateStr; // To store the numeric part of the date

    // Extract numeric characters from the date string
    for (char c : dateStr) {
        if (std::isdigit(c)) {
            numericDateStr += c;
        }
    }

    // Check if the numeric date string has 8 digits
    if (numericDateStr.size() == 8) {
        tmDate.tm_year = std::stoi(numericDateStr.substr(0, 4)) - 1900; // Adjust year
        tmDate.tm_mon = std::stoi(numericDateStr.substr(4, 2)) - 1;    // Adjust month
        tmDate.tm_mday = std::stoi(numericDateStr.substr(6, 2));

        // Convert both tm structs to time_t and calculate the difference in seconds
        std::time_t referenceTime = std::mktime(&tmReferenceDate);
        std::time_t dateTime = std::mktime(&tmDate);

        if (referenceTime != -1 && dateTime != -1) {
            return static_cast<int>((dateTime - referenceTime) / (60 * 60 * 24)); // Convert seconds to days
        }
    }

    // Invalid date format
    return -1;
}

int main() {
    int row = 0;
    // Open the CSV file for reading
    std::ifstream inputFile("all_stocks_5yr.csv");

    if (!inputFile.is_open()) {
        std::cerr << "Error: Unable to open input CSV file." << std::endl;
        return 1;
    }

    // Open the text file for writing
    std::ofstream outputFile("output.txt");

    if (!outputFile.is_open()) {
        std::cerr << "Error: Unable to open output text file." << std::endl;
        inputFile.close();
        return 1;
    }

    std::string line;
    bool isFirstRow = true;  // Flag to skip the first row
    double firstRowValue = 0.0;  // Store the original value of the first row
    double currentValue = 0.0;  // Store the current value for the calculation
    std::string currentCompany;  // Store the current company name

    while (std::getline(inputFile, line)) {
        if (isFirstRow) {
            isFirstRow = false;  // Skip the first row (header row)
            continue;
        }

        std::vector<std::string> columns;
        std::stringstream ss(line);
        std::string column;

        // Split the CSV line into columns
        while (std::getline(ss, column, ',')) {
            columns.push_back(column);
        }

        // Check if the line has at least 7 columns
        if (columns.size() >= 7) {
            bool containsEmptyEntry = false;

            // Check if any entry in the row is empty
            for (const std::string& entry : columns) {
                if (entry.empty()) {
                    containsEmptyEntry = true;
                    break;
                }
            }

            if (containsEmptyEntry) {
                std::cerr << "Warning: Row contains empty entry. Skipping row.\n";
                continue;  // Skip the row with empty entries
            }

            std::string dateStr = columns[0]; // Assuming the first column contains dates
            double value2 = std::stod(columns[1]);  // Convert the second column to a double
            std::string company = columns[6];  // Assuming the seventh column contains the company name

            // Calculate the number of days after February 8, 2013
            int daysDifference = daysBetweenDates(dateStr);

            if (daysDifference >= 0) {
                if (currentCompany != company) {
                    // Reset currentValue and firstRowValue when the company changes
                    currentValue = 0.0;
                    firstRowValue = value2;
                    currentCompany = company;
                }

                // Calculate the change in value from the first row
                double valueChange = value2 - firstRowValue;

                // Output the result to the text file
                leave++;
                if (leave > 150000) {
                    break;
                }
                
                    outputFile << daysDifference << "," << valueChange<< "\n";
                
                



                // Update currentValue for the next row
                currentValue = value2;
                
                

            }
            else {
                std::cerr << "Warning: Invalid date format in line. Skipping line.\n";
            }
        }
        else {
            std::cerr << "Warning: Line does not have 7 columns and will be skipped.\n";
        }
    }

    // Close the input and output files
    inputFile.close();
    outputFile.close();

    std::cout << "Data has been extracted and written to output.txt." << std::endl;
    return 0;
}

