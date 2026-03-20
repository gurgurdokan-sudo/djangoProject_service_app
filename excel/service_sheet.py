from openpyxl import load_workbook

def create_service_sheet(user, year, month):
    wb = load_workbook('templatesExcel/service_template.xlsx')
    wb.name = user.name
    ws = wb.active
    siyaku_number = '112300' #一旦新座市固定
    for i,d in enumerate(siyaku_number):
        cell = f'{chr(ord('K')+i)}5'
        ws[cell] = d
    ws['V5'] = '新座市' #一旦新座市固定
    ws['Aj5'] = '' #介護事業所
    ws['Aj6'] = '' #介護事業担当者
    ws['AX7'] = f"{year}年{month}月"

    insured_number = str(user.insured_number) #被保険者番号
    for i,d in enumerate(insured_number):
        cell = f"{chr(ord('G')+i)}7"
        ws[cell] = d
    ws['V7'] = user.name_kana
    ws['V8'] = user.name
    ws['W9'] = user.care_level
    ws['W11'] = '' #変更後
    ws['W12'] = '' 
    ws['AI9'] = user.max_separate_payment()
    return wb
