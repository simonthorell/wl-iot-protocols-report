## Zigbee

Zigbee is a short-range protocol with high scaleability for use of upwards to 65000 units.
The protocol is typically used for cases where you have multiple devices with low range that sends low
data-rate and low-power consumption applications and is an open standard.

The criterias for comparison were choosen to make it clearer wether or not a certain protocol
is right for your specific use case. Or more likely a brief introduction to the different protocols
and their capabilities.

### Protocol Overview
As mentioned before the most common use case for Zigbee is indoors, why? Because the most effective range
for Zigbee is 1-10m indoors. So what does this mean? Well Zigbee can be a great protocol for home automation,
industrial automation aswell as smart metering system.

Because of it's low data rate and power consumption you can use Zigbee for devices like garage doors, locks, lights, motion sensors and much more. Think of all the things you have home such as smoke alarms etc connected that sends data to for example your smart phone for you to monitor. All of this can be acheieved with Zigbee, at a lower power consumption than Bluetooth and Wifi, 20-50% cheaper than for example Z-Wave devices. Zigbee is also backed as a protocol by Philips, Samsung, Siemens & Whirlpool.

It also recently started to being used by Amazon, Apple and Google where they integrate it into 
their smart speakers and smart screens. Zigbee also uses the 2.4 GHz band as WiFi does.
Which makes Zigbee protocol available to all around the world so you can use the devices anywhere you want.

### Range

Indoors up to 10-100 meters
Outdoors up to 250 meters

Depends on interference with the signal, by that it means if obstacles in the environment and the power output from the devices. Zigbee devices in some cases also uses a mesh networking feature which extends the signal by make the signal "bounce" off of or through multiple devices.

### Power Consumption

Since Zigbee uses a low power consumption compared to other wireless protocols like WiFi, it is great suited for devices that is powered by battery. Zigbee is designed to consume a minimal power in idle mode or "sleep" mode. Which means it consumes in the range of microwatts or minimalwatts. It is hard to say what the lifetime is for different batteries inside Zigbee devices, but in devices that sends low data rate the battery can last months or years on a single charge.

### Security
Network: 

Key Establishment:
Devices with zigbee protocol, uses network keys to make communication between devices secure on a Zigbee network.

Link key Encryption:
You can also use link keys or encrypted keys which makes communcation between devices confidential.

Frame Counter:
Frame counters are for to prevent replay attacks. Which makes each message unique so there wont be replays of other messages sent before.

Application:

Application-Level Encryption:
The Zigbee protocol also support encryption on the application layer. It is a symmetric encryption
that is being used AES (Advanced Encryption Standard). This is to ensure that sensitive data exchange
between devices are being protected inside the network.

Message Authentication Codes(MACs):
"MACs" Media Access Control are also used in the Zigbee protocol. Which means that the
integrity is ensured so unauthorized modification is not made to the data during transmission. 
This makes all the messages tracable back to the device, which makes it easy to see if a specific
device "belongs" on the network or not. 

Key Transport:
Within the network it also securly transports keys between devices which makes the
distribution of keys effecient and secure.
            
Trust center:
Within Zigbee there is also a "trust center" which is responsible for management of keys.
It distributes and facilitates key establishment.
The trust center is also responsible for the authentication process. It authenticates
devices joining the network and establish each devices privileges.

Cryptographic Techniques:
As mentioned before it primarily uses AES for encryption and decryption of data in both
the network layer and application layer. Zigbee uses hash functions aswell for example SHA-256 to ensure the generation of message authentication, that ensures data integrity. Random number generations is also used to prevent patterns that are predictable inside security protcols. How? they generate cryptographic keys.

Security settings:
Zigbee has configurable security settings that can be specified to your certain use case.
This let's network admins to make changes to the security settings for their application.
The typical settings are encryption length of keys and the rotation intervals for the keys.
This is changed through the trust center settings.

### Pros & Cons
Pros:
- low power consumption
- high scaleability upwards to 60000 units.
- backed by big companies and used by big companies
- secure connections (CIA)
- costs less than other devices using for example Z-Wave

Cons: 
- low data rate transfer
- short range
- interupted signal if there are obstacles
- latency with more devices
- may need complex knowledge to use to it full potential

### Conclusion
Zigbee as a protocol should mainly be used for low data rate transmissions such as home automation for
garage doors, lamps, smoke alarms, monitoring water usage and such. That doesn't require more than 10 meters
in distance between the devices and as little as possible obstacles between the devices for the best signal.
It can also be used for industrial automation and monitoring different sensors outside. But be aware that
it needs to be some kind of amplifier to make the signal reach longer outside. Also to take in to consideration is that you need a pretty good understanding in IT to use the protocol to it's full potential. Over all the protocol is very secure to use in the sense that the protocol is both backed and used by companies such as Amazon, Google, Philips, Siemens etc. The protocol uses "CIA" in different layers and can be configure to suit the specific use case for the admin or admins on the network.