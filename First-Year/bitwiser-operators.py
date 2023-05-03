#
# Linux represents permissions as RWX, when it is represented numerically, 
#it is represented as the decimal equivalent of a 3 bit flag variable (7).  
#The left-most bit (the 4's place) irepresents the read permissions.  
#The middle bit (the 2's place) represents the write permissions, 
#and the last bit represents the execute permissions.
# (For more information on the actual Linux, you may review the following article:  
#Classic SysAdmin: Understanding Linux File PermissionsLinks to an external site.)

# Write three lines of code using the bitwise operators to
#change each of the three variables.

# You can hard code this for now if you wish, though we may use input statements later.

# Create a variable called permissions.  Set it equal to 7.

# Using bitwise operation, write one line of code that will change it to 3 
#(removing the Read permission).  Print the output.

# Using bitwise operation, write one line of code that will change it to 5
#(removing the Write permission).  Print the output.

# Using bitwise operation, write one line of code that will change it to 6
#(removing the Execute permission).  Print the output.

#https://docs.nersc.gov/filesystems/unix-file-permissions/

class permissionManager:
    def __init__(self):
        self.permission = 0b111
    
    def printRaw(self):
        print("RAW",bin(self.permission))
   
    def printTable(self):
        return False
    
    def canRead(self):
        return self.permission & 0b100 != 0
    
    def addRead(self):
        if self.canRead():
            return False
        self.permission ^= 0b100
        return True
        
    def removeRead(self):
        if not self.canRead():
            return False
        self.permission ^= 0b100
        return True
    
    def canWrite(self):
        return self.permission & 0b010 != 0
    
    def addWrite(self):
        if self.canWrite():
            return False
        self.permission ^= 0b010
        return True
        
    def removeWrite(self):
        if not self.canWrite():
            return False
        self.permission ^= 0b010
        return True
    
    def canExecute(self):
        return self.permission & 0b001 != 0
    
    def addExecute(self):
        if self.canExecute():
            return False
        self.permission ^= 0b001
        return True
        
    def removeExecute(self):
        if not self.canExecute():
            return False
        self.permission ^= 0b001
        print("Execute Permission: Removed")
        return True


h = permissionManager()

controlPanel = """
-- View Permissions --
0 = View raw permissions (Binary)
1 = View Permissions (Fancy)

-- Read --
2 = Can Read
3 = Remove Read
4 = Add Read

-- Write --
5 = Can Write
6 = Remove Write
7 = Add Write

-- Execute --
8 = Can Execute
9 = Remove Execute
10 = Add Execute

INPUT NUMBER HERE: 
"""

jumpList = [h.printRaw, h.printTable, h.canRead, h.removeRead, h.addRead, h.canWrite, h.removeWrite, h.addWrite, h.canExecute, h.removeExecute, h.addExecute]

while True:
    i = input(controlPanel).strip()
    if not i.isdigit():
        print("MUST BE A DIGIT")
        continue
    jumpList[int(i)]()
    input("PRESS ENTER TO CONTINUE")
