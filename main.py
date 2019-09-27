from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import encodings.idna # noqa F401 ignore import not used
from rest.manager import APIManager
from message.service import MessageService
from modules.switchmodule import SwitchesBox # noqa F401 ignore import not used
from modules.sensormodule import SensorsBox  # noqa F401 ignore import not used


from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 10)
Config.set('graphics', 'top', 35)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'borderless', 1)

rest = APIManager()
rest.get_init_data()

message = MessageService()  # message service init

Builder.load_file('main.kv')


class MainLayout (BoxLayout):
    pass


class StoresqliteApp (App):

    def build(self):
        return MainLayout()


if __name__ == '__main__':
    StoresqliteApp().run()
