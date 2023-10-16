import pandas as pd
import json

def extract_price_and_sales_data(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Initialize variables to store the extracted data
    extracted_data = []

    # Iterate through the columns and rows to identify "price" and "sales"
    for _, row in df.iterrows():
        price = None
        sales = None

        for column in df.columns:
            cell_value = row[column]

            # Check if the cell contains a numeric value (you can customize this condition)
            if pd.notna(cell_value) and isinstance(cell_value, (int, float)):
                if price is None:
                    price = cell_value
                elif sales is None:
                    sales = cell_value
                else:
                    break  # Exit the loop if both price and sales are found

        # Append the extracted data to the list
        if price is not None and sales is not None:
            extracted_data.append({
                "price": price,
                "sales": sales,
                "timestamp": row.get("timestamp", None)
            })

    # Convert the extracted data to JSON
    json_data = json.dumps(extracted_data)

    return json_data

# Example usage
csv_file_path = "your_csv_file.csv"  # Replace with the actual file path
json_data = extract_price_and_sales_data(csv_file_path)

# You can store or visualize the json_data as needed
