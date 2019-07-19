import xlrd 


 
loc = ("notlar.xlsx") 
loc2 = ("notlar2.xlsx") 
  
wb = xlrd.open_workbook(loc) 
wb2 = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
  
# For row 0 and column 0 
sheet.cell_value(2,1) 

print(sheet.cell_value(2,1))


    
    
