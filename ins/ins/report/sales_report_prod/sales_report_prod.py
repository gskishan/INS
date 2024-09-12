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
    cond = ""

    if customer:
        cond += "AND l.og_name = '{0}' ".format(customer)
    if from_date and to_date:
        cond += "AND l.enquiry_date BETWEEN '{0}' AND '{1}' ".format(from_date, to_date)

    query = """
    SELECT * FROM (
        -- Lead, Enquiry, and Quotation linked data
        SELECT
            l.og_name AS customer,
            l.place,
            l.vertical,
            l.name AS lead_id,
            e.name AS enquiry_id,
            q.name AS quotation_id,
            qi.item_code AS item_code,
            qi.item_name AS item,
            qi.item_group AS item_group,
            qi.qty AS qty,
            qi.rate AS rate,
            qi.amount AS amount,
            q.probability AS probability,
            l.expected_order_date,
            q.status AS status,
            q.amended_from
        FROM
            `tabLead` l
        LEFT JOIN
            `tabEnquiry` e ON l.name = e.lead
        LEFT JOIN
            `tabQuotation` q ON e.name = q.enquiry AND q.status != 'Cancelled'
        LEFT JOIN
            `tabQuotation Item` qi ON q.name = qi.parent
        WHERE
            l.name IS NOT NULL
            {0}

        UNION ALL

        -- Leads without Quotation
        SELECT
            l.og_name AS customer,
            l.place,
            l.vertical,
            l.name AS lead_id,
            e.name AS enquiry_id,
            NULL AS quotation_id,
            ei.item_code AS item_code,
            ei.item_name AS item,
            ei.item_group AS item_group,
            ei.qty AS qty,
            NULL AS rate,
            NULL AS amount,
            e.probability AS probability,
            l.expected_order_date,
            CASE
                WHEN e.enquiry_status IS NOT NULL THEN e.enquiry_status
                ELSE
                    CASE
                        WHEN e.docstatus = 2 THEN 'Cancelled'
                        WHEN e.docstatus = 0 THEN 'Draft'
                        WHEN e.docstatus = 1 THEN 'Submitted'
                    END
            END AS status,
            NULL AS amended_from
        FROM
            `tabLead` l
        LEFT JOIN
            `tabEnquiry` e ON l.name = e.lead
        LEFT JOIN
            `tabEnquiry Item` ei ON e.name = ei.parent
        LEFT JOIN
            `tabQuotation` q ON e.name = q.enquiry
        WHERE
            q.name IS NULL
            {0}
    ) AS data
    """.format(cond)

    # Execute the query with the given filters
    data = frappe.db.sql(query, as_dict=True)
    frappe.errprint(query)

    return data
