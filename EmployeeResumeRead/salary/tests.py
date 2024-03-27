from django.test import TestCase
import os
import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.datastructures import MultiValueDict

class TestProcessSalarySlip(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = "/process/"

        return super().setUpClass()
    def test_twofiles(self):
        infosys = open(os.path.join("test_data","infosys.pdf"),"rb")
        infosys_data = open(os.path.join("test_data","infosys.pdf"),"rb").read()
       
        pdf_file = InMemoryUploadedFile(file=infosys, 
                                        field_name="pdf_file",
                                        name="infosys.pdf", 
                                        content_type="application/pdf",
                                        size=len(infosys_data),
                                        charset="utf-8", )
        data = MultiValueDict({"pdf_file": [pdf_file]})
        resp = self.client.post(self.url, data, format='multipart')
        df = pd.read_excel(resp.content)
        self.assertTrue('38,879.00', df.Salary.values[0] ) 
        self.assertTrue('Ashok Mallappa', df.Employee_name.values[0] ) 
        # import pdb; pdb.set_trace()
    
        

     




