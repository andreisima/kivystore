from kivy import utils
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior

from store.manager import Manager
from rest.manager import APIManager


manager = Manager()
rest = APIManager()

Builder.load_file('modules/switchmodule.kv')


class SwitchesBox (BoxLayout):
    """docstring for SwitchesBox"""
    def __init__(self, **kwargs):
        super(SwitchesBox, self).__init__(**kwargs)
        self.padding = 5
        manager.switch_manager.register_module(self)
        self.register_event_type('on_init_data')

    def on_init_data(self):
        objs = manager.switch_manager.get_all()
        for obj in objs:
            ms = SwitchBox(uuid=obj.uuid)
            self.ids.container.add_widget(ms)


class SwitchBox (ButtonBehavior, BoxLayout):
    """docstring for MySwitch"""
    uuid = NumericProperty()
    name = StringProperty()
    val = BooleanProperty()
    updated_at = StringProperty()
    # on = \uFA19
    # off = \uFA18
    icon = StringProperty()
    color = ListProperty()

    def __init__(self, uuid, **kwargs):
        super(SwitchBox, self).__init__(**kwargs)
        self.register_event_type('on_obj_change')
        self.uuid = uuid
        self.populate_data()

    def populate_data(self):
        manager.switch_manager.register_component(self, self.uuid)
        data_obj = manager.switch_manager.get_object(self.uuid)
        self.name = data_obj.human_name
        self.val = data_obj.value
        self.updated_at = data_obj.updated_at.strftime('%d-%m %H:%M:%S')
        self.icon = '\uFA19' if self.val is True else '\uFA18'
        self.color = utils.get_color_from_hex('#008951') if self.val is True else utils.get_color_from_hex('#3D0900')

    def action(self):
        rest.patch(self.uuid, not self.val)

    def on_obj_change(self, value, updated_at):
        self.val = value
        self.icon = '\uFA19' if self.val is True else '\uFA18'
        self.color = utils.get_color_from_hex('#008951') if self.val is True else utils.get_color_from_hex('#3D0900')
        self.updated_at = updated_at.strftime('%d-%m %H:%M:%S')
