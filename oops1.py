class employee:
    def __init__(self):
        print(id(self))
        print("started executing data")
        self.id=201
        self.salary=50000
        self.designation="software engineer"
        print("data has been executed")

    def travel(self,destination):
        print("this travel func runs manually")
        print(f"employee is travelling to {destination}")

#craeting an object of employee class
sam=employee()
sam.name="sam kumar"
#sam2=employee()
print(id(sam))
print(sam.name)
#print(id(sam2))
#print(sam.id)
#sam.travel("bangalore")

#print(type(sam))

