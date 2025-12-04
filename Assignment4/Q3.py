import re
s = "Contact: +91-9876543210, Office: (91) 98765 43211, Home: 0091 9876543212  91 9876543210"

pattern = r"(?:\+\d{2}-\d{10})|(?:\(\d{2}\)\s\d{5}\s\d{5})|(?:0091\s\d{10})|(?:\d{2}\s\d{10})"

print(re.sub(pattern, "+91-XXXXXXXXXX", s))
