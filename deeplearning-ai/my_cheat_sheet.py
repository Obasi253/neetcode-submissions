# =====================================================================
#                 OBASI'S MASTER PYTHON CHEAT SHEET
# =====================================================================
# A living record of my core Python skills as I progress through my CS journey.
# Location: Ikom, Nigeria | Created: June 2026
# =====================================================================


# ---------------------------------------------------------------------
# TERMINOLOGY 1: VARIABLES & DATA TYPES
# ---------------------------------------------------------------------
# Rule: Text (Strings) MUST use quotation marks. Numbers stay free.
# Rule: Variable names use snake_case (lowercase with underscores).

# Text Data (String)
my_name = "Obasi"  # If quotes are missing, Python throws a NameError!

# Numerical Data (Integer)
my_score = 450  # No quotes! This allows Python to do math operations.
age = 30


# ---------------------------------------------------------------------
# TERMINOLOGY 2: THE HOLY TRINITY OF F-STRINGS
# ---------------------------------------------------------------------
# To inject code into text, you need 3 things:
# 1. The 'f' prefix before the opening quote.
# 2. Quotation marks to wrap the sentence.
# 3. Curly braces {} acting as a window to evaluate variables or math.

print(f"Hello, my name is {my_name}!")
print(f"Next year, my age will be {age + 1}")  # Math inside the window!


# ---------------------------------------------------------------------
# TERMINOLOGY 3: LARGE NUMBER FORMATTING (THE COMMA TRICK)
# ---------------------------------------------------------------------
# Syntax: {variable_name:,}
# The colon ':' acts as a separator, and the comma ',' tells Python 
# to format the number using thousands separators for human readability.

count = 1000000

# This outputs: "Total: 1,000,000" instead of "1000000"
print(f"Total: {count:,}") 


# ---------------------------------------------------------------------
# TERMINOLOGY 4: DYNAMIC VALUE OVERWRITING
# ---------------------------------------------------------------------
# Python reads code from top to bottom. If you reuse a variable name, 
# the old value gets completely replaced by the newest assignment.

current_score = 0
current_score = current_score + 50  # Overwrites 0 and updates to 50
current_score = current_score + 100 # Overwrites 50 and updates to 150

print(f"Final Score: {current_score}")
