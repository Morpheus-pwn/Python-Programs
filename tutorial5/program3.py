import pandas as pd

def write_data_to_excel(data, excel_file_path, sheet_name='Sheet1'):

    try:
        df = pd.DataFrame(data)  # Convert data to DataFrame if necessary
        df.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
        print(f"Data successfully written to {excel_file_path}, sheet '{sheet_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

data1 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 22],
         'Occupation': ['Engineer', 'Teacher', 'Student']}

excel_path1 = 'example1.xlsx'
write_data_to_excel(data1, excel_path1)