  
def convert(number):
    """В возврящаемую строку дописываются:
'Pling', если число number делится на 3,
'Plang', если число number делится на 5,
'Plong', если число number делится на 7,
само число number, если оно не делится ни на 3, ни на 5, ни на 7."""
    my_string = ""
    if number % 3 == 0:
        str = str + "Pling"
    if number % 5 == 0:
        str = str + "Plang"
    if number % 7 == 0:
        str = str + "Plong"
    if number % 7!= 0 and number % 5 != 0 and number % 3 != 0:
        str = str + my_string (number)
    return str
