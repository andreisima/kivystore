import dateutil.parser
# from kivy.event import EventDispatcher
from store.models.switch_model import Switch
from store.session_manager import SessionManager


class SwitchManager(SessionManager):

    modules = []
    components = []

    def initial_data(self, data):
        for d in data:
            sw = Switch()
            sw.uuid = d['uuid']
            sw.name = d['name']
            sw.human_name = d['human_name']
            sw.value = d['sw_value']
            # fix typo in backend
            print(d['upddated_at'])
            date_time_obj = dateutil.parser.parse(d['upddated_at'])
            sw.updated_at = date_time_obj
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
        objs = self.session.query(Switch).all()
        self.session.close()
        return objs

    def get_object(self, uuid):
        obj = self.session.query(Switch).get(uuid)
        self.session.close()
        return obj

    def update_object(self, uuid, value, updated_at):
        updated_at = dateutil.parser.parse(updated_at)
        self.session.query(Switch).filter(Switch.uuid == uuid).update(
            {
                'value': value,
                'updated_at': updated_at
            },
        )
        for component in self.components:
            for (k, v) in component.items():
                if k == uuid:
                    v.dispatch('on_obj_change', value, updated_at)
        self.session.close()
