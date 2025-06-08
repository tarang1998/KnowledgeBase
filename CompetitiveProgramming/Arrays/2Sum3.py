class TwoSum:

    def __init__(self):
        self.mem = {}

    def add(self,num):
        if num in self.mem:
            self.mem[num] += 1
        else:
            self.mem[num] = 1

    def find(self, target):

        for num in self.mem.keys():
            left = target -  num

            if left in self.mem:
                if left == num:
                    if self.mem[left] > 1:
                        return True
                else:
                    return True

        return False
    

if __name__ == "__main__":
    obj = TwoSum()
    obj.add(1)
    obj.add(2)
    obj.add(7)
    obj.add(11)
    obj.add(2)
    print(obj.find(9))
    print(obj.find(19))




