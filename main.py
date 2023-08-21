import whois

def check_domain_availability(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if not domain_info.status:
            return f"The domain '{domain_name}' is available!"
        else:
            return f"The domain '{domain_name}' is already registered."
    except whois.parser.PywhoisError:
        return f"An error occurred while checking the availability of '{domain_name}'."

if __name__ == "__main__":
    domain_name = input("Enter a domain name to check its availability: ")
    result = check_domain_availability(domain_name)
    print(result)
