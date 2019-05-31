import DataBase
from Workers.WorkerAndFired import *
from Workers.Service import *
from Workers.Office import *
from Workers.Agrarian import *
from Workers.Administration import *
from Workers.HR import *
from Workers.Manager import *
import _pickle


class INandOUTput:

    #Список усіх об'єктів
    main_list = []


    #Додавання нових робітників

    def add_new_worker(self, str):
        a = Worker.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.Data_Base.add_main_info_in_main()
        DataBase.Data_Base.save()

    def add_new_manager(self, str):
        a = Manager.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.Data_Base.add_main_info_in_manager()
        DataBase.Data_Base.save()

    def add_new_admistrator(self,str):
        a = Administrator.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.Data_Base.add_main_info_in_administation()
        DataBase.Data_Base.save()

    def add_new_agrarian(self, str):
        a = Agrarian.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.Data_Base.add_main_info_in_agrararian()
        DataBase.Data_Base.save()

    def add_new_service(self,str):
        a = Service.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.data_for_set = [DataBase.fullname, DataBase.ID]
        DataBase.Data_Base.add_main_info_in_service()
        DataBase.Data_Base.save()

    def add_new_HR(self, str):
        a = HR.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.data_for_set = [DataBase.fullname, DataBase.ID]
        DataBase.Data_Base.add_main_info_in_hr()
        DataBase.Data_Base.save()

    def add_new_office(self, str):
        a = Office.new_worker(str)
        INandOUTput.main_list.append(a)
        DataBase.data = a.main_data
        DataBase.fullname = a.fullname
        DataBase.ID = a.ID
        DataBase.Data_Base.add_main_info_in_office()
        DataBase.Data_Base.save()


    #Зміна даних об'єктів, які стосуються класу Worker

    def change_last(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_last(new)
        DataBase.fullname = o.fullname
        DataBase.ID = o.ID
        DataBase.Data_Base.change_main_info_fullname()
        if o == Service:
            DataBase.Data_Base.change_main_info_fullname_service()
        elif o == Agrarian:
            DataBase.Data_Base.change_main_info_fullname_agr()
        elif o == Administrator:
            DataBase.Data_Base.change_main_info_fullname_adm()
        elif o == Manager:
            DataBase.Data_Base.change_main_info_fullname_mng()
        elif o == HR:
            DataBase.Data_Base.change_main_info_fullname_hr()
        elif o == Office:
            DataBase.Data_Base.change_main_info_fullname_office()

        DataBase.Data_Base.save()


    def change_rate(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_rate(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.rate
        DataBase.Data_Base.change_main_info_rate()
        if o == Service:
            DataBase.Data_Base.change_main_info_rate_service()
        elif o == Agrarian:
            DataBase.Data_Base.change_main_info_rate_agr()
        elif o == Administrator:
            DataBase.Data_Base.change_main_info_rate_adm()
        elif o == Manager:
            DataBase.Data_Base.change_main_info_rate_mng()
        elif o == HR:
            DataBase.Data_Base.change_main_info_rate_hr()
        elif o == Office:
            DataBase.Data_Base.change_main_info_rate_office()
        DataBase.Data_Base.save()

    def change_position(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        DataBase.ID = o.ID
        o.change_position(new)
        DataBase.data_for_set = o.position
        DataBase.Data_Base.change_main_info_position()
        if o == Service:
            DataBase.Data_Base.change_main_info_position_service()
        elif o == Agrarian:
            DataBase.Data_Base.change_main_info_position_agr()
        elif o == Administrator:
            DataBase.Data_Base.change_main_info_position_adm()
        elif o == Manager:
            DataBase.Data_Base.change_main_info_position_mng()
        elif o == HR:
            DataBase.Data_Base.change_main_info_position_hr()
        elif o == Office:
            DataBase.Data_Base.change_main_info_position_office()
        DataBase.Data_Base.save()

    def change_type_work(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        DataBase.ID = o.ID
        o.change_type_work(new)
        DataBase.data_for_set = o.type_work
        DataBase.Data_Base.change_main_info_position()
        if o == Service:
            DataBase.Data_Base.change_main_type_of_work_service()
        elif o == Agrarian:
            DataBase.Data_Base.change_main_type_of_work_agr()
        elif o == Administrator:
            DataBase.Data_Base.change_main_type_of_work_adm()
        elif o == Manager:
            DataBase.Data_Base.change_main_type_of_work_mng()
        elif o == HR:
            DataBase.Data_Base.change_main_type_of_work_hr()
        elif o == Office:
            DataBase.Data_Base.change_main_type_of_work_office()
        DataBase.Data_Base.save()

    def change_military_ID(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_military_ID(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.military_ID
        DataBase.Data_Base.change_main_info_military_ID()
        if o == Service:
            DataBase.Data_Base.change_main_info_military_ID_service()
        elif o == Agrarian:
            DataBase.Data_Base.change_main_info_military_ID_agr()
        elif o == Administrator:
            DataBase.Data_Base.change_main_info_military_ID_adm()
        elif o == Manager:
            DataBase.Data_Base.change_main_info_military_ID_mng()
        elif o == HR:
            DataBase.Data_Base.change_main_info_military_ID_hr()
        elif o == Office:
            DataBase.Data_Base.change_main_info_military_ID_office()
        DataBase.Data_Base.save()

    def change_insurance(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_insurance(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.insurance
        DataBase.Data_Base.change_main_info_insurance()
        if o == Service:
            DataBase.Data_Base.change_main_info_insurance_service()
        elif o == Agrarian:
            DataBase.Data_Base.change_main_info_insurance_agr()
        elif o == Administrator:
            DataBase.Data_Base.change_main_info_insurance_adm()
        elif o == Manager:
            DataBase.Data_Base.change_main_info_insurance_mng()
        elif o == HR:
            DataBase.Data_Base.change_main_info_insurance_hr()
        elif o == Office:
            DataBase.Data_Base.change_main_info_insurance_office()
        DataBase.Data_Base.save()


    # Зміни об'єктів класу Administrator

    def change_chief_of_adm(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_chief(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.chief
        DataBase.Data_Base.change_administation_chief()
        DataBase.Data_Base.save()

    def clear_chief(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_chief()
        DataBase.ID = o.ID
        DataBase.Data_Base.change_administation_chief()
        DataBase.Data_Base.save()

    def add_duty_of_adm(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_duty_of_adm(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_of_adm
        DataBase.Data_Base.change_administation_duty_of_adm()
        DataBase.Data_Base.save()

    def change_duty_of_adm(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_duty_of_adm(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_of_adm
        DataBase.Data_Base.change_administation_duty_of_adm()
        DataBase.Data_Base.save()

    def clear_duty_of_adm(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_duty_of_adm()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_administation_duty_of_adm()
        DataBase.Data_Base.save()

    def add_monitor_of_unit(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_monitor_of_unit(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.monitor_of_unit
        DataBase.Data_Base.change_administation_monitor_of_unit()
        DataBase.Data_Base.save()

    def change_monitor_of_unit(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_monitor_of_unit(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.monitor_of_unit
        DataBase.Data_Base.change_administation_monitor_of_unit()
        DataBase.Data_Base.save()

    def clear_monitor_of_unit(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_monitor_of_unit()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_administation_monitor_of_unit()
        DataBase.Data_Base.save()

    def add_helper(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_helper(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.helper
        DataBase.Data_Base.change_administation_helper()
        DataBase.Data_Base.save()

    def change_helper(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_helper(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.helper
        DataBase.Data_Base.change_administation_helper()
        DataBase.Data_Base.save()

    def clear_helper(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_helper()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_administation_helper()
        DataBase.Data_Base.save()

    def all_adm_clear(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.all_clear_adm()
        DataBase.ID = o.ID
        DataBase.Data_Base.change_administation_chief()
        DataBase.Data_Base.clear_administation_helper()
        DataBase.Data_Base.clear_administation_duty_of_adm()
        DataBase.Data_Base.clear_administation_monitor_of_unit()
        DataBase.Data_Base.save()


    # Зміни об'єктів класу Agrarian

    def add_duty_agrar(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_duty_agrar(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_agrar
        DataBase.Data_Base.change_agr_duty_agrar()
        DataBase.Data_Base.save()

    def change_duty_agrar(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_duty_agrar(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_agrar
        DataBase.Data_Base.change_agr_duty_agrar()
        DataBase.Data_Base.save()

    def clear_duty_agrar(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_duty_agrar()
        DataBase.ID = o.ID
        DataBase.Data_Base.change_agr_duty_agrar()
        DataBase.Data_Base.save()

    def add_tools(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_tools(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.tools
        DataBase.Data_Base.change_agr_tools()
        DataBase.Data_Base.save()

    def change_tools(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_tools(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.tools
        DataBase.Data_Base.change_agr_tools()
        DataBase.Data_Base.save()

    def clear_tools(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_tools()
        DataBase.ID = o.ID
        DataBase.Data_Base.agr_clear_tools()
        DataBase.Data_Base.save()

    def change_chief_of_agrar(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_chief(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.chief
        DataBase.Data_Base.change_agr_chief()
        DataBase.Data_Base.save()

    def add_chief_of_agrar(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_chief(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.chief
        DataBase.Data_Base.change_agr_chief()
        DataBase.Data_Base.save()

    def clear_chief_of_agrar(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_chief()
        DataBase.ID = o.ID
        DataBase.Data_Base.agr_clear_chief()
        DataBase.Data_Base.save()

    def clear_all_agrar(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_all_agr_info()
        DataBase.ID = o.ID
        DataBase.Data_Base.agr_clear_chief()
        DataBase.Data_Base.change_agr_duty_agrar()
        DataBase.Data_Base.agr_clear_tools()
        DataBase.Data_Base.save()


    # Зміни об'єктів класу HR

    def add_duty_of_hr(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_duty_of_hr(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_of_hr
        DataBase.Data_Base.change_hr_duty_of_hr()
        DataBase.Data_Base.save()

    def change_duty_of_hr(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_duty_of_hr(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_of_hr
        DataBase.Data_Base.change_hr_duty_of_hr()
        DataBase.Data_Base.save()

    def clear_duty_of_hr(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_duty_of_hr()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_hr_duty_of_hr()
        DataBase.Data_Base.save()

    def add_for_whom(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_for_whom(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.for_whom
        DataBase.Data_Base.change_hr_for_whom()
        DataBase.Data_Base.save()

    def change_for_whom(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_for_whom(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.for_whom
        DataBase.Data_Base.change_hr_for_whom()
        DataBase.Data_Base.save()

    def clear_for_whom(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_for_whom()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_hr_for_whom()
        DataBase.Data_Base.save()

    def add_positions(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_positions(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.positions
        DataBase.Data_Base.change_hr_positions()
        DataBase.Data_Base.save()

    def change_positions(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_positions(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.positions
        DataBase.Data_Base.change_hr_positions()
        DataBase.Data_Base.save()

    def clear_positions(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_positions()
        DataBase.ID = o.ID
        DataBase.Data_Base.change_hr_positions()
        DataBase.Data_Base.save()

    def clear_all_hr(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_positions()
        DataBase.ID = o.ID
        DataBase.Data_Base.change_hr_positions()
        DataBase.Data_Base.clear_hr_for_whom()
        DataBase.Data_Base.clear_hr_duty_of_hr()
        DataBase.Data_Base.save()


    # Зміни об'єктів класу Manager

    def add_subject(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_subject(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.subject
        DataBase.Data_Base.change_mng_subkject()
        DataBase.Data_Base.save()

    def change_subject(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_subject(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.subject
        DataBase.Data_Base.change_mng_subkject()
        DataBase.Data_Base.save()

    def clear_subject(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_subject()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_mgr_subject()
        DataBase.Data_Base.save()

    def add_duty_of_mng(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_duty_of_mng(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_of_mng
        DataBase.Data_Base.change_magr_duty_of_mgr()
        DataBase.Data_Base.save()

    def change_duty_of_mng(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_duty_of_mng(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_of_mng
        DataBase.Data_Base.change_magr_duty_of_mgr()
        DataBase.Data_Base.save()

    def clear_duty_of_mng(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_duty_of_mng()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_mgr_duty()
        DataBase.Data_Base.save()

    def clear_all_mng(self,id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_duty_of_mng()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_mgr_duty()
        DataBase.Data_Base.clear_mgr_subject()
        DataBase.Data_Base.save()


    # Зміни об'єктів класу Office

    def change_chief_office(self,id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_chief(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.chief
        DataBase.Data_Base.change_office_chief()
        DataBase.Data_Base.save()

    def clear_chief_office(self,id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_chief()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_office_chief()
        DataBase.Data_Base.save()

    def add_duty_office(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_duty_office(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_office
        DataBase.Data_Base.change_office_chief()
        DataBase.Data_Base.save()

    def change_duty_office(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_duty_office(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.duty_office
        DataBase.Data_Base.change_office_chief()
        DataBase.Data_Base.save()

    def clear_duty_office(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_duty_office()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_office_duty_office()
        DataBase.Data_Base.save()

    def add_unit(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_unit(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.unit
        DataBase.Data_Base.change_office_unit()
        DataBase.Data_Base.save()

    def change_unit(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_unit(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.unit
        DataBase.Data_Base.change_office_unit()
        DataBase.Data_Base.save()

    def clear_unit(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_unit()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_office_unit()
        DataBase.Data_Base.save()

    def clear_all_office(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_unit()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_office_unit()
        DataBase.Data_Base.clear_office_chief()
        DataBase.Data_Base.clear_office_duty_office()
        DataBase.Data_Base.save()

    # Зміни об'єктів класу Service

    def change_chief_service(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_chief(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.chief
        DataBase.Data_Base.change_service_chief()
        DataBase.Data_Base.save()

    def clear_chief_service(self,id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_chief()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_service_chief()
        DataBase.Data_Base.save()

    def add_tools_of_service(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.add_tools_of_service(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.tools_of_service
        DataBase.Data_Base.change_service_tools_of_service()
        DataBase.Data_Base.save()

    def change_tools_of_service(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_tools_of_service(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.tools_of_service
        DataBase.Data_Base.change_service_tools_of_service()
        DataBase.Data_Base.save()

    def clear_tools_of_service(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_tools_of_service()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_service_tools_of_service()
        DataBase.Data_Base.save()

    def change_area(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.change_area(new)
        DataBase.ID = o.ID
        DataBase.data_for_set = o.area
        DataBase.Data_Base.change_service_area()
        DataBase.Data_Base.save()

    def clear_area(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_area()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_service_area()
        DataBase.Data_Base.save()

    def clear_all_service(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.clear_all_service()
        DataBase.ID = o.ID
        DataBase.Data_Base.clear_service_area()
        DataBase.Data_Base.clear_service_chief()
        DataBase.Data_Base.clear_service_tools_of_service()
        DataBase.Data_Base.save()

    # Зміни об'єктів класу Fired

    def change_data_of_fired(self, id, new):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.data_of_zvilnennya = new
        DataBase.ID = o.ID
        DataBase.Data_Base.change_zvilneny_data_zvilnennya()
        DataBase.Data_Base.save()

    # Відображення даних

    def show_all_data(self):
        print("Загальна кількість робітників: {}".format(Worker.num_of_worker))
        print("Загальна таблиця усіх робітників")
        DataBase.Data_Base.show_data_main()
        print("Менеджери")
        DataBase.Data_Base.show_data_mng()
        print("Адміністратори")
        DataBase.Data_Base.show_data_adm()
        print("Офісні робітники")
        DataBase.Data_Base.show_data_office()
        print("HR")
        DataBase.Data_Base.show_data_hr()
        print("Землероби")
        DataBase.Data_Base.show_data_agr()
        print("Обслуговучий персонал")
        DataBase.Data_Base.show_data_service()
        print("Звільнені робітники")
        DataBase.Data_Base.show_data_fired()

    #Звільнити робітника
    def firing(self, id):
        True_id = int(id) - 1
        o = INandOUTput.main_list[True_id]
        o.zvilniti()
        DataBase.Data_Base.delete_main_info()
        DataBase.Data_Base.save()

    # Ввід-вивід

    def input_output(self):

        command = input()



        while command != "exit":
            try:
                if command == "add worker":
                    print("Введіть дані за порядком в один рядок через пробіл\n"
                    "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                    str = input()
                    self.add_new_worker(str)

                elif command == "add worker administrator":
                    print("Введіть дані за порядком в один рядок через пробіл\n"
                      "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                    str = input()
                    self.add_new_admistrator(str)

                elif command == "add worker agrarian":
                    print("Введіть дані за порядком в один рядок через пробіл\n"
                      "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                    str = input()
                    self.add_new_agrarian(str)

                elif command == "add worker hr":
                    print("Введіть дані за порядком в один рядок через пробіл\n"
                      "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                    str = input()
                    self.add_new_HR(str)

                elif command == "add worker manager":
                    print("Введіть дані за порядком в один рядок через пробіл\n"
                      "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                    str = input()
                    self.add_new_manager(str)

                elif command == "add worker office":
                   print("Введіть дані за порядком в один рядок через пробіл\n"
                      "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                   str = input()
                   self.add_new_office(str)

                elif command == "add worker service":
                   print("Введіть дані за порядком в один рядок через пробіл\n"
                         "Прізвище, Ім'я, По батькові, Стать, Ставка, Посада, Тип роботи, Наявність медичної страховки, Наясвність військового квитка")
                   str = input()
                   self.add_new_service(str)

                elif command == "change last":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нове прізвище")
                   mew = input()
                   self.change_last(id, mew)

                elif command == "change rate":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нову ставку")
                   mew = input()
                   self.change_rate(id, mew)

                elif command == "change type work":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть новий тип роботи")
                   mew = input()
                   self.change_type_work(id, mew)

                elif command == "change position":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нову посаду")
                   mew = input()
                   self.change_position(id, mew)

                elif command == "change military id":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть новий стан")
                   mew = input()
                   self.change_military_ID(id, mew)

                elif command == "change insurance":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть новий стан")
                   mew = input()
                   self.change_insurance(id, mew)

                elif command == "change chief for admin":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть новиго начальника")
                   mew = input()
                   self.change_chief_of_adm(id, mew)

                elif command == "сlear chief for admin":
                   print("Введіть ІD")
                   id = input()
                   self.clear_chief(id)

                elif command == "add duty for admin":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нові обов'язки")
                   mew = input()
                   self.add_duty_of_adm(id, mew)

                elif command == "change duty for admin":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нові обов'язки")
                   mew = input()
                   self.change_duty_of_adm(id, mew)

                elif command == "clear duty for admin":
                   print("Введіть ІD")
                   id = input()
                   self.clear_duty_of_adm(id)

                elif command == "add unit for monitoring":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нові підрозділи")
                   mew = input()
                   self.add_monitor_of_unit(id,mew)

                elif command == "change unit for monitoring":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть нові підрозділи")
                   mew = input()
                   self.change_monitor_of_unit(id, mew)

                elif command == "clear unit for monitoring":
                   print("Введіть ІD")
                   id = input()
                   self.clear_monitor_of_unit(id)

                elif command == "add helper":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть ПІП помічника")
                   mew = input()
                   self.add_helper(id, mew)

                elif command == "change helper":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть ПІП помічника")
                   mew = input()
                   self.change_helper(id, mew)

                elif command == "clear helper":
                   print("Введіть ІD")
                   id = input()
                   self.clear_helper(id)

                elif command == "add helper":
                   print("Введіть ІD")
                   id = input()
                   print("Введіть ПІП помічника")
                   mew = input()
                   self.add_helper(id, mew)

                elif command == "clear all for admin":
                    print("Введіть ІD")
                    id = input()
                    self.all_adm_clear(id)

                elif command == "add duty for agrarian":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові обов'язки")
                    mew = input()
                    self.add_duty_agrar(id, mew)

                elif command == "change duty for agrarian":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові обов'язки")
                    mew = input()
                    self.change_duty_agrar(id, mew)

                elif command == "clear duty for agrarian":
                    print("Введіть ІD")
                    id = input()
                    self.clear_duty_agrar(id)

                elif command == "add tool for agrarian":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові інструменти")
                    mew = input()
                    self.add_tools(id, mew)

                elif command == "change tool for agrarian":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові інструменти")
                    mew = input()
                    self.change_tools(id, mew)

                elif command == "clear tool for agrarian":
                    print("Введіть ІD")
                    id = input()
                    self.clear_tools(id)

                elif command == "change chief for agrarian":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нового чальника")
                    mew = input()
                    self.change_chief_of_agrar(id, mew)

                elif command == "clear chief for agrarian":
                    print("Введіть ІD")
                    id = input()
                    self.clear_chief_of_agrar(id)

                elif command == "clear all for agrarian":
                    print("Введіть ІD")
                    id = input()
                    self.clear_all_agrar(id)

                elif command == "add duty for hr":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові обов'язки")
                    mew = input()
                    self.add_duty_of_hr(id, mew)

                elif command == "change duty for hr":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові обов'язки")
                    mew = input()
                    self.change_duty_of_hr(id, mew)

                elif command == "clear duty for hr":
                    print("Введіть ІD")
                    id = input()
                    self.clear_duty_of_hr(id)

                elif command == "add for whom for hr":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть ПІП")
                    mew = input()
                    self.add_for_whom(id, mew)

                elif command == "change for whom for hr":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть ПІП")
                    mew = input()
                    self.change_for_whom(id, mew)

                elif command == "clear for whom for hr":
                    print("Введіть ІD")
                    id = input()
                    self.clear_for_whom(id)

                elif command == "add positions for hr":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть посади")
                    mew = input()
                    self.add_positions(id, mew)

                elif command == "change positions for hr":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть посади")
                    mew = input()
                    self.change_positions(id, mew)

                elif command == "clear positions for hr":
                    print("Введіть ІD")
                    id = input()
                    self.clear_positions(id)

                elif command == "clear all for hr":
                    print("Введіть ІD")
                    id = input()
                    self.clear_all_hr(id)

                elif command == "add subject":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть робітника")
                    mew = input()
                    self.add_subject(id, mew)

                elif command == "change subject":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть робітника")
                    mew = input()
                    self.change_subject(id, mew)

                elif command == "change subject":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть робітника")
                    mew = input()
                    self.change_subject(id, mew)

                elif command == "clear subject":
                    print("Введіть ІD")
                    id = input()
                    self.clear_subject(id)

                elif command == "add duty for manager":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть обов'язки")
                    mew = input()
                    self.add_duty_of_mng(id, mew)

                elif command == "change duty for manager":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть обов'язки")
                    mew = input()
                    self.change_duty_of_mng(id, mew)

                elif command == "clear duty for manager":
                    print("Введіть ІD")
                    id = input()
                    self.clear_duty_of_mng(id)

                elif command == "add duty for manager":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть обов'язки")
                    mew = input()
                    self.add_duty_of_mng(id, mew)

                elif command == "clear all for manager":
                    print("Введіть ІD")
                    id = input()
                    self.clear_all_mng(id)

                elif command == "change chief for office":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть ПІП начальника")
                    mew = input()
                    self.change_chief_office(id, mew)

                elif command == "clear chief for office":
                    print("Введіть ІD")
                    id = input()
                    self.clear_chief_office(id)

                elif command == "add duty for office":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові обов'язки")
                    mew = input()
                    self.add_duty_office(id, mew)

                elif command == "change duty for office":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нові обов'язки")
                    mew = input()
                    self.change_duty_office(id, mew)

                elif command == "clear duty for office":
                    print("Введіть ІD")
                    id = input()
                    self.clear_duty_office(id)

                elif command == "add unit for office":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть новий підрозділ")
                    mew = input()
                    self.add_unit(id, mew)

                elif command == "change unit for office":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть новий підрозділ")
                    mew = input()
                    self.change_unit(id, mew)

                elif command == "clear unit for office":
                    print("Введіть ІD")
                    id = input()
                    self.clear_unit(id)

                elif command == "clear all for office":
                    print("Введіть ІD")
                    id = input()
                    self.clear_all_office(id)


                elif command == "change chief for service":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нового начальника")
                    mew = input()
                    self.add_unit(id, mew)

                elif command == "clear chief for service":
                    print("Введіть ІD")
                    id = input()
                    self.clear_chief_service(id)

                elif command == "add tool for service":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть назву інструменту")
                    mew = input()
                    self.add_tools_of_service(id, mew)

                elif command == "change tool for service":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть назву інструменту")
                    mew = input()
                    self.change_tools_of_service(id, mew)

                elif command == "clear tool for service":
                    print("Введіть ІD")
                    id = input()
                    self.clear_tools_of_service(id)

                elif command == "change area":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть територію")
                    mew = input()
                    self.change_area(id, mew)

                elif command == "clear area":
                    print("Введіть ІD")
                    id = input()
                    self.clear_area(id)

                elif command == "clear all for service":
                    print("Введіть ІD")
                    id = input()
                    self.clear_all_service(id)

                elif command == "change data for fired":
                    print("Введіть ІD")
                    id = input()
                    print("Введіть нову дату")
                    mew = input()
                    self.change_data_of_fired(id, mew)

                elif command == "show all data":
                    self.show_all_data()

                elif command == "show worker":
                    DataBase.Data_Base.show_data_main()

                elif command == "show managers":
                    DataBase.Data_Base.show_data_mng()

                elif command == "show administrator":
                    DataBase.Data_Base.show_data_adm()

                elif command == "show agrarians":
                    DataBase.Data_Base.show_data_agr()

                elif command == "show office":
                    DataBase.Data_Base.show_data_office()

                elif command == "show fired":
                    DataBase.Data_Base.show_data_fired()

                elif command == "show service":
                    DataBase.Data_Base.show_data_service()

                elif command == "show hr":
                    DataBase.Data_Base.show_data_hr()

                elif command == "filter position":
                    DataBase.data_for_set = input()
                    DataBase.Data_Base.search_position()

                elif command == "filter military id":
                    DataBase.data_for_set = input()
                    DataBase.Data_Base.search_position()

                elif command == "filter id":
                    DataBase.data_for_set = input()
                    DataBase.Data_Base.search_id_global()

                elif command == "filter chief office":
                    DataBase.data_for_set = input()
                    DataBase.Data_Base.search_chief_office()

                elif command == "filter PIP":
                    DataBase.data_for_set = input()
                    DataBase.Data_Base.search_PIP()

                else:
                    print("Введіть існуючу команду")

            except:
                print("Помилка1")
            command = input()

InputAoutput = INandOUTput()


