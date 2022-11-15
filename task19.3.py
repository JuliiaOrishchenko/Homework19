class MyIterator:

    def __init__(self, data):
        self.data = data
        self.list_len = len(self.data)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.list_len:
            item = self.data[self.position]
            self.position += 1
            return item
        raise StopIteration

    def __getitem__(self, item):
        return self.data[item]


my_shiny_list = ["each", "hunter", "wanna", "know"]
for word in MyIterator(my_shiny_list):
    print(word)
print(MyIterator(my_shiny_list)[1])
