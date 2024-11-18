<div align="center">

# 📊 Stemmler Calculator

A tool for analyzing student clinical course data and calculating experience scores.

<p>
    <a href="#prerequisites">Prerequisites</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#output-calculations">Calculations</a> •
    <a href="#common-scenarios-and-edge-cases">Scenarios</a>
</p>

> **Note**: This is a sample script that may need to be adjusted based on your institution's specific data structure and requirements.

</div>

---

## 🚀 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 💻 Installation

1. Clone this repository or download the files to your local machine.

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   <details>
   <summary>Windows</summary>

   ```bash
   venv\Scripts\activate
   ```

   </details>

   <details>
   <summary>macOS/Linux</summary>

   ```bash
   source venv/bin/activate
   ```

   </details>

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Usage

1. Prepare your input Excel file with the following requirements:

   <details>
   <summary>Required Columns (click to expand)</summary>

   - Acad Yr
   - ID
   - Course Name
   - Is ICE
   - Begin Date
   - End Date
   - Grad Date
   - Intensive
   - Clinical
   </details>

   > **Important**: Column names and data formats should match your institution's data structure. You may need to modify the script to accommodate different column names or additional requirements.

2. Place your input Excel file in the same directory as the script and name it `Stemmler.Scores.Sample.xlsx`

3. Run the script:

   ```bash
   python stemmler_calculator.py
   ```

4. The script will generate `Stemmler_Results.xlsx` containing:

   <table>
   <tr>
   <th>Sheet 1: Results</th>
   <th>Sheet 2: Processed Input Data</th>
   </tr>
   <tr>
   <td>

   - ID (original identifier)
   - Consortium ID
   - Intensive Rigor Score
   - Clinical Rigor Score
   - Time Score
   - comment
   </td>
   <td>

   - Original columns plus:
     - Weeks
     - Jan Date
     - Is 2H
     - 2H Weeks
     </td>
     </tr>
     </table>

## 🧮 Output Calculations

- **Consortium ID**: `1-<grad_year>-<index>`
  - index starts at 0001 for each graduation year
- **Intensive Rigor Score**: Total intensive weeks / 52 (capped at 1)
- **Clinical Rigor Score**: Total clinical weeks / 52 (capped at 1)
- **Time Score**: Total clinical weeks in second half / Total second half weeks (capped at 1)
  - Only counts weeks from courses that are both clinical AND occur after Jan 4th of the second year

## 📋 Common Scenarios and Edge Cases

### 1. Overlapping Courses

<details>
<summary>Example Scenario (click to expand)</summary>

- Student has two concurrent 6-week clinical courses after Jan 4th:
  ```
  Course A: 6 weeks
  Course B: 6 weeks (same dates)
  Total weeks counted: 12
  2H Weeks: 12
  Result: Time Score = 1.0 (capped)
  ```
  </details>

### 2. Score Capping

<details>
<summary>Example Scenario (click to expand)</summary>

- Student has 60 weeks of clinical courses
  ```
  Total weeks: 60
  Divided by 52: 1.15
  Final Score: 1.0 (capped)
  ```
  </details>

## 🔍 Data Processing Notes

- ❌ Records without graduation dates are removed
- 🔄 Student indexing resets to 0001 for each graduation year
- 📊 All scores are capped at 1.0

## ⚙️ Customization Notes

This script may need adjustments for:

- 📝 Different column names
- 🏢 Institutional requirements
- 🧮 Calculation methods
- 📅 Date formats
- ✅ Validation rules

## ⚠️ Error Handling

The script will show errors for:

- Missing input file
- Missing required columns
- Data format issues

## 💬 Support

For issues or questions, please open an issue in the repository.

## ⚖️ Disclaimer

<div align="center">

**This script is provided as a sample implementation.**  
Validate all results against your institution's standards before production use.

</div>
#   S t e m m l e r . C a l c u l a t i o n 
 
 
