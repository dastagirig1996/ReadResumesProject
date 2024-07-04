# from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
# from .pdfread import extract_pdf_data, extract_text_from_docx
# import re
# import asyncio
# import pandas as pd
# import os

# def NameFile(file):
#     name_match = re.search(r'_(.*?)\[\d+y_\d+m\]', file)
#     if name_match:
#         return name_match.group(1)
#     else:
#         return file

# def ExperienceFile(file):
#     exp_match = re.search(r'\d+y_\d+m', file)
#     if exp_match:
#         return exp_match.group(0)
#     else:
#         return None

# duplicates_count = 0
# def findunique(ls, op, file, folder_name):
#     global duplicates_count
#     items = list(op[0].items())
#     items.insert(0, ("NamefromFile", NameFile(file)))
#     items.insert(7, ("Exp_File", ExperienceFile(file)))
#     items.insert(8, ("FolderName", folder_name))  # Add Folder Name
#     op[0] = dict(items)
#     if ls is not None:
#         for i in ls:
#             if i['Email_id'] == op[0]['Email_id']:
#                 duplicates_count += 1
#                 return []
#     return op

# async def process_file(uploaded_file, data, dfs, folder_name):
#     fileName = uploaded_file.name
#     if fileName.endswith(".pdf"):
#         op = await extract_pdf_data(uploaded_file)
#         data.extend(findunique(data, op, fileName, folder_name))

#     elif fileName.endswith(".docx"):
#         op = await extract_text_from_docx(uploaded_file)
#         data.extend(findunique(data, op, fileName, folder_name))

#     elif fileName.endswith(".xlsx"):
#         df = await read_excel(uploaded_file)
#         dfs.append(df)

# async def read_excel(file):
#     loop = asyncio.get_event_loop()
#     return await loop.run_in_executor(None, pd.read_excel, file)

# # @timecalculator
# async def process_salary(request):
#     if request.method == 'POST':
#         uploaded_files = request.FILES.getlist('files')
#         folder_name = request.POST.get('folderName', 'default_folder')
        
#         if not uploaded_files:
#             return HttpResponse("Please choose at least one file......!!")
        
#         data = []
#         dfs = []
#         tasks = []

#         for uploaded_file in uploaded_files:
#             tasks.append(process_file(uploaded_file, data, dfs, folder_name))

#         await asyncio.gather(*tasks)

#         excel_file = 'empty.xlsx'
#         try:
#             if data:
#                 df = pd.DataFrame(data)
#                 excel_file = f'{folder_name}_employee_resumes_data.xlsx'
#                 df.to_excel(excel_file, index=False)
#             elif dfs:
#                 merged_df = pd.concat(dfs, ignore_index=True)
#                 merged_df = merged_df.drop_duplicates(subset=['Email_id'])
#                 excel_file = f'{folder_name}_merged_excels.xlsx'
#                 merged_df.to_excel(excel_file, index=False)
#             with open(excel_file, 'rb') as fh:
#                 response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#                 response['Content-Disposition'] = f'inline; filename={excel_file}'
#                 global duplicates_count
#                 print('duplicates', duplicates_count)
#                 duplicates_count = 0
#                 return response
#         except FileNotFoundError:
#             return HttpResponse("Please choose at least one file......!!")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#     return render(request, 'temp2.html')



from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .pdfread import extract_pdf_data, extract_text_from_docx
import re
import asyncio
import pandas as pd
import os

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

def findunique(ls, op, file, folder_name):
    global duplicates_count
    items = list(op[0].items())
    items.insert(0, ("NamefromFile", NameFile(file)))
    items.insert(7, ("Exp_File", ExperienceFile(file)))
    items.insert(8, ("FolderName", folder_name))  # Add Folder Name
    op[0] = dict(items)
    if ls is not None:
        for i in ls:
            if i['Email_id'] == op[0]['Email_id']:
                duplicates_count += 1
                return []
    return op

# async def process_file(uploaded_file, data, dfs, folder_name):
#     fileName = uploaded_file.name
#     if fileName.endswith(".pdf"):
#         op = await extract_pdf_data(uploaded_file)
#         data.extend(findunique(data, op, fileName, folder_name))

#     elif fileName.endswith(".docx") or fileName.endswith(".doc"):
#         op = await extract_text_from_docx(uploaded_file)
#         data.extend(findunique(data, op, fileName, folder_name))

#     elif fileName.endswith(".xlsx"):
#         df = await read_excel(uploaded_file)
#         dfs.append(df)

from zipfile import BadZipFile

async def process_file(uploaded_file, data, dfs, folder_name):
    fileName = uploaded_file.name
    try:
        if fileName.endswith(".pdf"):
            op = await extract_pdf_data(uploaded_file)
            data.extend(findunique(data, op, fileName, folder_name))

        elif fileName.endswith(".docx") or fileName.endswith(".doc"):
            op = await extract_text_from_docx(uploaded_file)
            data.extend(findunique(data, op, fileName, folder_name))

        elif fileName.endswith(".xlsx"):
            df = await read_excel(uploaded_file)
            dfs.append(df)
        else:
            print(f"Unsupported file format: {fileName}")

    except BadZipFile as e:
        print(f"BadZipFile error for file '{fileName}': {str(e)}")
        # Handle the error or log it as per your application's requirements
    except Exception as e:
        print(f"Error processing file '{fileName}': {str(e)}")
        # Handle the error or log it as per your application's requirements


async def read_excel(file):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, pd.read_excel, file)

# @timecalculator
async def process_salary(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        folder_name = request.POST.get('folderName', 'default_folder')
        
        if not uploaded_files:
            return HttpResponse("Please choose at least one file......!!")
        
        data = []
        dfs = []
        tasks = []

        for uploaded_file in uploaded_files:
            tasks.append(process_file(uploaded_file, data, dfs, folder_name))

        await asyncio.gather(*tasks)

        excel_file = 'empty.xlsx'
        try:
            if data:
                df = pd.DataFrame(data)
                excel_file = f'{folder_name}_employee_resumes_data.xlsx'
                df.to_excel(excel_file, index=False)
            elif dfs:
                merged_df = pd.concat(dfs, ignore_index=True)
                merged_df = merged_df.drop_duplicates(subset=['Email_id'])
                excel_file = f'{folder_name}_merged_excels.xlsx'
                merged_df.to_excel(excel_file, index=False)
            with open(excel_file, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = f'inline; filename={excel_file}'
                global duplicates_count
                print('duplicates', duplicates_count)
                duplicates_count = 0
                return response
        except FileNotFoundError:
            return HttpResponse("Please choose at least one file......!!")
        except Exception as e:
            print(f"An error occurred: {e}")
    return render(request, 'temp2.html')




















