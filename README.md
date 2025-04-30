# Light Scheduler
![image](https://github.com/user-attachments/assets/3a321eef-3340-4eb3-ac8f-55c5e7fdb487)


## Overview
Light Scheduler is a web application designed to help users schedule the on and off times for their lights. The application utilizes WebSocket for real-time communication and MQTT for message handling. This project features a new user interface theme that enhances user experience while maintaining the same core functionality.

## Features
- Schedule light on and off times using a user-friendly interface.
- Real-time connection status updates.
- Recommendations for running the `subscriber.py` script to ensure proper functionality.

## Getting Started

### Prerequisites
- Python 3.x
- Paho MQTT library
- A serial connection to an Arduino or similar device

### Installation
1. Clone the repository:
   ```
   git clone (https://github.com/amani-patrick/LightScheduler.git)
   cd lightScheduler
   ```

2. Install the required Python packages:
   ```
   pip install paho-mqtt
   ```

3. Ensure that your Arduino is connected to the specified serial port (e.g., COM3).

### Running the Application
1. Start the MQTT broker (if not already running).
2. Run the `subscriber.py` script to listen for incoming messages:
   ```
   python subscriber.py
   ```
3. Open `index.html` in a web browser to access the Light Scheduler interface.

### Usage
- Set the desired ON and OFF times using the time input fields.
- Click the "Submit Schedule" button to send the schedule to the server.
- Hover over the status display to see the connection status and a reminder to run `subscriber.py`.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
