import frappe
import json

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)


def execute():
    my_data = js_r("/home/gtk/Desktop/gtk/july-14-bench/apps/ins/ins/lead13.json")
    count = 0
    # my_data = [my_data[0]]
    for each_row in my_data:
        # create a new document
        try:
            single_note = each_row["notes"]
            each_row.pop("notes", None)
            if not each_row["email"]:
                each_row.pop("email",None)
            doc = frappe.get_doc(each_row)
            # print(each_row["name"], doc.name , "\n")
            if single_note:
                print("Note")
                doc.append("notes",{ "note":single_note})

            doc.db_insert()
            
            # new_address_doc = frappe.new_doc("Address")
            # new_address_doc.address_line1 = each_row["address_line1"]
            
            # new_address_doc.address_line2 = each_row["address_line2"]
            # new_address_doc.address_title = each_row["address_title"]
            # new_address_doc.city = each_row["city"]
            # new_address_doc.province = ''
            # new_address_doc.pincode = each_row["pincode"]
            # new_address_doc.country = each_row["country"]
            
            # new_address_doc.append("links", {"link_doctype": "Lead", "link_name": doc.name})
            # new_address_doc.address_type = each_row["address_type"]
            # new_address_doc.insert(ignore_mandatory=True)
            
            
            # contact = frappe.new_doc("Contact")
            # contact.update(
            #     {
            #         "first_name": each_row["lead_name"],
            #         "salutation": each_row["salutation"],
            #         "gender": each_row["gender"],
            #         "designation": each_row["designation"],
            #         "company_name": each_row["company_name"],
            #         "image": each_row["image"],
            #         "department":each_row["department"]
            #     }
            # )
            # if "email" in each_row: 
            #     contact.append("email_ids", {"email_id": each_row["email"], "is_primary": 0})
            # contact.append("phone_nos", {"phone": each_row["phone"], "is_primary_phone": 1})
            # contact.append("phone_nos", {"phone": each_row["mobile_no"], "is_primary_mobile_no": 1})
            
            # contact.append("links", dict(link_doctype="Lead", link_name=doc.name))
            
            # contact.insert(ignore_permissions=True, ignore_mandatory=True, ignore_links=True )
            # contact.reload()  # load changes by hooks on contact
            print(count, each_row['name'])
            count += 1
        except Exception as e:
            print(json.dumps(each_row, indent=4), e,'\n\n\n\n')

        
    # frappe.db.commit()
        
    