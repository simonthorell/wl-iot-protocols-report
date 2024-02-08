# Wireless Protocols Report

### Purpose of the Report
This report aims to guide in selecting wireless communication protocols for IoT
devices, focusing on efficiency, cost, scalability, and reliability. We compare
WiFi, Bluetooth, Bluetooth LE, Zigbee, Z-Wave, and NFC across various parameters
such as range, data rate, power consumption, and security, to aid stakeholders
in making informed decisions for IoT applications.

### Areas to Investigate
- Protocol Cverwiev
- Range
- Power Consumption
- Security
- Other Considerations for IoT

### Authors
Simon Thorell, Erik Pettersson, Nathan Tewelde Bahta, 
Milad Isho Saeb and Abdihakim Abdisamad Roble.

### Download the report: [PDF](https://github.com/simonthorell/wl-protocols-report/pdfs/REPORT.pdf)

<BR>
## WIFI

Here is some text...

### Protocol Overview
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Range
Some text...

### Power Consumption
Some text...

### Security
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Other Considerations for IoT
1) List item
2) List item
3) List item
<BR>
## Bluetooth

Here is some text...

### Protocol Overview
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Range
Some text...

### Power Consumption
Some text...

### Security
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Other Considerations for IoT
1) List item
2) List item
3) List item
<BR>
## Bluetooth LE

Bluetooth Low Energy (Bluetooth LE, colloquially BLE, formerly marketed as Bluetooth Smart) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries. Compared to Classic Bluetooth, Bluetooth LE is intended to provide considerably reduced power consumption and cost while maintaining a similar communication range.

### Protocol Overview
- Bluetooth LE is renowned for its low power consumption, making it an ideal choice for battery-operated devices. Key features include:

- Low Energy Operation: BLE is optimized for low power use at a reduced data rate.
Adaptive Frequency Hopping: Increases the robustness of communication by avoiding channels with interference.

### Range
Bluetooth LE can achieve a communication range of up to 100 meters (328 feet) in open space, though this is highly dependent on environmental factors and the capabilities of the specific devices being used.

### Power Consumption
BLE's power efficiency is one of its most significant advantages:

- Devices can operate for months or even years on a tiny battery by efficiently managing sleep and active modes.
- The actual power consumption depends on usage patterns, broadcast frequency, and data volume.

### Security
Bluetooth LE provides several security features to protect against eavesdropping and man-in-the-middle attacks:

1) Encryption: AES-128 bit encryption for securing data transmission.
2) Authentication: Features to verify the identity of connected devices.
3) Privacy: Random address techniques prevent tracking of devices.

### Other Considerations for IoT
Bluetooth LE is highly suitable for Internet of Things (IoT) applications due to:

1) Low Cost: BLE devices are relatively inexpensive to manufacture.
2) Ubiquity: BLE is supported by a vast array of modern smartphones, tablets, and PCs, facilitating easy interactions with IoT devices.
3) Community and Support: A broad community and robust ecosystem of tools and libraries support BLE development.
  
This technology's combination of low power consumption, robust security features, and widespread support makes Bluetooth LE an excellent choice for developing a wide range of IoT applications.
<BR>
## Zigbee

Here is some text...

### Protocol Overview
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Range
Some text...

### Power Consumption
Some text...

### Security
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Other Considerations for IoT
1) List item
2) List item
3) List item
<BR>
## Z-Wave

Z-Wave is a wireless communications protocol used primarily for home automation. It is designed to allow smart devices to communicate with each other within the home via low-energy radio waves. Developed by Zensys, a Danish company, it is now managed by the Z-Wave Alliance, a consortium of over 700 companies dedicated to the development of Z-Wave technology.

### Protocol Overview
- Z-Wave operates on a mesh network topology, enabling devices to communicate with each other by forwarding messages across the network. Key features include:

- Low Energy Operation: Z-Wave is designed for low power consumption, extending the battery life of devices.
- Mesh Networking: Devices can act as repeaters, extending the range and reliability of the network.

### Range
Z-Wave networks can cover a typical home, with a range of approximately 30 meters (98 feet) indoors. The mesh network architecture allows devices to work together to extend coverage and overcome obstacles.

### Power Consumption
Z-Wave's power efficiency ensures that battery-operated devices, such as sensors and locks, can last for years on a single battery charge:

- Devices are designed to minimize energy use, entering sleep mode when not actively communicating.
- The actual power consumption varies based on device activity and network configuration.

### Security
Z-Wave includes several layers of security to safeguard against unauthorized access and ensure secure communication:

1) AES-128 Encryption: Provides strong encryption for data transmission.
2) S2 Security Framework: Enhances security with secure key exchange and device pairing procedures.
3) Device Authentication: Ensures that only authorized devices can join the network.

### Other Considerations for IoT
Z-Wave is particularly well-suited for smart home and IoT applications due to:

1) Interoperability: Z-Wave ensures that devices from different manufacturers can work together seamlessly.
2) Wide Adoption: Over 2,600 certified products available, making it easy to find devices that fit specific needs.
3) Dedicated Frequency: Operates on a dedicated frequency band (typically 908.42 MHz in the US, varying by country), reducing interference from other wireless devices.

Z-Wave's combination of low power consumption, strong security measures, and extensive interoperability makes it a preferred choice for smart home automation and IoT ecosystems.
<BR>
## NFC

Here is some text...

### Protocol Overview
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Range
Some text...

### Power Consumption
Some text...

### Security
- Here is also some variant.
- Here is also some variant.
- Here is also some variant.

### Other Considerations for IoT
1) List item
2) List item
3) List item
<BR>

### Protocol Summaries

- **WiFi** emerges as the go-to choice for high-bandwidth applications requiring internet access, 
although at the cost of higher power consumption.
- **Bluetooth** and **Bluetooth LE** offer versatility, with BLE being particularly advantageous 
for battery-operated devices due to its low energy profile.
- **Zigbee** and **Z-Wave** stand out in creating extensive, low-power mesh networks, 
ideal for home automation and sensor networks.
- **NFC** offers a unique niche in close-proximity, secure transactions and data exchange.

### Conclusion: Choosing the Right Wireless Protocol for IoT

Selecting a wireless protocol is crucial, with each serving specific IoT needs.
The choice hinges on application, range, throughput, power, and interoperability.
This report aims to help IoT developers in making protocol choices, the key to efficient and
scalable IoT solutions. Embracing the right protocol is strategic, essential for
IoT innovation and advancement.