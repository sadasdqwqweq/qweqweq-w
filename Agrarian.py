from Workers.WorkerAndFired import Worker

class Agrarian(Worker):
    chief = None
    duty_agrar = None
    tools = None

    def __init__(self, last, first, father, sex, rate, type_work,position,insurance, military_ID):
        super().__init__(last, first, father, sex, rate,type_work,position, insurance, military_ID)

    def add_duty_agrar(self, new_duty):
        self.duty_agrar = new_duty
        return self.duty_agrar

    def add_tools(self, new_tools):
        self.tools = self.tools + new_tools
        return self.tools

    def add_chief(self, new_chief):
        self.chief = new_chief
        return self.chief

    def change_chief(self, new_chief):
        self.chief = new_chief
        return self.chief

    def change_duty_agrar(self, new_duty):
        self.duty_agrar = self.duty_agrar + new_duty
        return self.duty_agrar

    def change_tools(self, new_tools):
        self.tools = new_tools
        return self.tools

    def clear_chief(self):
        self.chief = None
        return self.chief

    def clear_duty_agrar(self):
        self.duty_agrar = None
        return self.duty_agrar

    def clear_tools(self):
        self.tools = None
        return self.tools

    def clear_all_agr_info(self):
        self.clear_chief()
        self.clear_duty_agrar()
        self.clear_tools()