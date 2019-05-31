from Workers.WorkerAndFired import Worker


class Manager(Worker):
    duty_of_mng = None
    subject = None

    def __init__(self, last, first, father, sex, rate, type_work, position, insurance, military_ID):
        super().__init__(last, first, father, sex, rate, type_work, position, insurance, military_ID)

    def add_subject(self, new_sub):
        self.subject = self.subject + new_sub
        return self.subject

    def change_subject(self, new_sub):
        self.subject = new_sub
        return self.subject

    def clear_subject(self):
        self.subject = None
        return self.subject

    def add_duty_of_mng(self, new_duty):
        self.duty_of_mng = self.duty_of_mng + new_duty
        return self.duty_of_mng

    def change_duty_of_mng(self, new_duty):
        print(self.duty_of_mng)
        self.duty_of_mng = new_duty
        return self.duty_of_mng

    def clear_duty_of_mng(self):
        self.duty_of_mng = None
        return self.duty_of_mng

    def clear_all_manager(self):
        self.clear_duty_of_mng()
        self.clear_subject()

