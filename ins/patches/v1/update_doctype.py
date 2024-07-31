import frappe

def execute():
    # frappe.reload_doc("ins", "doctype", "Enquiry")
    old_lead = frappe.get_doc("DocType", "Lead")
    print(old_lead.as_dict(), "Before Relaoding \n\n\n\n\n")
    frappe.reload_doc("CRM", "doctype", "Lead")
    new_lead = frappe.get_doc("DocType", "Lead")
    print(new_lead.as_dict(), "After Reloading")
