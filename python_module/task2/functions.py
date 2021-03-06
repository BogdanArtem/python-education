"""Functions practice example"""

# Modify this function to return a list of strings as defined above
def list_benefits():
    """Return list of benefits"""
    return [
        'More organized code', 'More readable code',
        'Easier code reuse', 'Allowing programmers to share and connect code together'
        ]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    """Create sentence"""
    return benefit + ' is a benefit of functions!'

def name_the_benefits_of_functions():
    """Print all benefits of function"""
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
