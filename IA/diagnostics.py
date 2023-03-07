import wmi
import datetime
import platform
import os, sys

# Variables
wrapper = wmi.WMI()
startupDir = str("C:/Users/" + os.getlogin() + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
diagnosticFile = str("C:/Users/" + os.getlogin() + "/Desktop/Diagnostics.log")


# Functions
def getProcesses():
  # Needs testing
  with open(diagnosticFile, "w+") as file:
    file.write("PID   PROCESS NAME")
 
    # Iterating through all the running processes
    for process in wrapper.Win32_Process():
      file.write(f"{process.ProcessId:<10} {process.Name}")
    return True


def getRuntime():
    # Needs testing
    with open(diagnosticFile, "w+") as file:
      OS = ("Operating-System: ", platform.system())
      ver = ("Version: ", platform.version())
      machine = ("Machine-Type: ", platform.machine())
      currentTime = ("Time: ", datetime.now().time())
      currentDate = ("Date: ", datetime.now().date())
      encoding = ("Encoding: ", sys.getfilesystemencoding())
    
      returnList = (OS, ver, machine, currentDate, currentTime, encoding)
      file.write(returnList)
      return True


def getSysInfo():
  # Needs testing
  with open(diagnosticFile, "w+") as file:
    returnlist = list()
    returnlist.append(platform.uname())
    file.write(''.join(returnlist))
    return True


def getStartup():
  # Needs testing
  with open(diagnosticFile, "w+") as file:
    for FILE in startupDir:
      file.write(FILE, "\n")