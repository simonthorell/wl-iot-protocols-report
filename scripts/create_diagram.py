import json
import matplotlib.pyplot as plt

# Assuming the JSON data is loaded from 'protocols_data.json'
with open('protocols_data.json', 'r') as file:
    data = json.load(file)

protocols = [protocol['name'] for protocol in data['protocols']]

# Process ranges (assuming meters are specified and ranges may be given)
range_values = []
for protocol in data['protocols']:
    range_str = protocol['range']
    # Extract numbers, assuming ' meters' is always present
    if '-' in range_str:
        min_range, max_range = [int(val.split(' ')[0]) for val in range_str.split('-')]
        range_values.append((min_range + max_range) / 2)
    else:
        range_values.append(int(range_str.split(' ')[0]))

# Process frequencies (count occurrence of each frequency)
frequency_counts = {}
for protocol in data['protocols']:
    freqs = protocol['frequency'].split(', ')
    for freq in freqs:
        if freq not in frequency_counts:
            frequency_counts[freq] = 0
        frequency_counts[freq] += 1

# Process data rates (convert all to Mbps)
# Function to convert data rate to Mbps
def convert_to_mbps(data_rate_str):
    converted_rates = []
    rates = data_rate_str.split('-')
    for rate in rates:
        parts = rate.strip().split(' ')
        if len(parts) == 2:
            # If the rate includes both a number and a unit
            number, unit = parts
            number = float(number)
            if 'Kbps' in unit:
                number /= 1000  # Convert Kbps to Mbps
            elif 'Gbps' in unit:
                number *= 1000  # Convert Gbps to Mbps
        elif len(parts) == 1 and parts[0].isdigit():
            # If the rate is just a number (assuming Mbps by default)
            number = float(parts[0])
        else:
            # Handle unexpected formats or log an error
            print(f"Unexpected data rate format: '{rate}'")
            number = 0  # Default or error value; adjust as needed
        
        converted_rates.append(number)
    
    return max(converted_rates)

# Updated part for processing data rates
data_rate_values = [convert_to_mbps(protocol['dataRate']) for protocol in data['protocols']]

# Plotting Range
plt.figure(figsize=(10, 6))
plt.bar(protocols, range_values, color='skyblue')
plt.xlabel('Protocol')
plt.ylabel('Average Range (meters)')
plt.title('Range of Different IoT Wireless Protocols')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/protocols_range.png')

# Plotting Frequency Usage
plt.figure(figsize=(10, 6))
plt.bar(frequency_counts.keys(), frequency_counts.values(), color='lightgreen')
plt.xlabel('Frequency')
plt.ylabel('Number of Protocols')
plt.title('Frequency Usage across IoT Wireless Protocols')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/protocols_frequency.png')

# Plotting Data Rate
plt.figure(figsize=(10, 6))
plt.bar(protocols, data_rate_values, color='lightcoral')
plt.xlabel('Protocol')
plt.ylabel('Max Data Rate (Mbps)')
plt.title('Data Rate Comparison across IoT Wireless Protocols')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/protocols_datarate.png')