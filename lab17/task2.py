import csv
import math
def read_stock_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Handle missing values
            closing_price = row.get('closing_price', '').strip()
            volume = row.get('volume', '').strip()
            date = row.get('date', '').strip()
            # Fill missing values with None for now
            closing_price = float(closing_price) if closing_price.replace('.', '', 1).isdigit() else None
            volume = float(volume) if volume.replace('.', '', 1).isdigit() else None
            data.append({
                'date': date,
                'closing_price': closing_price,
                'volume': volume
            })
    return data
def fill_missing_values(data):
    # Forward fill for closing_price and volume
    last_price = None
    last_volume = None
    for row in data:
        if row['closing_price'] is None:
            row['closing_price'] = last_price
        else:
            last_price = row['closing_price']
        if row['volume'] is None:
            row['volume'] = last_volume
        else:
            last_volume = row['volume']
    # If still None (first row), fill with 0
    for row in data:
        if row['closing_price'] is None:
            row['closing_price'] = 0.0
        if row['volume'] is None:
            row['volume'] = 0.0
    return data
def create_lag_features(data):
    # 1-day return: (today - yesterday) / yesterday
    # 7-day return: (today - 7days ago) / 7days ago
    for i, row in enumerate(data):
        # 1-day lag
        if i > 0 and data[i-1]['closing_price'] != 0:
            row['return_1d'] = (row['closing_price'] - data[i-1]['closing_price']) / data[i-1]['closing_price']
        else:
            row['return_1d'] = 0.0
        # 7-day lag
        if i > 6 and data[i-7]['closing_price'] != 0:
            row['return_7d'] = (row['closing_price'] - data[i-7]['closing_price']) / data[i-7]['closing_price']
        else:
            row['return_7d'] = 0.0
    return data
def log_scale_volume(data):
    for row in data:
        v = row['volume']
        # Add 1 to avoid log(0)
        row['log_volume'] = math.log(v + 1) if v is not None else 0.0
    return data
def detect_outliers_iqr(data):
    prices = [row['closing_price'] for row in data if row['closing_price'] is not None]
    prices_sorted = sorted(prices)
    n = len(prices_sorted)
    def percentile(p):
        k = int(round(p * (n + 1))) - 1
        k = max(0, min(k, n-1))
        return prices_sorted[k]
    Q1 = percentile(0.25)
    Q3 = percentile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    for row in data:
        price = row['closing_price']
        row['outlier'] = 1 if (price < lower or price > upper) else 0
    return data
def write_processed_csv(data, output_file):
    fieldnames = ['date', 'closing_price', 'volume', 'return_1d', 'return_7d', 'log_volume', 'outlier']
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({
                'date': row['date'],
                'closing_price': row['closing_price'],
                'volume': row['volume'],
                'return_1d': row['return_1d'],
                'return_7d': row['return_7d'],
                'log_volume': row['log_volume'],
                'outlier': row['outlier']
            })
def main():
    filename = input("Enter stock CSV filename: ")
    data = read_stock_csv(filename)
    data = fill_missing_values(data)
    data = create_lag_features(data)
    data = log_scale_volume(data)
    data = detect_outliers_iqr(data)
    output_file = 'processed_' + filename
    write_processed_csv(data, output_file)
    print(f" A time-series dataset ready for forecasting models.")
if __name__ == "__main__":
    main()
