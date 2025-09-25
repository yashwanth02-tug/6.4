import csv

def read_iot_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse values, handle missing as None
            temp = row.get('temperature', '').strip()
            hum = row.get('humidity', '').strip()
            sensor_id = row.get('sensor_id', '').strip()
            timestamp = row.get('timestamp', '').strip()

            def to_float(val):
                try:
                    return float(val)
                except ValueError:
                    return None

            temp = to_float(temp)
            hum = to_float(hum)

            data.append({
                'timestamp': timestamp,
                'sensor_id': sensor_id,
                'temperature': temp,
                'humidity': hum
            })
    return data


def forward_fill(data, key):
    last_val = None
    for row in data:
        if row[key] is None:
            row[key] = last_val
        else:
            last_val = row[key]
    # If first values are None, fill with 0
    for row in data:
        if row[key] is None:
            row[key] = 0.0
    return data


def rolling_mean(data, key, window=5):
    values = [row[key] for row in data]
    means = []
    for i in range(len(values)):
        window_vals = values[max(0, i - window + 1):i + 1]
        mean = sum(window_vals) / len(window_vals) if window_vals else 0.0
        means.append(mean)
    for i, row in enumerate(data):
        row[key + '_detrended'] = row[key] - means[i]
    return data


def standard_scale(data, input_key, output_key):
    vals = [row[input_key] for row in data]
    mean = sum(vals) / len(vals) if vals else 0.0
    std = (sum((v - mean) ** 2 for v in vals) / len(vals)) ** 0.5 if vals else 1.0
    if std == 0:
        std = 1.0
    for row in data:
        row[output_key] = (row[input_key] - mean) / std
    return data


def encode_sensor_ids(data):
    sensor_ids = sorted(set(row['sensor_id'] for row in data))
    id_map = {sid: idx for idx, sid in enumerate(sensor_ids)}
    for row in data:
        row['sensor_id_encoded'] = id_map[row['sensor_id']]
    return data


def write_processed_iot_csv(data, output_file):
    fieldnames = [
        'timestamp', 'sensor_id', 'sensor_id_encoded',
        'temperature', 'temperature_detrended', 'temperature_scaled',
        'humidity', 'humidity_detrended', 'humidity_scaled'
    ]
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({
                'timestamp': row['timestamp'],
                'sensor_id': row['sensor_id'],
                'sensor_id_encoded': row['sensor_id_encoded'],
                'temperature': row['temperature'],
                'temperature_detrended': row['temperature_detrended'],
                'temperature_scaled': row['temperature_scaled'],
                'humidity': row['humidity'],
                'humidity_detrended': row['humidity_detrended'],
                'humidity_scaled': row['humidity_scaled']
            })


def main():
    filename = input("Enter IoT CSV filename: ")
    data = read_iot_csv(filename)

    # Fill missing values
    data = forward_fill(data, 'temperature')
    data = forward_fill(data, 'humidity')

    # Detrend
    data = rolling_mean(data, 'temperature', window=5)
    data = rolling_mean(data, 'humidity', window=5)

    # Standard scale detrended data → correctly map to *_scaled
    data = standard_scale(data, 'temperature_detrended', 'temperature_scaled')
    data = standard_scale(data, 'humidity_detrended', 'humidity_scaled')

    # Encode sensor IDs
    data = encode_sensor_ids(data)

    # Write final output
    output_file = 'processed_' + filename
    write_processed_iot_csv(data, output_file)
    print(f" A structured dataset optimized for anomaly detection.")


if __name__ == "__main__":
    main()
