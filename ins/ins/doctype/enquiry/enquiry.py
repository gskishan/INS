# Copyright (c) 2024, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Enquiry(Document):
    
    @frappe.whitelist()
    def update_data(self):
        for d in get_data():
            if frappe.db.exists("Enquiry", d.get("name")):
                doc=frappe.get_doc("Enquiry",d.get("name"))
                doc.db_set("docstatus",d.get("docstatus"))


def get_data():
    return [
    {
  "name": "ENQUIRY-00002",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00004",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00005",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00006",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00007",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00008",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00010",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00011",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00012",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00013",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00014",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00018",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00019",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00020",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00021",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00022",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00023",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00024",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00025",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00026",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00028",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00029",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00030",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00031",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00032",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00033",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00034",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00035",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00036",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00037",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00037-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-00037"
 },
 {
  "name": "ENQUIRY-00038",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00039",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00040",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00041",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00042",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00043",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00045",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00046",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00047",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00048",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00049",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00050",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00051",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00052",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00053",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00054",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00055",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00056",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00056-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-00056"
 },
 {
  "name": "ENQUIRY-00057",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00058",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00059",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00060",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00061",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00062",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00063",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00064",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00065",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00066",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00067",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00068",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00069",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00070",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00071",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00072",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00073",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00074",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00075",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00076",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00076-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-00076"
 },
 {
  "name": "ENQUIRY-00077",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00078",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00079",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00079-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-00079"
 },
 {
  "name": "ENQUIRY-00080",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00081",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00082",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00083",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00084",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00085",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00086",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00087",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00088",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00089",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00090",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00091",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00092",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00093",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00094",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00095",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00096",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00097",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00098",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00099",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00099-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-00099"
 },
 {
  "name": "ENQUIRY-00100",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00101",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00102",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00103",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00104",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00105",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00106",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00107",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00108",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00109",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00110",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00111",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00112",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00113",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00114",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00115",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00116",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00118",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00119",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00120",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00121",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00122",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00123",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00124",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00125",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00126",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00127",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00128",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00129",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00130",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00131",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00132",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00133",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00134",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00135",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00136",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00137",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00138",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00139",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00140",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00141",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00142",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00143",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00144",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00145",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00146",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00147",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00148",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00149",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00150",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00151",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00152",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00153",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00154",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00155",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00156",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00157",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00158",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00159",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00160",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00161",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00162",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00163",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00164",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00165",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00166",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00167",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00168",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00169",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00170",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00171",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00172",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00173",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00174",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00175",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00176",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00177",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00178",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00179",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00180",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00181",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00182",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00183",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00184",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00185",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00186",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00187",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00188",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00189",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00190",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00191",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00192",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00193",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00194",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00195",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00196",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00197",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00198",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00199",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00200",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00201",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00202",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00203",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00204",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00205",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00206",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00207",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00208",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00209",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-00211",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00212",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00213",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00214",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-00214-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-00214"
 },
 {
  "name": "ENQUIRY-00215",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00216",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00217",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00218",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00219",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00220",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00221",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00222",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00223",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00224",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00225",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00226",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-00227",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00001",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00002",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00003",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00004",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00005",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00006",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00007",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00008",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00009",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00010",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00011",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00012",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00013",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00014",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00015",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00016",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00017",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00018",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00020",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00021",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-02-00022",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00023",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00024",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00025",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00026",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00027",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00028",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00029",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00030",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00031",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00032",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00033",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00034",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00035",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00036",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00037",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00038",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00039",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00040",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00041",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00042",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00043",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00044",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00045",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00046",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00047",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00048",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00049",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00050",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00051",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00051-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00051"
 },
 {
  "name": "ENQUIRY-02-00052",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00053",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00054",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00055",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00056",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00057",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00058",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00059",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00060",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00061",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00062",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-02-00063",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00064",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00065",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00066",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00067",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00068",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00069",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00070",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00070-1",
  "docstatus": 2,
  "amended_from": "ENQUIRY-02-00070"
 },
 {
  "name": "ENQUIRY-02-00071",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00072",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00073",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00074",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00075",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00076",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00077",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00078",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00079",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00080",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00081",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00082",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00083",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00084",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00085",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00086",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00087",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00088",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00089",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00090",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00091",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00092",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00093",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00094",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00095",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-02-00096",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00097",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00098",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00099",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00100",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00101",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00102",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00103",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00104",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00105",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00106",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00107",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00108",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00109",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00110",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00111",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00112",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00113",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00114",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00115",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00116",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00117",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00117-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00117"
 },
 {
  "name": "ENQUIRY-02-00118",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00119",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00120",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00121",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00122",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00123",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00124",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00125",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00126",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00127",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00128",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00129",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00130",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00131",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00132",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00133",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00134",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00135",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00136",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00137",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00138",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00139",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00140",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00141",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00142",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00143",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00144",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00145",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00146",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00147",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00148",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00149",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00150",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00151",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00152",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00153",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00154",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00155",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00156",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00156-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00156"
 },
 {
  "name": "ENQUIRY-02-00157",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00158",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00159",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00160",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00161",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00162",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00163",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00164",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00165",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00166",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00167",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00168",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00169",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00170",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00171",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00172",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00173",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00174",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00175",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00176",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00177",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00178",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00179",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00180",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00181",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00182",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00183",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00184",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00185",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00186",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00187",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00188",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00189",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00190",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00191",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00192",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00193",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00194",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00195",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00196",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00197",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00198",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00199",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00200",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00201",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00202",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00203",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00204",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00205",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00206",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00207",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00208",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00209",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00210",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00211",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00212",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00213",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00214",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00215",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00216",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00217",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00218",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00219",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00220",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00221",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00222",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00223",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00224",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00225",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00226",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00227",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00228",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00229",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00230",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00231",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00232",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00233",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00234",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00235",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00236",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00237",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00238",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00239",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00240",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00241",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00242",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00243",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00244",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00245",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00246",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00247",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00248",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00249",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00250",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00251",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00252",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00253",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00254",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00255",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00256",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00257",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00258",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00259",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00260",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00261",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00262",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00263",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00264",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00265",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00266",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00267",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00268",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00269",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00270",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00271",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00272",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00273",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00274",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00275",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00276",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00277",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00278",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00279",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00280",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00281",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00282",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00283",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00284",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00285",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00286",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00287",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00288",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00289",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00289-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00289"
 },
 {
  "name": "ENQUIRY-02-00290",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00291",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00292",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00293",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00294",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00295",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00296",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00297",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00298",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00299",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00300",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00301",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00302",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00303",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00304",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00305",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00305-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00305"
 },
 {
  "name": "ENQUIRY-02-00306",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00307",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00308",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00309",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00310",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00311",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00312",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00313",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00314",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00315",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00316",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00317",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00317-1",
  "docstatus": 2,
  "amended_from": "ENQUIRY-02-00317"
 },
 {
  "name": "ENQUIRY-02-00317-2",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00317-1"
 },
 {
  "name": "ENQUIRY-02-00318",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00319",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00320",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00321",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00322",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00323",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00323-1",
  "docstatus": 2,
  "amended_from": "ENQUIRY-02-00323"
 },
 {
  "name": "ENQUIRY-02-00323-2",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00323-1"
 },
 {
  "name": "ENQUIRY-02-00324",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00325",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00326",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00327",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00328",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00329",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00330",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00330-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00330"
 },
 {
  "name": "ENQUIRY-02-00331",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00332",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00333",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00334",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00335",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00336",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00337",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00338",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00339",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00340",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00341",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00342",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00343",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00344",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00345",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00346",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00347",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00348",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00349",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00350",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00351",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00352",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00353",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00354",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00355",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00356",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00357",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00358",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00359",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00360",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00361",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00362",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00363",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00364",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00365",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00366",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00367",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00368",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00369",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00370",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00371",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00372",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00373",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00374",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00375",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00376",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00377",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00378",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00379",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00380",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00381",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00382",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00383",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00384",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00385",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00386",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00387",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00388",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00389",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00390",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00391",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00392",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00393",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00394",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00395",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00396",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00397",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00398",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00399",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00400",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00401",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00402",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00403",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00404",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00405",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00406",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00407",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00408",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00409",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00410",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00411",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00412",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00413",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00414",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00415",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00416",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00417",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00418",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00419",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00420",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00421",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00422",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00423",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00424",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00425",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00426",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00427",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00428",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00429",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00430",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00431",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00432",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00433",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00433-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00433"
 },
 {
  "name": "ENQUIRY-02-00434",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00435",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00436",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00437",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00438",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00439",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00440",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00441",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00442",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00443",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00444",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00444-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00444"
 },
 {
  "name": "ENQUIRY-02-00445",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00446",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00447",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00448",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00449",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00450",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00451",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00452",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00453",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00454",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00455",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00456",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00457",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00458",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00459",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00460",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00461",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00462",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00463",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00464",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00465",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00466",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00467",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00468",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00469",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00470",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00471",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00472",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00473",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00474",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00475",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00476",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00477",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00478",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00479",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00480",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00481",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00482",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00483",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00484",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00485",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00486",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00487",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00488",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00489",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00490",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00491",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00492",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00493",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00494",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00495",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00496",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00497",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00498",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00499",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00500",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00501",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00502",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00503",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00504",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00505",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00506",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00507",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00508",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00509",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00510",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00511",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00512",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00513",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00514",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00515",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00516",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00517",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00518",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00519",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00520",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00521",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00522",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00523",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00524",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00525",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00526",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00527",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00528",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00529",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00530",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00531",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00532",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00533",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00534",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00535",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00536",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00537",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00538",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00539",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00540",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00541",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00542",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00543",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00544",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00545",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00546",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00547",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00548",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00549",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00550",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00551",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00552",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00553",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00555",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00556",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00557",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00558",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00559",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00560",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00561",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00562",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00563",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00564",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00565",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00566",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00567",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00568",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00569",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00570",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00571",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00572",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00573",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00574",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00575",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00576",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00577",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00578",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00579",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00580",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00581",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00582",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00583",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00584",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00585",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00586",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00587",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00588",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00589",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00590",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00591",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00592",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00593",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00594",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00595",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00596",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00597",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00598",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00599",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00600",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00601",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00602",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00603",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00604",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00605",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00606",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00607",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00608",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00609",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00610",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00611",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00612",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00613",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00614",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00615",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00616",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00617",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00618",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00619",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00620",
  "docstatus": 2
 },
 {
  "name": "ENQUIRY-02-00620-1",
  "docstatus": 1,
  "amended_from": "ENQUIRY-02-00620"
 },
 {
  "name": "ENQUIRY-02-00621",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00622",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00623",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00624",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00625",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00626",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00627",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00628",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00629",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00630",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00631",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00632",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00633",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00634",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00635",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00636",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00637",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00638",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00639",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00640",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00641",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00642",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00643",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00644",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00645",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00646",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00647",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00648",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00649",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00650",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00651",
  "docstatus": 0
 },
 {
  "name": "ENQUIRY-02-00652",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00653",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00654",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00655",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00656",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00657",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00658",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00659",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00660",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00661",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00662",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00663",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00664",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00665",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00666",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00667",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00668",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00669",
  "docstatus": 1
 },
 {
  "name": "ENQUIRY-02-00670",
  "docstatus": 1
 }
]

