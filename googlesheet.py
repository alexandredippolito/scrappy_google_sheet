import gspread

def sheet(jobs):
  # linked credentials
  gc = gspread.service_account(filename="credentials.json")
  #linked keys
  sh = gc.open_by_key('1Il86V5q7XPbP-ym53cjhoYQ8tbfbpfcCvERZVvVn5LA')
  worksheet = sh.sheet1
  for job in jobs:
    worksheet.append_row(list(job.values()))
