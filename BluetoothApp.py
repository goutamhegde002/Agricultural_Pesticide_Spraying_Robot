import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import bluetooth

class BluetoothApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Create label
        label = Label(text="Pesticide Spraying Robot Control")
        layout.add_widget(label)
        
        # Create buttons for robot control
        buttons = {
            "Forward": "F",
            "Backward": "B",
            "Left": "L",
            "Right": "R",
            "Stop": "S",
            "Spray Left": "S",
            "Spray Right": "T"
        }

        for button_text, command in buttons.items():
            button = Button(text=button_text, size_hint=(1, 0.2))
            button.bind(on_press=lambda btn, cmd=command: self.send_bluetooth_command(cmd))
            layout.add_widget(button)

        return layout

    def send_bluetooth_command(self, command):
        # Bluetooth address and port
        bd_addr = "XX:XX:XX:XX:XX:XX"  # Replace with your Bluetooth module's MAC address
        port = 1

        try:
            # Connect to Bluetooth device
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((bd_addr, port))

            # Send command
            sock.send(command)

            # Close connection
            sock.close()

        except bluetooth.btcommon.BluetoothError as err:
            print(f"Bluetooth error: {err}")

if __name__ == "__main__":
    BluetoothApp().run()
