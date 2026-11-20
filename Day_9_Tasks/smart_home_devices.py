'''A smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance.'''


class WiFiDevice:
    def connect_wifi(self):
        print("WiFi Connected")


class VoiceAssistant:
    def voice_control(self):
        print("Voice Control Activated")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker Features")


# Creating object
s = SmartSpeaker()

# Displaying details
s.display()
s.connect_wifi()
s.voice_control()
