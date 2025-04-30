import paho.mqtt.client as mqtt
import serial
import json
import time

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

# MQTT configuration
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'light/schedule'

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for serial connection to stabilize

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        schedule = json.loads(payload)
        on_time = schedule['onTime']
        off_time = schedule['offTime']
        
        # Simple logic to send '1' or '0' based on current time
        current_time = time.strftime('%H:%M')
        if current_time >= on_time and current_time < off_time:
            ser.write('1'.encode())
            print(f"Sent '1' to Arduino (Light ON)")
        else:
            ser.write('0'.encode())
            print(f"Sent '0' to Arduino (Light OFF)")
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()