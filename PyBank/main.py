import os
import pandas as pd

def analyze_financial_data(file_path, output_file_path):
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute file path for the financial dataset
    file_path = os.path.join(script_directory, 'Resources', 'budget_data.csv')

    # Construct the absolute file path for the output text file
    output_file_path = os.path.join(script_directory, 'analysis', 'output.txt')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Calculate total number of months (excluding header)
    total_months = len(df)

    # Calculate net total amount of Profit/Losses
    net_total = df["Profit/Losses"].sum()

    # Calculate changes in Profit/Losses
    df["Change"] = df["Profit/Losses"].diff()

    # Calculate average change of Profit/Losses
    average_change = df["Change"].mean()

    # Find the greatest increase and decrease in profits
    greatest_increase = df["Change"].max()
    greatest_increase_date = df.loc[df["Change"].idxmax(), "Date"]
    greatest_decrease = df["Change"].min()
    greatest_decrease_date = df.loc[df["Change"].idxmin(), "Date"]

    # Prepare the analysis results
    analysis_results = (
        "Financial Analysis\n"
        "------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${round(average_change, 2)}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    )

    # Print the results to terminal
    print(analysis_results)

    # Export the results to text file
    if output_file_path:
        with open(output_file_path, 'w') as txtfile:
            txtfile.write(analysis_results)

# Run the analysis with relative file paths
analyze_financial_data(None, None)
