voters = [("Amit", 22, "Indian"),
          ("John", 30, "USA"),
          ("Neha", 17, "Indian"),
          ("Ravi", 19, "Indian")]

eligible_voters = list(filter(lambda v: v[1] >= 18 and v[2] == "Indian", voters))
eligible_names = [v[0] for v in eligible_voters]
count = len(eligible_names)

voter_dict = {
    "Eligible": [v[0] for v in voters if v[1] >= 18 and v[2] == "Indian"],
    "NotEligible": [v[0] for v in voters if not (v[1] >= 18 and v[2] == "Indian")]
}

print("Eligible:", eligible_names)
print("Count:", count)
print(voter_dict)
