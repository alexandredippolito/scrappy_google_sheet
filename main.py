import gspread
from indeed import search_indeed
from save import save_to_csv
from googlesheet import sheet


search = 'python'

result_indeed = search_indeed(search)
sheet(result_indeed)
# sheet()
# save_to_csv(result_indeed)


