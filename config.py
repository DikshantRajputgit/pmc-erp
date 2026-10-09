import streamlit as st

# Streamlit secrets se DATABASE_URL uthana
try:
    DATABASE_URL = st.secrets["DATABASE_URL"]
except Exception:
    DATABASE_URL = None

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not configured in Streamlit Secrets")

PAGE_KEYS = [
    "dashboard",
    "sales_upload",
    "product_master",
    "doctor_master",
    "medical_master",
    "area_master",
    "product_mapping",
    "stock_entry",
    "doctor_expense",
    "sales_expense",
    "doctor_payment",
    "payment_collection",
    "medical_ledger",
    "doctor_pnl",
    "company_pnl",
    "user_management",
    "company_expense",
]

PAGE_LABELS = {
    "dashboard": "Dashboard",
    "sales_upload": "Sales Upload",
    "product_master": "Product Master",
    "doctor_master": "Doctor Master",
    "medical_master": "Medical Master",
    "area_master": "Area Master",
    "product_mapping": "Product Mapping",
    "stock_entry": "Stock Entry / Visits",
    "doctor_expense": "Doctor Expenses",
    "sales_expense": "Sales Person Expenses",
    "doctor_payment": "Doctor Payments",
    "payment_collection": "Payment Collection",
    "medical_ledger": "Medical Ledger",
    "doctor_pnl": "Doctor PNL",
    "company_pnl": "Company PNL",
    "user_management": "User Management",
    "company_expense": "Company Expenses",
}

COMMISSION_TYPES = ["SUPPLY", "MRP_PERCENT", "PAYMENT", "TRADE", "FIXED"]

COMMISSION_VALUE_HELP: dict[str, str] = {
    "SUPPLY": "**Percentage** of supply value in the visit period.",
    "MRP_PERCENT": "**Percentage** of MRP on sold qty.",
    "PAYMENT": "**Percentage** of collections from that medical.",
    "TRADE": "**Percentage** of sold value at rate.",
    "FIXED": "**Fixed amount** added per product line.",
}

DOCTOR_EXPENSE_TYPES = ["Gift", "Dinner", "Samples", "Tour", "Petrol", "Other"]
SALES_EXPENSE_TYPES = ["Fuel", "Food", "Hotel", "Travel", "Bike Service", "Mobile Recharge", "Other"]
COMPANY_EXPENSE_TYPES = ["Salary", "Samples", "Tour", "Other Operational"]
PAYMENT_MODES = ["Cash", "Cheque", "NEFT", "RTGS", "UPI", "Other"]
