# Stemmler Calculator

This script analyzes student course data and calculates various scores based on their clinical experiences and course timing.

> **Note**: This is a sample script that may need to be adjusted based on your institution's specific data structure and requirements.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files to your local machine.

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your input Excel file with the following requirements:

   - File must have a sheet named "Courses"
   - Required columns: Acad Yr, ID, Course Name, Is ICE, Begin Date, End Date, Grad Date, Intensive, Clinical

   > **Important**: Column names and data formats should match your institution's data structure. You may need to modify the script to accommodate different column names or additional requirements.

2. Place your input Excel file in the same directory as the script and name it "Stemmler.Scores.Sample.xlsx"

3. Run the script:

   ```bash
   python stemmler_calculator.py
   ```

4. The script will generate a new Excel file named "Stemmler_Results.xlsx" containing two sheets:

   **Sheet 1: Results**

   - ID (original student identifier)
   - Consortium ID
   - Intensive Rigor Score
   - Clinical Rigor Score
   - Time Score
   - comment

   **Sheet 2: Processed Input Data**
   Contains the original input data with additional calculated columns:

   - Weeks
   - Jan Date
   - Is 2H
   - 2H Weeks

## Output Calculations

- **Consortium ID**: Formatted as "1-<grad_year>-<index>", where index is a 4-digit number starting at 0001 for each graduation year
- **Intensive Rigor Score**: Total intensive weeks / 52 (capped at 1)
- **Clinical Rigor Score**: Total clinical weeks / 52 (capped at 1)
- **Time Score**: Total clinical weeks in second half / Total second half weeks (capped at 1)
  - Only counts weeks from courses that are both clinical AND occur after Jan 4th of the second year

## Common Scenarios and Edge Cases

1. **Overlapping Courses**:

   - If a student takes multiple clinical courses simultaneously in the second half of the year, their weeks may add up to more than their actual 2H Weeks
   - Example: A student has two 6-week clinical courses that run concurrently after Jan 4th
     - Course A: 6 weeks
     - Course B: 6 weeks (same dates as Course A)
     - Total clinical weeks counted: 12 weeks
     - If 2H Weeks = 12, Time Score = 1.0 (capped at 1)

2. **Score Capping**:
   - All scores (Intensive Rigor, Clinical Rigor, Time Score) are capped at 1.0
   - Scores may reach 1.0 through various combinations of courses
   - Example: A student with 60 weeks of clinical courses will still receive a Clinical Rigor Score of 1.0 (not 1.15)

## Data Processing Notes

- Records without graduation dates are automatically removed
- Student indexing in Consortium ID resets to 0001 for each graduation year
- All scores are capped at 1.0

## Customization Notes

This script may need adjustments for:

- Different column names in your input data
- Additional institutional requirements
- Different calculation methods
- Special cases specific to your institution
- Different date formats
- Additional validation rules

## Error Handling

The script includes basic error handling and will display an error message if:

- The input file is not found
- The required columns are missing
- There are issues with data formatting

## Support

For any issues or questions, please open an issue in the repository.

## Disclaimer

This script is provided as a sample implementation and may need significant modifications to work with your specific institutional data and requirements. Always validate the results against your institution's standards and requirements before using in production.
#   S t e m m l e r . C a l c u l a t i o n 
 
 
