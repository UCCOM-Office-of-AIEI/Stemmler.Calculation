<div align="center">
    <h1>📊 Stemmler Calculation Workscript</h1>
    <p>A tool for analyzing student clinical course data and calculating experience scores.</p>
    <div>
        <a href="#prerequisites">Prerequisites</a> •
        <a href="#installation">Installation</a> •
        <a href="#usage">Usage</a> •
        <a href="#calculations">Calculations</a> •
        <a href="#scenarios">Scenarios</a>
    </div>
    <br>
    <blockquote>
        <strong>Note:</strong> This is a sample script that may need to be adjusted based on your institution's specific data structure and requirements.
    </blockquote>
</div>

<hr>

<h2 id="prerequisites">🚀 Prerequisites</h2>
<ul>
    <li>Python 3.7 or higher</li>
    <li>pip (Python package installer)</li>
</ul>

<h2 id="installation">💻 Installation</h2>
<ol>
    <li>Clone this repository or download the files to your local machine.</li>
    <li>
        <p>Create a virtual environment (recommended):</p>
        <pre><code>python -m venv venv</code></pre>
    </li>
    <li>
        <p>Activate the virtual environment:</p>
        <details>
            <summary>Windows</summary>
            <pre><code>venv\Scripts\activate</code></pre>
        </details>
        <details>
            <summary>macOS/Linux</summary>
            <pre><code>source venv/bin/activate</code></pre>
        </details>
    </li>
    <li>
        <p>Install the required packages:</p>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h2 id="usage">📝 Usage</h2>
<ol>
    <li>
        <p>Prepare your input Excel file with the following requirements:</p>
        <details>
            <summary><strong>Required Columns (click to expand)</strong></summary>
            <ul>
                <li>Acad Yr</li>
                <li>ID</li>
                <li>Course Name</li>
                <li>Is ICE</li>
                <li>Begin Date</li>
                <li>End Date</li>
                <li>Grad Date</li>
                <li>Intensive</li>
                <li>Clinical</li>
            </ul>
        </details>
        <blockquote>
            <strong>Important:</strong> Column names and data formats should match your institution's data structure.
        </blockquote>
    </li>
    <li>Place your input Excel file in the same directory as the script and name it <code>Stemmler.Scores.Sample.xlsx</code></li>
    <li>
        <p>Run the script:</p>
        <pre><code>python stemmler_calculator.py</code></pre>
    </li>
</ol>

<h3>Output Files</h3>
<div>
    <h4>Sheet 1: Results</h4>
    <ul>
        <li>ID (original identifier)</li>
        <li>Consortium ID</li>
        <li>Intensive Rigor Score</li>
        <li>Clinical Rigor Score</li>
        <li>Time Score</li>
        <li>comment</li>
    </ul>

    <h4>Sheet 2: Processed Input Data</h4>
    <p>Contains original columns plus:</p>
    <ul>
        <li>Weeks</li>
        <li>Jan Date</li>
        <li>Is 2H</li>
        <li>2H Weeks</li>
    </ul>

</div>

<h2 id="calculations">🧮 Output Calculations</h2>
<ul>
    <li><strong>Consortium ID:</strong> <code>1-&lt;grad_year&gt;-&lt;index&gt;</code>
        <ul>
            <li>index starts at 0001 for each graduation year</li>
        </ul>
    </li>
    <li><strong>Intensive Rigor Score:</strong> Total intensive weeks / 52 (capped at 1)</li>
    <li><strong>Clinical Rigor Score:</strong> Total clinical weeks / 52 (capped at 1)</li>
    <li><strong>Time Score:</strong> Total clinical weeks in second half / Total second half weeks (capped at 1)
        <ul>
            <li>Only counts weeks from courses that are both clinical AND occur after Jan 4th of the second year</li>
        </ul>
    </li>
</ul>

<h2 id="scenarios">📋 Common Scenarios</h2>
<div>
    <h3>1. Overlapping Courses</h3>
    <details>
        <summary>Example Scenario</summary>
        <pre>
Student has two concurrent 6-week clinical courses after Jan 4th:
Course A: 6 weeks
Course B: 6 weeks (same dates)
Total weeks counted: 12
2H Weeks: 12
Result: Time Score = 1.0 (capped)</pre>
    </details>

    <h3>2. Score Capping</h3>
    <details>
        <summary>Example Scenario</summary>
        <pre>

Student has 60 weeks of clinical courses:
Total weeks: 60
Divided by 52: 1.15
Final Score: 1.0 (capped)</pre>

</details>

</div>

<h2>🔍 Data Processing Notes</h2>
<ul>
    <li>❌ Records without graduation dates are removed</li>
    <li>🔄 Student indexing resets to 0001 for each graduation year</li>
    <li>📊 All scores are capped at 1.0</li>
</ul>

<h2>⚙️ Customization Notes</h2>
<p>This script may need adjustments for:</p>
<ul>
    <li>📝 Different column names</li>
    <li>🏢 Institutional requirements</li>
    <li>🧮 Calculation methods</li>
    <li>📅 Date formats</li>
    <li>✅ Validation rules</li>
</ul>

<h2>⚠️ Error Handling</h2>
<p>The script will show errors for:</p>
<ul>
    <li>Missing input file</li>
    <li>Missing required columns</li>
    <li>Data format issues</li>
</ul>

<h2>💬 Support</h2>
<p>For issues or questions, please open an issue in the repository.</p>

<div align="center">
    <h2>⚖️ Disclaimer</h2>
    <p><strong>This script is provided as a sample implementation.</strong><br>
    Validate all results against your institution's standards before production use.</p>
</div>
#   S t e m m l e r . C a l c u l a t i o n 
 
 
