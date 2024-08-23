# Copyright (c) 2024, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)

	return columns, data



def get_columns(filters= None):
	return [
		{
			"label": _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Place"),
			"fieldname": "place",
			"fieldtype": "Data",
			"width": 70,
		},
		{
			"label": _("Vertical"),
			"fieldname": "vertical",
			"fieldtype": "Data",
			"width": 80,
		},
		{
			"label": _("Lead ID"),
			"fieldname": "lead_id",
			"fieldtype": "Link",
			"options": "Lead",
			"width": 200,
		},
		{
			"label": _("Enquiry ID"),
			"fieldname": "enquiry_id",
			"fieldtype": "Link",
			"options": "Enquiry",
			"width": 200,
		},
		{
			"label": _("Quotation ID"),
			"fieldname": "quotation_id",
			"fieldtype": "Link",
			"options": "Quotation",
			"width": 200,
		},
		{
			"label": _("Item Code"),
			"fieldname": "item_code",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": _("Item Name"),
			"fieldname": "item",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Item Group"),
			"fieldname": "item_group",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Qty"),
			"fieldname": "qty",
			"fieldtype": "Data",
			"width": 70,
		},
		{
			"label": _("Rate"),
			"fieldname": "rate",
			"fieldtype": "Data",
			"width": 80,
		},
		{
			"label": _("Amount"),
			"fieldname": "amount",
			"fieldtype": "Currency",
			"width": 80,
		},
		{
            "label": _("Probability"),
            "fieldname": "probability",
            "fieldtype": "Data",
            "width": 100,
        },
		{
			"label": _("Expected Order Date"),
			"fieldname": "expected_order_date",
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 100,
		}
	]


def get_data(filters=None):
    customer = filters.customer
    from_date = filters.from_date
    to_date = filters.to_date

    query = """
        SELECT
            l.og_name AS customer,
            l.place,
            l.vertical,
            l.name AS lead_id,
            e.name AS enquiry_id,
            q.name AS quotation_id,
	    ei.item_code AS item_code,
            ei.item_name AS item,
            ei.item_group AS item_group,
            ei.qty AS qty,
            ei.rate AS rate,
            ei.amount AS amount,
            COALESCE(q.probability, e.probability, l.probability) AS probability,
            l.expected_order_date,
            CASE
		    WHEN e.docstatus = 2 THEN 'Cancelled'
		    ELSE COALESCE(q.status, e.enquiry_status, l.status)
		END AS status
        FROM
            `tabLead` l
        LEFT JOIN
            `tabEnquiry` e ON l.name = e.lead
        LEFT JOIN
            `tabEnquiry Item` ei ON e.name = ei.parent
        LEFT JOIN
            `tabQuotation` q ON e.name = q.enquiry
        LEFT JOIN
            `tabQuotation Item` qi ON q.name = qi.parent
        WHERE
            1=1
    """

    if customer:
        query += " AND l.og_name = %(customer)s"
    if from_date and to_date:
        query += " AND l.enquiry_date BETWEEN %(from_date)s AND %(to_date)s"

    query += "    GROUP BY ei.item_code ORDER BY l.name, e.name, q.name"
	

    data = frappe.db.sql(query, {
        'customer': customer,
        'from_date': from_date,
        'to_date': to_date,
    }, as_dict=True)
    frappe.errprint(query)

    # total_amount = sum(row['amount'] for row in data)
    
    # # Add a row for total amount at the end of the data
    # if data:
    #     data.append({
    #         'customer': "Total Amount",
    #         'amount': total_amount
    #     })
    
    return data
