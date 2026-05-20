class Book:
    count = 0
    def __init__(self,title,author,list_of_reviews):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews
        self.count +=1

    def add_review(self,new_review):
        self.list_of_reviews = self.list_of_reviews + new_review
        self.count+=1

    def count_review(self):
        return self.count
    
    def display_review(self):
        return self.list_of_reviews

obj1 = Book("LegendBook","Yash","Good Book")
obj1.add_review("Execellent book")
print(obj1.display_review(),obj1.count_review())