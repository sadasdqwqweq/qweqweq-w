import sqlite3
from Workers.WorkerAndFired import Worker
con = sqlite3.connect("./Всі робітники.db")
cur = con.cursor()
data = Worker.main_data
fullname = "ЫФ фыв"
ID = 1
data_for_set = [fullname, ID]


class Main:
    con = sqlite3.connect("./Всі робітники.db")
    cur = con.cursor()

    def save(self):
        con.commit()

    def close_DB(self):
        cur.close()
        con.close()


    #Worker

    def add_main_info_in_main(self):
        cur.execute('INSERT INTO Всіробітники VALUES(?, ?, ?, ?, ?, ?, ?, ?)', data)

    def change_main_info_fullname(self):
        cur.execute('UPDATE Всіробітники SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate(self):
        cur.execute('UPDATE Всіробітники SET Ставка = ? WHERE ID = ?',data_for_set )

    def change_main_type_of_work(self):
        cur.execute('UPDATE Всіробітники SET Тип роботи = ? WHERE ID = ?',data_for_set)

    def change_main_info_position(self):
        cur.execute('UPDATE Всіробітники SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance(self):
        cur.execute('UPDATE Всіробітники SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID(self):
        cur.execute('UPDATE Всіробітники SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def delete_main_info(self):
        cur.execute('INSERT INTO Звільнені VALUES(?, ?, ?, ?, ?, ?, ?, ?)', data)
        cur.execute('Delete from Всіробітники WHERE ID = ?', ID)


    # Manager
    def change_main_info_fullname_mng(self):
        cur.execute('UPDATE Менеджери SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_mng(self):
        cur.execute('UPDATE Менеджери SET Ставка = ? WHERE ID = ?',data_for_set )

    def change_main_type_of_work_mng(self):
        cur.execute('UPDATE Менеджери SET Тип роботи = ? WHERE ID = ?',data_for_set)

    def change_main_info_position_mng(self):
        cur.execute('UPDATE Менеджери SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_mng(self):
        cur.execute('UPDATE Менеджери SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_mng(self):
        cur.execute('UPDATE Менеджери SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_manager(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Менеджери VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)', data)

    def change_magr_duty_of_mgr(self):
        cur.execute("UPDATE Менеджери SET Обов'язки = ? WHERE ID = ?",data_for_set )

    def change_mng_subkject(self):
        cur.execute('UPDATE Менеджери SET Піддані = ? WHERE ID = ?',data_for_set )

    def clear_mgr_duty(self):
        cur.execute("UPDATE Менеджери SET Обов'язки = NULL WHERE ID = ?", ID)

    def clear_mgr_subject(self):
        cur.execute('UPDATE Менеджери SET Піддані = NULL WHERE ID = ?', ID)


    #HR

    def change_main_info_fullname_hr(self):
        cur.execute('UPDATE HR SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_hr(self):
        cur.execute('UPDATE HR SET Ставка = ? WHERE ID = ?',data_for_set )

    def change_main_type_of_work_hr(self):
        cur.execute('UPDATE HR SET Тип роботи = ? WHERE ID = ?',data_for_set)

    def change_main_info_position_hr(self):
        cur.execute('UPDATE HR SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_hr(self):
        cur.execute('UPDATE HR SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_hr(self):
        cur.execute('UPDATE HR SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_hr(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO HR VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL )', data)

    def change_hr_positions(self):
        cur.execute('UPDATE HR SET Посади, на які опитує = ? WHERE ID = ?',data_for_set )

    def change_hr_for_whom(self):
        cur.execute('UPDATE HR SET Для яких менеджерів = ? WHERE ID = ?',data_for_set )

    def change_hr_duty_of_hr(self):
        cur.execute("UPDATE HR SET Обов'язки = ? WHERE ID = ?",data_for_set )

    def clear_hr_positions(self):
        cur.execute('UPDATE HR SET Посади, на які опитує = NULL WHERE ID = ?', ID)

    def clear_hr_for_whom(self):
        cur.execute('UPDATE HR SET Для яких менеджерів = NULL WHERE ID = ?', ID)

    def clear_hr_duty_of_hr(self):
        cur.execute("UPDATE HR SET Обов'язки = NULL WHERE ID = ?", ID)


    #Agrarian

    def change_main_info_fullname_agr(self):
        cur.execute('UPDATE Землероби SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_agr(self):
        cur.execute('UPDATE Землероби SET Ставка = ? WHERE ID = ?',data_for_set )

    def change_main_type_of_work_agr(self):
        cur.execute('UPDATE Землероби SET Тип роботи = ? WHERE ID = ?',data_for_set)

    def change_main_info_position_agr(self):
        cur.execute('UPDATE Землероби SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_agr(self):
        cur.execute('UPDATE Землероби SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_agr(self):
        cur.execute('UPDATE Землероби SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_agrararian(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Землероби VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)', data)

    def change_agr_chief(self):
        cur.execute('UPDATE Землероби SET Начальник = ? WHERE ID = ?',data_for_set )

    def change_agr_duty_agrar(self):
        cur.execute("UPDATE Землероби SET Обов'язки = ? WHERE ID = ?",data_for_set )

    def change_agr_tools(self):
        cur.execute('UPDATE Землероби SET Інструменти = ? WHERE ID = ?',data_for_set )

    def agr_clear_chief(self):
        cur.execute('UPDATE Землероби SET Начальник = ? WHERE ID = ?', ID)

    def agr_clear_duty_agrar(self):
        cur.execute("UPDATE Землероби SET Обов'язки = NULL WHERE ID = ?", ID)

    def agr_clear_tools(self):
        cur.execute('UPDATE Землероби SET Інструменти = NULL WHERE ID = ?', ID)


    #Office

    def change_main_info_fullname_office(self):
        cur.execute('UPDATE Офісніробітники SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_office(self):
        cur.execute('UPDATE Офісніробітники SET Ставка = ? WHERE ID = ?', data_for_set)

    def change_main_type_of_work_office(self):
        cur.execute('UPDATE Офісніробітники SET Тип роботи = ? WHERE ID = ?', data_for_set)

    def change_main_info_position_office(self):
        cur.execute('UPDATE Офісніробітники SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_office(self):
        cur.execute('UPDATE Офісніробітники SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_office(self):
        cur.execute('UPDATE Офісніробітники SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_office(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Офісніробітники VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)', data)

    def change_office_chief(self):
        cur.execute('UPDATE Офісніробітники SET Начальник = ? WHERE ID = ?',data_for_set )

    def clear_office_chief(self):
        cur.execute('UPDATE Офісніробітники SET Начальник = NULL WHERE ID = ?', ID)

    def change_office_duty_office(self):
        cur.execute("UPDATE Офісніробітники SET Обов'язки = ? WHERE ID = ?",data_for_set )

    def clear_office_duty_office(self):
        cur.execute("UPDATE Офісніробітники SET Обов'язки = NULL WHERE ID = ?", ID)

    def change_office_unit(self):
        cur.execute("UPDATE Офісніробітники SET Підрозділ = ? WHERE ID = ?",data_for_set )

    def clear_office_unit(self):
        cur.execute("UPDATE Офісніробітники SET Підрозділ = NULL WHERE ID = ?", ID)


    #Service

    def change_main_info_fullname_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Ставка = ? WHERE ID = ?', data_for_set)

    def change_main_type_of_work_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Тип роботи = ? WHERE ID = ?', data_for_set)

    def change_main_info_position_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_service(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Обслуговуючийперсонал VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)', data)

    def change_service_chief(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Начальник = ? WHERE ID = ?', data_for_set )

    def clear_service_chief(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Начальник = NULL WHERE ID = ?', ID)

    def change_service_tools_of_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Інструменти = ? WHERE ID = ?',data_for_set )

    def clear_service_tools_of_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Інструменти = NULL WHERE ID = ?', ID)

    def change_service_area(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Територія = ? WHERE ID = ?',data_for_set )

    def clear_service_area(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Територія = NULL WHERE ID = ?', ID)


    #Administration

    def change_main_info_fullname_adm(self):
        cur.execute('UPDATE Адміністрація SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_adm(self):
        cur.execute('UPDATE Адміністрація SET Ставка = ? WHERE ID = ?', data_for_set)

    def change_main_type_of_work_adm(self):
        cur.execute('UPDATE Адміністрація SET Тип роботи = ? WHERE ID = ?', data_for_set)

    def change_main_info_position_adm(self):
        cur.execute('UPDATE Адміністрація SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_adm(self):
        cur.execute('UPDATE Адміністрація SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_adm(self):
        cur.execute('UPDATE Адміністрація SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_administation(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Адміністрація VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL)', data)

    def change_administation_chief(self):
        cur.execute('UPDATE Адміністрація SET Начальник = ? WHERE ID = ?',data_for_set )

    def clear_administation_chief(self):
        cur.execute('UPDATE Адміністрація SET Начальник = NULL WHERE ID = ?', ID)

    def change_administation_duty_of_adm(self):
        cur.execute("UPDATE Адміністрація SET Обов'язки = ? WHERE ID = ?",data_for_set )

    def clear_administation_duty_of_adm(self):
        cur.execute("UPDATE Адміністрація SET Обов'язки = NULL WHERE ID = ?", ID)

    def change_administation_monitor_of_unit(self):
        cur.execute('UPDATE Адміністрація SET Відповідальний за підрозділ = ? WHERE ID = ?', data_for_set )

    def clear_administation_monitor_of_unit(self):
        cur.execute('UPDATE Адміністрація SET Відповідальний за підрозділ = NULL WHERE ID = ?', ID)

    def change_administation_helper(self):
        cur.execute('UPDATE Адміністрація SET Помічник = ? WHERE ID = ?',data_for_set )

    def clear_administation_helper(self):
        cur.execute('UPDATE Адміністрація SET Помічник = NULL WHERE ID = ?', ID)


    #Zvilneny

    def change_main_info_fullname_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET ПІП= ? WHERE ID = ?', data_for_set)

    def change_main_info_rate_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Ставка = ? WHERE ID = ?', data_for_set)

    def change_main_type_of_work_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Тип роботи = ? WHERE ID = ?', data_for_set)

    def change_main_info_position_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Посада = ? WHERE ID = ?', data_for_set)

    def change_main_info_insurance_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Медична страховка = ? WHERE ID = ?', data_for_set)

    def change_main_info_military_ID_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Військовий квиток = ? WHERE ID = ?', data_for_set)

    def add_main_info_in_zvilneny(self):
        self.delete_main_info()
        cur.execute('INSERT INTO Звільнені VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL)', data)

    def change_zvilneny_data_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Дата звільнення = ? )',data_for_set )

    def clear_zvilneny_data_zvilnennya(self):
        cur.execute('UPDATE Звільнені SET Дата звільнення = NULL )',data_for_set )

    #Відображення даних

    def show_data_main(self):
        cur.execute("SELECT * FROM Всіробітники")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7]))

    def show_data_adm(self):
        cur.execute("SELECT * FROM Адміністрація")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tВідповідальний за підрозділ\t\tПомічник\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

    def show_data_agr(self):
        cur.execute("SELECT * FROM Землероби")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tІнструменти\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_hr(self):
        cur.execute("SELECT * FROM HR")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Посади, на які опитує\t\tДля яких менеджерів\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_mng(self):
        cur.execute("SELECT * FROM Менеджери")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Піддані\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    def show_data_office(self):
        cur.execute("SELECT * FROM Офісніробітники")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tПідрозділ\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_service(self):
        cur.execute("SELECT * FROM Обслуговуючийперсонал")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tІнструменти\t\tТериторія")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_fired(self):
        cur.execute("SELECT * FROM Звільнені")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Дата звільнення")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8]))

    #Фільтри пошуку

    def search_position(self):
        cur.execute("SELECT * FROM Всіробітники WHERE Посада = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

    def search_PIP(self):
        cur.execute("SELECT * FROM Всіробітники WHERE ПІП = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

    def search_id_global(self):
        cur.execute("SELECT * FROM Всіробітники WHERE ID = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

    def search_chief_office(self):
        cur.execute("SELECT * FROM Офісніробітники WHERE Начальник = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tПідрозділ\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def search_military_id(self):
        cur.execute("SELECT * FROM Всіробітники WHERE Військовий квиток = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tТип роботи\t\tПосада\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2],row[3], row[4], row[5],row[6], row[7]))


Data_Base = Main()

