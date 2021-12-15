Hotel={"rr":{"chicken65":700,"chicken biriyani":890},"buhari":{"mutton sukka":900,"mutton biriyani":900},"hahmed biriyani":{"veg rice":789,"jeera rice":890}}
order={}
class hotelfood:
    def __init__(self):
        print("hotels avilable rr,buhari,hahmed biriyani")
        self.hotelname=input("enter hotel name")
    def menucard(self):
        if type(self.hotelname)==str:
            if self.hotelname in Hotel:
                hotel=self.hotelname
                value=Hotel.get(self.hotelname)
                for i,j in value.items():
                    print(f"{i} : {j}")
                    
            else:
                raise ValueError("details not avilable")

        else:
            raise TypeError("invalid type")
    def order(self):
        enter=input("ordering type yes or no ")
        if enter == "yes":
            items=input("number of dishes = ")
            if int(items)>0 and int(items)<30:
                for i in range(int(items)):
                    dish=input("Enter dish name = ")
                    if(dish in Hotel[self.hotelname]):
                        quantity=input(f"Enter Quantity : ")
                        order[dish]=quantity
                    else:
                        raise ValueError("not available")
            else:
                raise ValueError("invalid type")
        else:
            print("Thank you")

    def bill(self):
        amount=0
        for i,j in order.items():
            price=Hotel[self.hotelname]
            amount=price[i]*int(j)
            print("order confirmed")
            print("bill amount", amount)
            print("Thank you",
                  "enjoy food")  

              
ret=hotelfood()
ret.menucard()
ret.order()
ret.bill()
                  

              
