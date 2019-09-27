from kivy.lang import Builder
from kivy.properties import (
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout

from store.manager import Manager
from rest.manager import APIManager


manager = Manager()
rest = APIManager()

Builder.load_file('modules/sensormodule.kv')


class SensorsBox (BoxLayout):
    """docstring for SensorsBox"""

    def __init__(self, **kwargs):
        super(SensorsBox, self).__init__(**kwargs)
        manager.sensor_manager.register_module(self)
        self.register_event_type('on_init_data')

    def on_init_data(self):
        objs = manager.sensor_manager.get_all()
        for obj in objs:
            ms = Sensor(uuid=obj.uuid)
            self.add_widget(ms)


class Sensor (BoxLayout):
    """docstring for MyLabel"""
    name = StringProperty()
    value = StringProperty()

    def __init__(self, uuid, **kwargs):
        super(Sensor, self).__init__(**kwargs)
        self.register_event_type('on_obj_change')
        self.uuid = uuid
        self.populate_data()

    def populate_data(self):
        manager.sensor_manager.register_component(self, self.uuid)
        data_obj = manager.sensor_manager.get_object(self.uuid)
        self.name = data_obj.human_name
        self.value = str(round(data_obj.value, 2))

    def on_obj_change(self, value, updated_at):
        self.value = value
