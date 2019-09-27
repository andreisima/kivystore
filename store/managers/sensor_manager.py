import dateutil.parser
from store.models.sensor_model import Sensor
from store.session_manager import SessionManager


class SensorManager(SessionManager):

    modules = []
    components = []

    def initial_data(self, data):
        for d in data:
            sw = Sensor()
            sw.uuid = d['uuid']
            sw.name = d['name']
            sw.human_name = d['human_name']
            sw.value = d['sensor_current_value']
            self.session.add(sw)
        self.session.commit()
        self.session.close()
        for module in self.modules:
            for (k, v) in module.items():
                v.dispatch('on_init_data')

    def register_module(self, module):
        d = {}
        d[id(module)] = module
        self.modules.append(d)

    def register_component(self, component, uuid):
        d = {}
        d[uuid] = component
        self.components.append(d)
        print(self.components)

    def get_all(self):
        objs = self.session.query(Sensor).all()
        return objs

    def get_object(self, uuid):
        obj = self.session.query(Sensor).get(uuid)
        self.session.close()
        return obj

    def update_object(self, uuid, value, updated_at):
        updated_at = dateutil.parser.parse(updated_at)
        self.session.query(Sensor).filter(Sensor.uuid == uuid).update(
            {
                'value': value,
                # 'updated_at': updated_at
            }
        )
        for component in self.components:
            for (k, v) in component.items():
                if k == uuid:
                    v.dispatch('on_obj_change', value, updated_at)
        self.session.close()
