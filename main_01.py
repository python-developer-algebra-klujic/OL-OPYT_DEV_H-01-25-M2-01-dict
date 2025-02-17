# Rjecnik je kolekcija koja elemente opisuje kao par kljuc, vrijednost.

# book = {
#     1: 'Vlak u snijegu',
#     2: 'Mato Lovrak',
#     3: 'Biblioteka "Lastavica"',
#     4: 1980
# }

book = {
    'title': 'Vlak u snijegu',
    'author': 'Mato Lovrak',
    'publisher': 'Biblioteka "Lastavica"',
    'year': 1980
}


# print(f'Naziv knjige: {book[1]}')
print(f'Naziv knjige: {book['title']}')
print(f'Autor knjige: {book['author']}')
print(f'Izdavac knjige: {book['publisher']}')
print(f'Godina izdanja knjige: {book['year']}')

# Dodavanje vrijednosti u rijecnik
book['number_of_pages'] = 250

print(book)
