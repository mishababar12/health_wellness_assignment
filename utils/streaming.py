
# Function: stream_output
# Purpose: Agent ka output screen par dikhana

"""
Yeh function sirf ek kaam karta hai —
jo bhi output agent se mile (uska `pretty_output`),
use console par print karta hai.


- Normally yeh function streaming ke waqt use hota hai — 
jaise jab hum Runner.stream(...) chalate hain, 
tab har step ko pretty format me show karne ke liye
yeh function madad karta hai.

"""

def stream_output(output):
    print(output.pretty_output)
