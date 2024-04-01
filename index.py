import eventlet

import os
import time
from st2reactor.sensor.base import Sensor

class FileChangeSensor(Sensor):
    def __init__(self, sensor_service, config=None):
        super(FileChangeSensor, self).__init__(sensor_service=sensor_service, config=config)
        self.file_path = '/index.txt'
        self.last_modified = None

    def setup(self):
        # Initialization code goes here
        pass

    def run(self):
       while True:
            # Read current file content
            with open(self.file_path, 'r') as f:
                current_content = f.read()

            # Compare current content with previous content
            if current_content != self.previous_content:
                self.sensor_service.dispatch(trigger='file_content_changed',
                                             payload={'file_path': self.file_path,
                                                      'new_content': current_content})
                self.previous_content = current_content

            # Sleep for 60 seconds before checking again
            time.sleep(60)

    def cleanup(self):
        # Cleanup code goes here
        pass

        # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass    

# Register the sensor class with the st2 sensor service
sensor = FileChangeSensor()
sensor.setup()
sensor.run()


