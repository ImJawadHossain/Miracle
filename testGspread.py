import gspread
from oauth2client.service_account import ServiceAccountCredentials
emails = "themillibit@gmail.com"
names = "the Millibit"
scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# for open a spreadSheet
spreadsheet = client.open("SeleniumSpreadsheets")

# for open a worksheet
worksheet = spreadsheet.worksheet("JawadSheets")

# # for add a new worksheet
# worksheet1 = spreadsheet.add_worksheet(title="newWorksheets", rows="100", cols="20")
#
# # for get a cell value
# value = worksheet.acell('A1').value
# print(value)
#
# # for see worksheet list
# worksheet_list = spreadsheet.worksheets()
# print(worksheet_list)

# # for get cell formula
# get_cell_formula = worksheet.acell('B1', value_render_option='FORMULA').value
# print(get_cell_formula)

# # for get all value in a raw as a list
# row_values_list = worksheet.row_values(1)
# print(values_list)

# # for get all value in a column
# col_value_list = worksheet.col_values(1)
# print(col_value_list)

# # for get all value in a worksheet
# worksheet_all_data = worksheet.get_all_values() # or for get as a dictonary use 'get_all_records()' method
# print(worksheet_all_data)

# # for find something in a worksheet
# cell = worksheet.find("testing")
# print((cell.row, cell.col))

# # update a cell
# worksheet.update('B1', 'Bingo!')


# # for change bg color or font color or font size etc.
# worksheet.format("A1:C1", {
#     "backgroundColor": {
#       "red": 0.0,
#       "green": 0.0,
#       "blue": 0.0
#     },
#     "horizontalAlignment": "CENTER",
#     "textFormat": {
#       "foregroundColor": {
#         "red": 1.0,
#         "green": 1.0,
#         "blue": 1.0
#       },
#       "fontSize": 12,
#       "bold": True
#     }
# })
