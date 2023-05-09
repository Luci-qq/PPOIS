from Model import Model
from View import MainApp

mod = Model("E:\\universityProgs\\Lab2\\data.xml")
mod.make_records_for_table()
_table_records = mod.get_records_for_table()

main = MainApp(_table_records)
main.run()
