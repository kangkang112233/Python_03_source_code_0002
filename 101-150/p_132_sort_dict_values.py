# Sorting Dictionary Values with itemgetter()
# TIMESTAMP__2024_08_04__120902
# This example demonstrates how to sort dictionary values using itemgetter() in a library management system.

from operator import itemgetter

# Sample dictionary representing book titles and their publication years
books = {
    "Python Programming": 2021,
    "Learning Python": 2019,
    "Effective Python": 2015,
    "Fluent Python": 2016,
}

# Sorting the dictionary by values (publication years)
sorted_books = sorted(books.items(), key=itemgetter(1))

# Display the sorted dictionary
for title, year in sorted_books:
    print(f"{title}: {year}")
