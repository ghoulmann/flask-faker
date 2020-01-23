from profile_generator.profile import Profile
from profile_generator.device import Device
from random import randint
import json
class Person(Profile):
    def __init__(self):
        Profile.__init__(self)
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.name = self.first_name + " " + self.last_name
        self.address = self.fake.address()
        self.ssn = self.fake.ssn()
        self.zip = self.address[:5]
        self.street = self.getLocation("street")
        self.state = self.getLocation("state")
        self.city = self.getLocation("city")
        self.phone = self.fake.phone_number()
        self.position = self.fake.job()
        self.employer = self.fake.company() + ", " + self.fake.company_suffix()
        self.password = self.fake.password()
        self.username = self.fake.user_name()
        del(self.fake)
    def getLocation(self, part):
        try:
            split_address = self.address[:-6].split("\n")
            if part == "street":
                return split_address[0]
            elif part == "citystate":
                return split_address[1]
            elif part == "state":
                citystate = split_address[1].split(', ')
                return citystate[1]
            elif part == "city":
                citystate = split_address[1].split(',')
                return citystate[0]
            else:
                pass
        except IndexError:
            pass
    def get_json_str(self):
        j = json.dumps(self.__dict__, indent=4)
        return j
    def json_out(self):
        dt = {}
        dt[self.username] = self.__dict__
        #dt.update(vars(self))
        #with open(path, '+w')as file:
        #    json.dump(dt, file, indent=4)
        #return dt
        #print(type(dt))
        #json_string = json.dumps(dt, indent=4)
        return dt

    def write_json(self, path):
        dt = {}
        dt.update(vars(self))
        with open(path, '+w')as file:
            json.dump(dt, file, indent=4)
