class EmploymentTypes:
    def _init_(self, employment_type):
        self.employment_type = employment_type

emp_types = EmploymentTypes(input("Enter your employment type, if you are permanent or temporary: "))
print(emp_types.employment_type)


class Sector:
    def _init_(self, sector):
        self.sector = sector

sector = Sector(input("Enter your Sector, if you works under Government, private or cooperate: "))
print(sector.sector)


class BasicPay:
    def _init_(self, basic_pay):
        self.basic_pay = basic_pay

    def get_annual_pay(self):
        return self.basic_pay * 12

obj1 = BasicPay(float(input("Enter your basic pay: ")))
print(obj1.get_annual_pay())


class Allowance:
    def _init_(self, allowance_percentage=0.0):
        self.allowance_percentage = allowance_percentage  # Convert to decimal

    def set_allowance_percentage(self, allowance_percentage):
        self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

    def get_total_allowance(self, basic_pay):
        return self.allowance_percentage * basic_pay

obj2 = Allowance()
obj2.set_allowance_percentage(float(input("Enter your Allowance: ")))
print(obj2.get_total_allowance(obj1.get_annual_pay())) 


class Allowance:
    def init(self, allowance_percentage=0.0):
        self.allowance_percentage = allowance_percentage  # Convert to decimal

    def set_allowance_percentage(self, allowance_percentage):
        self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

    def get_total_allowance(self, BasicPay):
        return self.allowance_percentage *BasicPay

obj2 = Allowance()
obj2.set_allowance_percentage(float(input("Enter your Allowance: ")))
print(obj2.get_total_allowance(obj1.getBasicPay())) 

class fees_remuneration:
    def init(self, fees_remuneration_percentage=0.0):
        self.fees_remuneration_percentage = fees_remuneration_percentage  # Convert to decimal

    def set_fees_remuneration_percentage(self,fees_remuneration_percentage):
        self.fees_remuneration_percentage =fees_remuneration_percentage / 100  # Convert to decimal

    def get_total_fees_remuneration_(self, BasicPay):
        return self.fees_remuneration_percentage *BasicPay 

obj3= fees_remuneration()
obj3.set_fees_remuneration_percentage(float(input("Enter your fees_remuneration_: ")))
print(obj3.get_total_fees_remuneration_(obj1.getBasicPay())) 

class commission:
    def init(self, commission_percentage=0.0):
        self.commission_percentage = commission_percentage  # Convert to decimal

    def set_commission_percentage(self,commission_percentage):
        self.commission_percentage =commission_percentage / 100  # Convert to decimal

    def get_total_commission(self, BasicPay):
        return self.commission_percentage *BasicPay 

obj4= commission()
obj4.set_commission_percentage(float(input("Enter your commission: ")))
print(obj4.get_total_commission(obj1.getBasicPay())) 

class leave_encashment:
    def init(self, leave_encashment_percentage=0.0):
        self.leave_encashment_percentage = leave_encashment_percentage # Convert to decimal

    def set_leave_encashment_percentage(self,leave_encashment_percentage):
        self.leave_encashment_percentage =leave_encashment_percentage / 100  # Convert to decimal

    def get_total_leave_encashment(self, BasicPay):
        return self.leave_encashment_percentage *BasicPay

obj5= leave_encashment()
obj5.set_leave_encashment_percentage(float(input("Enter your leave_encashment: ")))
print(obj5.get_total_leave_encashment(obj1.getBasicPay())) 

class shareofProfirreceived:
    def init(self, shareofProfirreceived_percentage=0.0):
        self.shareofProfirreceived_percentage = shareofProfirreceived_percentage  # Convert to decimal

    def set_shareofProfirreceived_percentage(self,shareofProfirreceived_percentage):
        self.shareofProfirreceived_percentage =shareofProfirreceived_percentage / 100  # Convert to decimal

    def get_total_shareofProfirreceived(self, BasicPay):
        return self.shareofProfirreceived_percentage *BasicPay 

obj6= shareofProfirreceived()
obj6.set_shareofProfirreceived_percentage(float(input("Enter your share of Profit received: ")))
print(obj6.get_total_shareofProfirreceived(obj1.getBasicPay()))

class consultancyIncome:
    def init(self, consultancyIncome_percentage=0.0):
        self.consultancyIncome_percentage = consultancyIncome_percentage # Convert to decimal

    def set_consultancyIncome_percentage(self,consultancyIncome_percentage):
        self.consultancyIncome_percentage =consultancyIncome_percentage / 100  # Convert to decimal

    def get_total_consultancyIncome(self, BasicPay):
        return self.consultancyIncome_percentage *BasicPay

obj7= consultancyIncome()
obj7.set_consultancyIncome_percentage(float(input("Enter your consultancy Income received: ")))
print(obj7.get_total_consultancyIncome(obj1.getBasicPay()))
    
