vendor = {"name": "alice", "date": "2026-10-01", "amount": float(42.50)};
#print(vendor["name"]);

def parse_line(vendor):
    print(vendor["name"])
    print(vendor["date"])
    print(vendor["amount"])
parse_line(vendor);