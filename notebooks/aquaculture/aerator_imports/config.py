"""
Configuration module for aerator imports data analysis.
Contains all mappings, constants, and settings.
"""

# Data paths
INPUT_DIR = "../../../data/raw/aquaculture/aerator_imports/"
YEAR_RANGE = range(2021, 2025)

# Date columns that need conversion
DATE_COLUMNS = [
    "FECHA DE LIQUIDACIóN",
    "FECHA DE LLEGADA",
    "FECHA DE EMBARQUE",
    "FECHA PAGO",
    "FECHA INGRESO SISTEMA",
]

# Column name translations (Spanish to English)
COLUMN_TRANSLATIONS = [
    "CUSTOMS",
    "ADVALOREM",
    "FREIGHT AGENCY",
    "CUSTOMS AGENT",
    "YEAR",
    "MANUFACTURE YEAR",
    "PACKAGES",
    "QUANTITY",
    "CHARACTERISTICS",
    "EMBARKATION CITY",
    "RELEASE CODE",
    "BILL OF LADING",
    "CONTAINER",
    "TNAN CODE",
    "DAU",
    "COMMERCIAL WAREHOUSE",
    "COMMERCIAL PRODUCT DESCRIPTION",
    "DAY",
    "CONSIGNEE ADDRESS",
    "SHIPPER",
    "TRANSPORT COMPANY",
    "GOODS STATUS",
    "INVOICE",
    "ASSESSMENT DATE",
    "SHIPPING DATE",
    "SETTLEMENT DATE",
    "ARRIVAL DATE",
    "SYSTEM ENTRY DATE",
    "PAYMENT DATE",
    "INCOTERM",
    "ITEM",
    "BRAND",
    "COMMERCIAL BRAND",
    "MONTH",
    "MERCHANDISE MODEL",
    "VESSEL",
    "FINAL CARGO NUMBER",
    "MANIFEST NUMBER",
    "COUNTRY OF ORIGIN",
    "TARIFF HEADING",
    "NET WEIGHT KG",
    "PROBABLE IMPORTER",
    "PRODUCT",
    "ENDORSEMENT",
    "CUSTOMS REGIME",
    "IMPORTER RUC",
    "ASSESSMENT TYPE",
    "UNIT OF MEASURE",
    "CIF US$",
    "FREIGHT US$",
    "FOB US$",
    "FOB UNIT US$",
    "INSURANCE US$",
    "TRANSPORT MODE",
]

# Brand standardization mapping
BRAND_MAPPING = {
    "SIN MARCA": "GENERICO",
    "S/MARCA": "GENERICO",
    "SINMARCA": "GENERICO",
    "SMARCA": "GENERICO",
    "S/M": "GENERICO",
    "SM": "GENERICO",
    "N-M": "GENERICO",
    "AEROMIX SYSTEMS": "AEROMIX",
    "WALKER AIREADORES": "WALKER",
    "WALKER-AIREADORES": "WALKER",
    "NEOPERL ITALIA": "NEOPERL",
}

# Model standardization mapping
MODEL_MAPPING = {
    "SIN MODELO": "GENERICO",
    "SIN MODELO,": "GENERICO",
    "S/MODELO": "GENERICO",
    "SMODELO": "GENERICO",
    "S/M": "GENERICO",
    "SM": "GENERICO",
    "N-M": "GENERICO",
    "N/A": "GENERICO",
    "NA": "GENERICO",
}

# Product standardization mapping
PRODUCT_MAPPING = {
    "AERADOR": "AIREADOR",
    "AIREADORES": "AIREADOR",
    "AIREADORAS": "AIREADOR",
    "AIREADORAS DE AGUA": "AIREADOR",
    "AIREADORES DE AGUA": "AIREADOR",
    "AIREADORES DE AGUA DULCE": "AIREADOR",
    "AIREADORES DE AGUA SALADA": "AIREADOR",
    "AIREADORES DE AGUA MARINA": "AIREADOR",
    "SET DE AIREADORES": "AIREADOR",
    "AIREADORES DE 8 PALETAS": "AIREADOR",
    "AIREADORES DE 12 PALETAS": "AIREADOR",
    "AIREADORES DE 16 PALETAS": "AIREADOR",
    "AIREADORES DE 3 HP": "AIREADOR",
    "AIREADORES DE 5 HP": "AIREADOR",
    "AIREADORES DE 3.5 HP": "AIREADOR",
    "AIREADORES DE 2 HP": "AIREADOR",
    "AIREADOR DE 4 PALETAS": "AIREADOR",
    "AIREADOR DE 8 PALETAS": "AIREADOR",
    "AIREADOR DE 12 PALETAS": "AIREADOR",
    "AIREADOR DE 16 PALETAS": "AIREADOR",
    "AIREADOR DE 3 HP": "AIREADOR",
    "AIREADOR DE 5 HP": "AIREADOR",
    "AIREADOR DE 3.5 HP": "AIREADOR",
    "AIREADOR DE 2 HP": "AIREADOR",
    "AIREADORES DE 16 PALETAS PARA MEZCLAR OXIGENO CON MOTOR": "AIREADOR",
    "MULTI IMPULSOR AIREADOR DE PALETAS": "AIREADOR",
    "AIREADOR SANIPERL-DL": "AIREADOR",
    "AIREADORES 3 HP 460V": "AIREADOR",
    "AIREADORES 3.5 HP 440V": "AIREADOR",
    "PADDLE WHEEL AERATOR": "AIREADOR",
    "PADDLE WHEEL AERATOR/ AIREADOR": "AIREADOR",
    "PALETA DE AIREADORES FUDU": "PALETAS PARA AIREADOR",
}

# Analysis configuration
ANALYSIS_CONFIG = {
    # Numeric columns for analysis (using original Spanish names)
    "numeric_cols": [
        "US$ FOB",
        "US$ CIF",
        "CANTIDAD",
        "PESO NETO KG",
        "ADVALOREM",
        "US$ FLETE",
        "US$ SEGURO",
        "BULTOS",
    ],
    # Categorical columns for analysis (using original Spanish names)
    "categorical_cols": [
        "PAIS ORIGEN",
        "MARCA",
        "PROBABLE IMPORTADOR",
        "DESCRIPCION PRODUCTO COMERCIAL",
        "CIUDAD EMBARQUE",
        "EMPRESA TRANSPORTADORA",
        "DIRECCION CONSIGNATARIO",
        "MODELO MERCADERIA",
    ],
    # Default number of top items to show
    "top_n": 10,
    # Price range for filtering brands in price analysis
    "price_filter_range": (500, 1500),
    # Percentile for outlier exclusion in visualizations
    "outlier_percentile": 95,
}

# Visualization settings
VIZ_CONFIG = {
    "default_figsize": (12, 8),
    "color_palette": "Spectral",
    "background_color": "lightblue",
    "dpi": 100,
    "style": "whitegrid",
}
