from .managers.switch_manager import SwitchManager
from .managers.sensor_manager import SensorManager


class _Singleton (object):
    instance = None
    class __OnlyOne:

        def __init__(self):
            self.val = None

        def __str__(self):
            return (f'self: {self.val}')
    # Make sure you do not overwite this method

    def __new__(cls):
        if not _Singleton.instance:
            _Singleton.instance = _Singleton.__OnlyOne
        return _Singleton.instance

    def __getattr__(cls):
        return getattr(self.instance, name)

    def __setattr__(cls):
        return setattr(self.instance, name)

    # def __init__(cls):


class Manager (object):

    manager = _Singleton()
    switch_manager = SwitchManager()
    sensor_manager = SensorManager()

    manager.val = {
        'switch_manager': switch_manager,
        'sensor_manager': sensor_manager,
    }

    # def __init__(self, **kwargs):
    #   super(Manager, self).__init__(**kwargs)
    #   self.switch_manager = self.manager.val['switch_manager']
