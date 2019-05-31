from Workers.WorkerAndFired import Worker


class Office(Worker):
    chief = None
    duty_office = None
    unit = None

    def __init__(self, last, first, father, sex, rate,type_work, position,insurance, military_ID):
        super().__init__(last, first, father, sex, rate,type_work,position, insurance, military_ID)

    def change_chief(self, new_chief):
        self.chief = new_chief
        return self.chief

    def clear_chief(self):
        self.chief = None
        return self.chief

    def add_duty_office(self, new_duty):
        self.duty_office = self.duty_office + new_duty
        return self.duty_office

    def change_duty_office(self, new_duty):
        self.duty_office = new_duty
        return self.duty_office

    def clear_duty_office(self):
        self.duty_office = None
        return self.duty_office

    def add_unit(self, new_unit):
        self.unit = self.unit + new_unit
        return self.unit

    def change_unit(self, new_unit):
        self.unit = new_unit
        return self.unit

    def clear_unit(self):
        self.unit = None
        return self.unit

    def clear_all_office(self):
        self.clear_chief()
        self.clear_unit()
        self.clear_duty_office()
