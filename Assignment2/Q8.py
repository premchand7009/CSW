def process_emails(email_list):
    valid_emails = list(filter(lambda e: "@" in e and (e.endswith(".com") or e.endswith(".org")), email_list))
    domains = [email.split("@")[1].split(".")[0] for email in valid_emails]
    domain_freq = {domain: domains.count(domain) for domain in set(domains)}
    print("Valid Emails:", valid_emails)
    print("Domains:", domains)
    print("Domain Frequency:", domain_freq)

emails = ["test@gmail.com", "hello123", "abc.org"]
process_emails(emails)
