from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("CRM"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "doctype",
					"name": "Lead",
					"description": _("Database of potential customers."),
				},
				{
					"type": "doctype",
					"name": "Opportunity",
					"description": _("Potential opportunities for selling."),
				},
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
				},
			]
		},
		{
			"label": _("Accounting"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "doctype",
					"name": "Company",
					"description": _("Company (not Customer or Supplier) master.")
				},
				{
					"type": "doctype",
					"name": "Account",
					"icon": "fa fa-sitemap",
					"label": _("Chart of Accounts"),
					"route": "Tree/Account",
					"description": _("Tree of financial accounts."),
				},
				{
					"type": "doctype",
					"name": "Cost Center",
					"icon": "fa fa-sitemap",
					"label": _("Cost Center"),
					"route": "Tree/Cost Center",
					"description": _("Tree of financial accounts."),
				},
				{
					"type": "report",
					"name":"General Ledger",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "doctype",
					"name": "Journal Entry",
					"description": _("Accounting journal entries.")
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"label": _("Budget vs Actual Revenue"),
					"name": "Budget Variance Report",
					"doctype": "Cost Center"
				},
				{
					"type": "report",
					"is_query_report": True,
					"label": _("Debtors aging"),
					"name": "Accounts Receivable Summary",
					"doctype": "Sales Invoice"
				},
				{
					"type": "report",
					"is_query_report": True,
					"label": _("Income and Expense Report"),
					"name": "Profit and Loss Statement",
					"doctype": "GL Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"label": _("Cost center based Income and Expense Report"),
					"name": "Profitability Analysis",
					"doctype": "GL Entry"
				},

				{
					"type": "report",
					"is_query_report": True,
					"label": _("Lead Details"),
					"name": "Lead Details",
					"doctype": "Lead"
				},

				

			]
		}
	]
