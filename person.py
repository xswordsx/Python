class Person:
    _object_set = set()

    @property
    def object_set():
        return [:]_object_set

    @property
    def name(self):
            return self._name

    @name.setter
    def name(self, value):
            if isinstance(value, str):
                    self._name = value

    @property
    def birth_year(self):
            return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
            if isinstance(value, int):
                    self._birth_year = value
            else:
                    self._birth_year = 2013

    @property
    def gender(self):
            return self._gender

    @gender.setter
    def gender(self, value):
            if value == "M" or value == "F":
                    self._gender = value

    @property
    def mother(self):
            return self._mother

    @staticmethod
    def parentChecker(self, value):
            return self is not value and type(value) == type(self)

    @staticmethod
    def is_direct_successor(self, other):
            return (other in self.children) or (self in other.children)

    @mother.setter
    def mother(self, value):
            if parentChecker(self, value) and value.gender == "F":
                    self._mother = value

    @property
    def father(self):
            return self._father

    @father.setter
    def father(self, value):
            if parentChecker(self, value) and value.gender == "M":
                    self._father = value

    def __init__(self, name="Unknown", birth_year=2013, gender="M"):
            self.name = name
            self.birth_year = birth_year
            self.gender = gender
            self._mother = None
            self._father = None
            self._brothers = list()
            self._sisters = list()
            Person._object_set.add(self)

    def get_brothers(self):
            return self._brothers

    def get_sisters(self):
            return self._sisters

    def children(self):
            returningSet = list()
            for person in Person._object_set:
                if person.mother == self or person.father == self:
                    returningSet.append(person)
            return returningSet