class Other_HouseRentAllowances:
    def init(self, HouseRentAllowances_percentage=0.0):
        self.HouseRentAllowances_percentage = HouseRentAllowances_percentage  # Convert to decimal

    def set_HouseRentAllowances_percentage(self,HouseRentAllowances_percentage):
        self.HouseRentAllowances_percentage =HouseRentAllowances_percentage / 100  # Convert to decimal

    def get_total_HouseRentAllowances(self, BasicPay):
        return self.HouseRentAllowances_percentage *BasicPay 

obj8= Other_HouseRentAllowances()
obj8.set_HouseRentAllowances_percentage(float(input("Enter your other allowances that is house rent house rent  Income received: ")))
print(obj8.get_total_HouseRentAllowances(obj1.getBasicPay()))


class Other_mobile_allowances:
    def init(self, mobile_allowances_percentage=0.0):
        self.mobile_allowances_percentage = mobile_allowances_percentage  # Convert to decimal

    def set_mobile_allowances_percentage(self,mobile_allowances_percentage):
        self.mobile_allowances_percentage =mobile_allowances_percentage / 100  # Convert to decimal

    def get_total_mobile_allowances(self, BasicPay):
        return self.mobile_allowances_percentage *BasicPay

obj9= Other_mobile_allowances()
obj9.set_mobile_allowances_percentage(float(input("Enter your other allowances that is mobile_allowances received: ")))
print(obj9.get_total_mobile_allowances(obj1.getBasicPay()))

class Other_conveyance_allowances:
    def init(self, conveyance_allowances_percentage=0.0):
        self.conveyance_allowances_percentage = conveyance_allowances_percentage  # Convert to decimal

    def set_conveyance_allowances_percentage(self,conveyance_allowances_percentage):
        self.conveyance_allowances_percentage =conveyance_allowances_percentage / 100  # Convert to decimal

    def get_total_conveyance_allowances(self, BasicPay):
        return self.conveyance_allowances_percentage *BasicPay

obj10= Other_conveyance_allowances()
obj10.set_conveyance_allowances_percentage(float(input("Enter your other allowances that is conveyance_allowances received: ")))
print(obj10.get_total_conveyance_allowances(obj1.getBasicPay()))

class Other_ltc:
    def init(self, ltc_percentage=0.0):
        self.ltc_percentage =ltc_percentage  # Convert to decimal

    def set_ltc_percentage(self,ltc_percentage):
        self.ltc_percentage =ltc_percentage / 100  # Convert to decimal

    def get_total_ltc(self, BasicPay):
        return self.ltc_percentage *BasicPay

obj11= Other_ltc()
obj11.set_ltc_percentage(float(input("Enter your other allowances that is ltc received: ")))
print(obj11.get_total_ltc(obj1.getBasicPay()))

class Other_anyother_allowances:
    def init(self, anyother_allowances_percentage=0.0):
        self.anyother_allowances_percentage =anyother_allowances_percentage  # Convert to decimal

    def set_anyother_allowances_percentage(self,anyother_allowances_percentage):
        self.anyother_allowances_percentage =anyother_allowances_percentage / 100  # Convert to decimal

    def get_total_anyother_allowances(self, BasicPay):
        return self.anyother_allowances_percentage *BasicPay

obj12= Other_anyother_allowances()
obj12.set_anyother_allowances_percentage(float(input("Enter your other allowances that is anyother_allowances received: ")))
print(obj12.get_total_anyother_allowances(obj1.getBasicPay()))

class NPPF:
    def init(self, NPPF_percentage=0.0):
        self.NPPF_percentage =NPPF_percentage # Convert to decimal

    def set_NPPF_percentage(self,NPPF_percentage):
        self.NPPF_percentage =NPPF_percentage / 100  # Convert to decimal

    def get_total_NPPF(self, BasicPay):
        return self.NPPF_percentage *BasicPay

obj13= NPPF()
obj13.set_NPPF_percentage(float(input("Enter NPPF deduction: ")))
print(obj13.get_total_NPPF(obj1.getBasicPay()))


class GIS:
    def init(self, GIS_percentage=0.0):
        self.GIS_percentage =GIS_percentage # Convert to decimal

    def set_GIS_percentage(self,GIS_percentage):
        self.GIS_percentage =GIS_percentage / 100  # Convert to decimal

    def get_total_GIS(self, BasicPay):
        return self.GIS_percentage *BasicPay

obj14= GIS()
obj14.set_GIS_percentage(float(input("Enter GIS deduction: ")))
print(obj14.get_total_GIS(obj1.getBasicPay()))

class children:
    def init(self, children):
        self.children =children # Convert to decimal

    def set_children(self,children):
        self.children=children # Convert to decimal

    def get_children(self):
        return self.children

