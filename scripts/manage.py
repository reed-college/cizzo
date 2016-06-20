from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import csv

from blop.app import app, db

from blop import models

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def loc_seed():

    models.Location.query.delete()

    with open('location_codes.csv', 'r') as csvfile:
        loccodereader = csv.DictReader(csvfile, delimiter=',')
        for row in loccodereader:
            loccode = models.Location(name=row['name'], general=row[
                                              'general'])
            db.session.add(loccode)
            db.session.commit()


@manager.command
def type_seed():

    models.Type.query.delete()

    with open('incident_types.csv', 'r') as csvfile:
        typereader = csv.DictReader(csvfile, delimiter=',')
        for row in typereader:
            typecode = models.Type(code=row['code'],
                                   description=row['description'])
            db.session.add(typecode)
            db.session.commit()


@manager.command
def add_fake_incidents():

    models.Incident.query.delete()

    # insert function to add fake incidents
    # location = location = models.Location.query.filter(models.Location.name == "Foster").first()
    # types = [models.Type.query.filter(models.Type.code == "UAA").first(), models.Type.query.filter(models.Type.code == "THEB").first(), models.Type.query.filter(models.Type.code == "HARA").first()]
    # incident = models.Incident(
    #                            datetime = datetime.datetime(2016, 8, 13, 19, 00)
    #                            summary = "practice event"
    #                            types = types
    #                            location = location
    # )



if __name__ == '__main__':
    manager.run()