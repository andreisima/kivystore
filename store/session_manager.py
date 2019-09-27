from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from store.models.switch_model import Switch
from store.models.sensor_model import Sensor

engine = create_engine('sqlite:///:memory:', echo=False)

# create a Session
Session = sessionmaker(bind=engine)
Switch.metadata.create_all(bind=engine)
Sensor.metadata.create_all(bind=engine)


class SessionManager(object):
    def __init__(self):
        self.session = Session()
