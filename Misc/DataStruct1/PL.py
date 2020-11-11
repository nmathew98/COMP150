def create_dict(file_name):
    with open(file_name) as file:
        contents = file.read().strip().split("\n")
        
    authors, books = [], []
    for content in contents:
        book, author = content.split("*")
        author = tuple(author.split())
        
        if author in authors:
            books[authors.index(author)] += [book]
        else:
            authors.append(author)
            books += [[book]]
                    
    print(len(books), len(authors))
    return dict(zip(authors, books))

print(create_dict('top_50_author.txt'))
