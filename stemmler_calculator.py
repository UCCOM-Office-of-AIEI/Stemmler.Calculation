import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def calculate_weeks(row):
    """Calculate weeks between two dates, rounded up"""
    delta = (row['End Date'] - row['Begin Date']).days
    return int(np.ceil(delta / 7))

def get_jan_date(acad_yr):
    """Get January 4th date of the second year in academic year"""
    second_year = acad_yr.split('-')[1]
    return pd.to_datetime(f'1/4/{second_year}')

def calculate_2h_weeks(row):
    """Calculate weeks between graduation and January date, rounded up"""
    if pd.isna(row['Grad Date']) or pd.isna(row['Jan Date']):
        return 0
    delta = (row['Grad Date'] - row['Jan Date']).days
    return int(np.ceil(delta / 7))

def process_data(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name='Courses')
    
    # Convert date columns to datetime
    date_columns = ['Begin Date', 'End Date', 'Grad Date']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    
    # Remove entries without graduation dates
    df = df.dropna(subset=['Grad Date'])
    
    # Calculate Weeks
    df['Weeks'] = df.apply(calculate_weeks, axis=1)
    
    # Calculate Jan Date
    df['Jan Date'] = df['Acad Yr'].apply(get_jan_date)
    
    # Calculate Is 2H
    df['Is 2H'] = (df['End Date'] > df['Jan Date']).astype(int)
    
    # Calculate 2H Weeks
    df['2H Weeks'] = df.apply(calculate_2h_weeks, axis=1)
    
    results = []
    
    # Group students by graduation year and sort within each year
    df_grouped = df.groupby(df['Grad Date'].dt.year)
    
    for grad_year, year_group in df_grouped:
        # Get unique students for this graduation year and sort them
        year_students = sorted(year_group['ID'].unique())
        
        for idx, student_id in enumerate(year_students, 1):
            student_data = year_group[year_group['ID'] == student_id]
            
            # Calculate Consortium ID (index resets for each grad year)
            consortium_id = f"1-{grad_year}-{str(idx).zfill(4)}"
            
            # Calculate Intensive Rigor Score
            intensive_weeks = student_data[student_data['Intensive'] == 1]['Weeks'].sum()
            intensive_score = min(intensive_weeks / 52, 1)
            
            # Calculate Clinical Rigor Score
            clinical_weeks = student_data[student_data['Clinical'] == 1]['Weeks'].sum()
            clinical_score = min(clinical_weeks / 52, 1)
            
            # Calculate Time Score
            second_half_clinical_weeks = student_data[
                (student_data['Is 2H'] == 1) & 
                (student_data['Clinical'] == 1)
            ]['Weeks'].sum()
            total_2h_weeks = student_data['2H Weeks'].iloc[0]
            time_score = min(second_half_clinical_weeks / total_2h_weeks if total_2h_weeks > 0 else 0, 1)
            
            results.append({
                'ID': student_id,
                'Consortium ID': consortium_id,
                'Intensive Rigor Score': intensive_score,
                'Clinical Rigor Score': clinical_score,
                'Time Score': time_score,
                'comment': ''
            })
    
    # Create results DataFrame and set column order
    results_df = pd.DataFrame(results)
    column_order = ['ID', 'Consortium ID', 'Intensive Rigor Score', 
                    'Clinical Rigor Score', 'Time Score', 'comment']
    results_df = results_df[column_order]
    return results_df, df  # Return both the results and processed input data

def main():
    try:
        # Process the data and get both results and processed input
        results, processed_input = process_data('Stemmler.Scores.Sample.xlsx')
        
        # Save results to Excel with multiple sheets
        with pd.ExcelWriter('Stemmler_Results.xlsx', engine='openpyxl') as writer:
            results.to_excel(writer, sheet_name='Results', index=False)
            processed_input.to_excel(writer, sheet_name='Processed Input Data', index=False)
            
        print("Analysis complete! Results saved to 'Stemmler_Results.xlsx'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 