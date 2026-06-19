name = "Obasi"
daily_hours = 3
passport_target = 100000
saved_so_far = 15000

# Using triple quotes for a clean layout
dashboard = f"""
========================================
       {name.upper()}'S DEV DASHBOARD
========================================
* Study Plan: {daily_hours} hours a day
* Weekly Total: {daily_hours * 7} hours of coding!

[PASSPORT TRACKER]
* Target Amount: ₦{passport_target}
* Current Progress: ₦{saved_so_far}
* Remaining Balance: ₦{passport_target - saved_so_far}

Next Destination: Dublin, Ireland ✈️
========================================
"""

print(dashboard)
