# Function to convert date format
def convert_date_format(date_str):
    try:
        # Split the input date string
        year, month, day = date_str.split('-')
        # Return in the new format
        return f"{day}-{month}-{year}"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Take input from user
date_input = input("Enter a date (YYYY-MM-DD): ")
converted_date = convert_date_format(date_input)

# Show result
print(converted_date)
