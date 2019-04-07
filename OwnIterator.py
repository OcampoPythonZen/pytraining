class MyIterator:
    """
    My own iterator
    """
    def __init__(self, *args):
        self.position = 0
        self.args = args
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.args):
            raise StopIteration
        args = self.args[self.position]
        self.position += 1
        return args

if __name__ == "__main__":
    i = MyIterator('777',1,2,3,4,5,6,7,'333',123)
    for item in i:
        print(item)
