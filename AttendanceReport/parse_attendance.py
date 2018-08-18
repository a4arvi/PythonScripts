'''
    File name: parse_attendance.py
    Author: Aravind Babu M
    Date created: 08/19/2018
    Date last modified: 08/19/2018
    Python Version: 3.6.3
'''

import csv, sys, itertools

class EmpPayroll(object):
    def __init__(self, ecode=None, ename=None, present=None, absent=None, absentDays=None):
        self.ecode = ecode
        self.ename = ename
        self.present = present
        self.absent = absent
        self.absentDays = absentDays

def main():
    try:
        filename = sys.argv[1]

        with open(filename, newline='') as f:
            for _ in range(2):
                next(f)
            for line in f:
                print (line[:-17])
                break

            f.seek(0, 0)
            for line in itertools.islice(f, 5, None):
                reader = csv.DictReader(f, restkey='Empty Field')
                reader.fieldnames = ("SrNo.  ",
                                     "Card No ",
                                     "ECode  ",
                                     "Employee Name         ",
                                     "PunchDate   ",
                                     "Day ",
                                     "Punch-Timings",
                                     "Last",
                                     "Shift",
                                     "MusterMark",
                                     "WorkTime",
                                     "ActualHours",
                                     "Late",
                                     "Early",
                                     "OverTime",
                                     "Remarks")

                #Array of class objects
                empList = []

                empCode = ""
                empName = ""
                present = 0
                absent = 0
                absentDays = ""
    
                try:
                    for row in reader:
                        if not row:
                            continue
            
                        ecode = row['ECode  ']
                        ename = row['Employee Name         ']
                        eday = row['Day ']
                        epunch = row['Punch-Timings']
                        epunch = epunch.strip()

                        #Append to array when the row correspond to next employee
                        if (empCode != "") and (ecode != "") and (empCode != ecode):
                            empList.append(EmpPayroll(empCode,empName,present,absent,absentDays[:-1]))
                            present = 0
                            absent = 0
                            absentDays = ""

                        #save name and code from first line for this employee
                        if (ecode != ""):
                            empCode = ecode
                            empName = ename

                        #When punch-in is valid, incr present
                        if (epunch != ""):
                            present += 1
                        else:
                            absent += 1
                            absentDays += eday + ","
            
                    #Append last valid employee entry
                    if (empCode != "") and (ecode == ""):
                        empList.append(EmpPayroll(empCode,empName,present,absent,absentDays[:-1]))
            
                    x = len(empList)
                    print ("Number of employee entries: %d" % x)
                    print ()

                    cnt = 1
                    print ("%4s %-10s %-30s %-10s %-10s %-10s %-10s" % ("S.No", "EmpCode", "EmpName", "NumDays", "Present", "Absent", "Absent Days"))
                    for row in empList:
                        print ("%3d. %-10s %-30s %-10d %-10d %-10d [%-10s]" % (cnt, row.ecode, row.ename, (int(row.present)+int(row.absent)),row.present, row.absent,row.absentDays))
                        cnt += 1
            
                except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    except IOError:
        print("Error: File not found")
    except IndexError:
        print("Error: Filename argument missing")

if __name__ == '__main__':  
   main()