class children:
    def set_children(self, children):
        self.children=children
    def getchildren(self):
        return self.children  
children=children()
children.set_children(int(input("Enter the number of children you have: ")))
print(children.getchildren())


class Netincome:

    def get_total_income(self, 
                         BasicPay, 
                         Allowance, 
                         fees_remuneration,
                         commission, 
                         leave_encashment, 
                         consultancyIncome , 
                         shareofProfirreceived,
                         Other_HouseRentAllowances, 
                         Other_mobile_allowances,
                         Other_conveyance_allowances,
                         Other_ltc,
                         Other_anyother_allowances,
                         NPPF,
                         GIS
                         
                         ):
        
        return (BasicPay 
                + Allowance
                +fees_remuneration
                +commission 
                +leave_encashment
                +consultancyIncome
                +shareofProfirreceived
                +Other_HouseRentAllowances
                +Other_mobile_allowances
                +Other_conveyance_allowances
                +Other_ltc
                + Other_anyother_allowances
                -NPPF
                -GIS
        )
    
obj40=Netincome()
# print(obj40.get_total_income(obj1.getBasicPay(), 
print(obj40.get_total_income(
    obj1.getBasicPay(),
    obj2.get_total_allowance(obj1.getBasicPay()),
    obj3.get_total_fees_remuneration_(obj1.getBasicPay()),
    obj4.get_total_commission(obj1.getBasicPay()), 
    obj5.get_total_leave_encashment(obj1.getBasicPay()), 
    obj6.get_total_shareofProfirreceived(obj1.getBasicPay()),
    obj7.get_total_consultancyIncome(obj1.getBasicPay()) , 
    obj8.get_total_HouseRentAllowances(obj1.getBasicPay()),
    obj9.get_total_mobile_allowances(obj1.getBasicPay()),
    obj10.get_total_conveyance_allowances(obj1.getBasicPay()),
    obj11.get_total_ltc(obj1.getBasicPay()),
    obj12.get_total_anyother_allowances(obj1.getBasicPay()),
    obj13.get_total_NPPF(obj1.getBasicPay()),
    obj14.get_total_GIS(obj1.getBasicPay())
))


class taxBreaks:
    def getTB ( Netincome):
    # def taxBreaks(Netincome):
        if Netincome() <= 300000:
            print(" 0% on NetIncome")
            TB1= (0/100)*Netincome
            print("Your income charge no tax rate" , TB1)

        elif 300001<Netincome <400000:
            print(" 10% on NetIncome")
            TB2= (10/100)*Netincome
            print("You have to pay" , TB2)

        elif 400001<Netincome <650000:
            print(" 15% on NetIncome")
            TB3= (15/100)*Netincome
            print("You have to pay" , TB3)

        elif 650001<Netincome <1000000:
            print(" 20% on NetIncome")
            TB4= (20/100)*Netincome
            print("You have to pay" , TB4)
    
        elif 1000001<Netincome <1500000:
            print(" 25% on NetIncome")
            TB5= (25/100)*Netincome
            print("You have to pay" , TB5)

        else:
            print(" 30% on NetIncome")
            TB6= (30/100)*Netincome
            print("You have to pay" , TB6)

objTB= taxBreaks()
# objTB.set_GIS_percentage(float(input("Enter GIS deduction: ")))
print(objTB.getTB(obj40.get_total_income(BasicPay, 
                         Allowance, 
                         fees_remuneration,
                         commission, 
                         leave_encashment, 
                         consultancyIncome , 
                         shareofProfirreceived,
                         Other_HouseRentAllowances, 
                         Other_mobile_allowances,
                         Other_conveyance_allowances,
                         Other_ltc,
                         Other_anyother_allowances,
                         NPPF,
                         GIS)))
print(objTB.getTB(obj40.get_total_income( obj1.getBasicPay()),
    obj2.get_total_allowance(obj1.getBasicPay()),
    obj3.get_total_fees_remuneration_(obj1.getBasicPay()),
    obj4.get_total_commission(obj1.getBasicPay()), 
    obj5.get_total_leave_encashment(obj1.getBasicPay()), 
    obj6.get_total_shareofProfirreceived(obj1.getBasicPay()),
    obj7.get_total_consultancyIncome(obj1.getBasicPay()) , 
    obj8.get_total_HouseRentAllowances(obj1.getBasicPay()),
    obj9.get_total_mobile_allowances(obj1.getBasicPay()),
    obj10.get_total_conveyance_allowances(obj1.getBasicPay()),
    obj11.get_total_ltc(obj1.getBasicPay()),
    obj12.get_total_anyother_allowances(obj1.getBasicPay()),
    obj13.get_total_NPPF(obj1.getBasicPay()),
    obj14.get_total_GIS(obj1.getBasicPay())))