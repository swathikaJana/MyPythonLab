class multifunction():

    
    def Subfields():
        field=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Programming' ,'Natural Language Processing']
        print("Sub-fields in AI are:")
        for i in field:
            print(i)

    def OddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
           print(num,"is an even number")
        else:
           print(num,"is an odd number")

    def Eligible_for_Male(Gender,Age):
        if(Age>27):
          print("ELIGIBLE for Marriage")
        else:
          print("Not Eligible For Marriage")
     
    def Eligible_for_FeMale(Gender,Age):
        if(Age>21):
          print("ELIGIBLE for Marriage")
        else:
          print("Not Eligible For Marriage")
    
    def percentage1():
       

    def area():
        base=int(input("Enter the base:"))
        height=int(input("Enter the height:"))
        print("area of triangle = (base*height)/2;")
        area_tria=float(base*height)/2
        print(f"area of triangle = {area_tria}")

    def perimeter():
        height1=(int(input("Enter the height1:")))
        height2=(int(input("Enter the height2:")))
        height3=(int(input("Enter the height3:")))
        print("perimeter of triangle = (height1+height2+height3)")
        peri_tria= height1+height2+height3
        print(f"perimeter of triangle = {peri_tria}")

    
    