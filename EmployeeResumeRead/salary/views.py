 
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .pdfread import extract_pdf_data, extract_text_from_docx
import re
import asyncio
import pandas as pd



def NameFile(file):
    name_match = re.search(r'_(.*?)\[\d+y_\d+m\]', file)
    if name_match:
        return name_match.group(1)
    else:
        return file
    
def ExperienceFile(file):
    exp_match = re.search(r'\d+y_\d+m', file)
    if exp_match:
        return exp_match.group(0)
    else:
         return None
duplicates_count = 0
def findunique(ls,op,file):
    global duplicates_count
    # import pdb; pdb.set_trace()
    # order_dic = OrderedDict({"NamefromFile":NameFile(file)})
    # order_dic.update(op[0])
    # regular_dic = dict(order_dic)
    # op[0] = regular_dic
    items = list(op[0].items())
    items.insert(0,("NamefromFile",NameFile(file)))
    items.insert(7,("Exp_File",ExperienceFile(file)))
    # op[0].setdefault("Exp_File",ExperienceFile(file))
    op[0] = dict(items)
    if ls is not None:
        for i in ls:
            if i['Email_id'] == op[0]['Email_id']:
               duplicates_count +=1
               return []
    return op

async def process_file(uploaded_file, data, dfs):
    fileName = uploaded_file.name
    if fileName.endswith(".pdf"):
        op = await extract_pdf_data(uploaded_file)
        data.extend(findunique(data, op, fileName))

    elif fileName.endswith(".docx"):
        op = await extract_text_from_docx(uploaded_file)
        data.extend(findunique(data, op, fileName))

    elif fileName.endswith(".xlsx"):
        df = await read_excel(uploaded_file)
        dfs.append(df)

async def read_excel(file):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, pd.read_excel, file)


# @timecalculator
async def process_salary(request):
    if request.method == 'POST':
        uploaded_files =  request.FILES.getlist('files')
        data = []
        dfs = []
        tasks = []
        count = 1

        for uploaded_file in uploaded_files:
            count += 1
            tasks.append(process_file(uploaded_file, data, dfs))

        await asyncio.gather(*tasks)
        excel_file = 'empty.xlsx'
        try:
            if data:
                df = pd.DataFrame(data)
                excel_file = 'employee_resumes_data.xlsx'
                df.to_excel(excel_file,index=False)
            elif dfs:
                merged_df = pd.concat(dfs,ignore_index=True)
                merged_df = merged_df.drop_duplicates(subset = ['Email_id'])
                excel_file = 'merged_excels.xlsx'
                merged_df.to_excel(excel_file,index=False)
            with open(excel_file,'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename='+excel_file
                global duplicates_count
                print('duplicates',duplicates_count)
                duplicates_count = 0
                return response   
        except FileNotFoundError as fe:
            return HttpResponse("Please choose atleast one file......!!")
        except Exception as e:
            print(f"An error occurred: {e}")
    return render(request, 'temp2.html')
 