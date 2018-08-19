'''
    File name: Payroll.py
    Author: Aravind Babu M
    Date created: 08/20/2018
    Date last modified: 08/20/2018
    Python Version: 3.6.3
'''

import calendar
import datetime

#basic 40% of gross
#hra below 22000 - 30% of gross; 25% of gross
#conveyance 1600
#medical 1250
#special -> gross - [basic+hra+conveyance+medical]
#deductions = pf + esi + pt + tds
#[gross] > 21000, pf = 15000 * 12%; else [gross - hra]*12%
#esi = gross * 1.75%
#[gross]*6 months <= 75000, pt = 171; else 208
#actual gross = gross - [gross_per_day * number of loss of pay days]

def main():
    inp_gross = input("Enter Gross Amount: ")
    lop_num_of_days = input("Enter number of days of LOP: ")
    night_num_of_days = input("Enter  number of days of night pay: ")
    double_num_of_days = input("Enter number of days of double pay: ")
    incentive = input("Enter incentive amount: ")

    now = datetime.datetime.now()
    num_of_days = calendar.monthrange(now.year,now.month)[1]

    gross_per_day = int(inp_gross) / num_of_days

    gross = (int(inp_gross) - (int(gross_per_day) * int(lop_num_of_days)))

    basic = int(gross) * (40/100)

    if (int(gross) <= 22000):
        hra = int(gross) * (30/100)
    else:
        hra = int(gross) * (25/100)

    conveyance = 1600
    medical = 1250
    special = abs(int(gross) - (int(basic) + int(hra) + int(conveyance) + int(medical)))

    if (int(gross) <= 21000):
        pf = (int(gross) - int(hra)) * (12/100)
        esi = int(gross) * (1.75/100)
    else:
        pf = 15000 * (12/100)
        esi = 0

    if ((int(gross) * 6) <= 75000):
        pt = 171
    else:
        pt = 208
    
    deductions = abs(int(pf) + int(esi) + int(pt))
    net = abs(int(gross) - int(deductions))

    night_shift = 100
    night_shift_allowance = int(night_shift) * int(night_num_of_days)

    double_pay = net / num_of_days
    double_pay_allowance = int(double_pay) * int(double_num_of_days)

    total_allowances = abs(int(night_shift_allowance) + int(double_pay_allowance) + int(incentive))

    take_home = abs(int(net) + int(total_allowances))

    print ("-------------------------------")
    print ("Actual Gross     : ", int(inp_gross))
    print ("Num LOP          : ", int(lop_num_of_days))
    print ("-------------------------------")
    print ("Basic            : ", int(basic))
    print ("HRA              : ", int(hra))
    print ("Conveyance       : ", int(conveyance))
    print ("Medical          : ", int(medical))
    print ("Special          : ", int(special))
    print ("-------------------------------")
    print ("Gross            : ", int(gross))
    print ("-------------------------------")
    print ("PF               : ", int(pf))
    print ("ESI              : ", int(esi))
    print ("PT               : ", int(pt))
    print ("-------------------------------")
    print ("Deductions       : ", int(deductions))
    print ("-------------------------------")
    print ("Net Pay          : ", int(net))
    print ("-------------------------------")
    print ("Night shift      : ", int(night_shift_allowance))
    print ("Double pay       : ", int(double_pay_allowance))
    print ("Incentives       : ", int(incentive))
    print ("-------------------------------")
    print ("Total Allowances : ", int(total_allowances))
    print ("-------------------------------")
    print ("Take home        : ", int (take_home))
    print ("-------------------------------")

if __name__ == '__main__':  
   main()
