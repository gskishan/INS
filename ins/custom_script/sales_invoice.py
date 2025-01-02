from frappe import utils
import re
import frappe
from erpnext.accounts.utils import get_fiscal_year

@frappe.whitelist()
def update_oldrecord():
    sql="""SELECT 
  name,
    company,
    YEAR(posting_date) AS invoice_year,
    ROW_NUMBER() OVER (PARTITION BY company, YEAR(posting_date) ORDER BY creation) AS order_number
FROM 
    `tabSales Invoice`
ORDER BY 
    company, creation;"""
    for d in frappe.db.sql(sql,as_dict=True):
        si=frappe.get_doc("Sales Invoice",d.name)
        si.db_set("sequence",0)

def get_year(posting_date):
    import datetime
    date_string = str(posting_date)
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    year = date_object.year
    return year

def validate(self, method=None):
    if self.is_new() and 'param' in self.naming_series:
        try:
            fiscal_year_data = get_fiscal_year(date=self.posting_date)
            fiscal_start = fiscal_year_data[1]  
            fiscal_end = fiscal_year_data[2] 
            
            sql = """
                SELECT MAX(sequence) 
                FROM `tabSales Invoice`
                WHERE company=%s AND sequence IS NOT NULL 
                AND posting_date BETWEEN %s AND %s
            """
            last_count = frappe.db.sql(sql, (self.company, fiscal_start, fiscal_end), as_dict=False)

            last_count = last_count[0][0] if last_count else None
            self.sequence = last_count + 1 if last_count else 1	
        except Exception as e:
            frappe.log_error(f"Error setting sequence: {str(e)}")
    elif self.is_new():
        self.sequence = 0


    

def autoname(doc, method=None):
    set_name(doc)

def set_name(doc):
    if 'param' in doc.naming_series:
        fiscal_year_data = get_fiscal_year(date=doc.posting_date)
        fiscal_start = fiscal_year_data[1]  
        fiscal_end = fiscal_year_data[2]

        month = re.findall(r'\d+', utils.today())[1]
        vertical = doc.vertical
        doc_type = doc.type
        
        company_codes = {
            "insmart Systems": "10000",
            "insmart Systems India Private Limited": "20000",
            "OIA TECHNOLOGIES PRIVATE LIMITED": "30000"
        }
        company_code = company_codes.get(doc.company, "00000")

        sql = """
            SELECT MAX(sequence)
            FROM `tab{0}`
            WHERE company=%s AND sequence IS NOT NULL 
            AND posting_date BETWEEN %s AND %s
        """.format(doc.doctype)
        
        max_sequence = frappe.db.sql(sql, (doc.company, fiscal_start, fiscal_end), as_dict=False)
        max_sequence = max_sequence[0][0] if max_sequence else None
        sequence = max_sequence + 1 if max_sequence else 1

        last_number = int(company_code) + sequence
        fiscal_year = fiscal_year_data[0].replace('-', '')

        doc.name = f"{fiscal_year}{doc_type}{month}{vertical}{last_number}"
