import csv as c

data = [
    ['SN', 'Name', 'Country', 'Contribution', 'Year'],
    [1, 'Linus Torvalds', 'Finland', 'Linux Kernel', 1991],
    [2, 'Tim Berners-Lee', 'England', 'World Wide Web', 1990],
    [3, 'Guido van Rossum', 'Netherlands', 'Python', 1991]
]

filename = "contributions.csv"

with open(filename, mode='w', newline='') as file:
    writer = c.writer(file)
    writer.writerows(data)

print(f"Data has been written to {filename}")
