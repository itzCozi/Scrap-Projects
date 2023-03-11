# Earth Liberation Front
import wmi
import requests
import ctypes
import platform
import os, sys
from datetime import datetime

# Variables
counter = 0
wrapper = wmi.WMI()
IP = requests.get('https://api.ipify.org')
startupDir = str("C:/Users/" + os.getlogin() + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
diagnosticFile = str("C:/Users/" + os.getlogin() + "/OneDrive/Desktop/Diagnostics.log")


# Functions
class functions:
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
        file.write(str(returnList))
        return True


  def getSysInfo():
    # Needs testing
    with open(diagnosticFile, "w+") as file:
      returnlist = list()
      returnlist.append(platform.uname())
      file.write(str(returnlist))
      return True


  def getStartup():
    # Needs testing
    with open(diagnosticFile, "w+") as file:
      counter = 0
      for FILE in startupDir:
        file.write(str(os.path.abspath("Startup/" + FILE) + "\n"))
      return True


  def getPerms():
    # Needs testing
    # https://raccoon.ninja/en/dev/using-python-to-check-if-the-application-is-running-as-an-administrator/
    try:
      is_admin = (os.getuid() == 0)
    except AttributeError:
      is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    with open(diagnosticFile, "w+") as file:
      if is_admin:
        file.write("Permissions: Admin")
      else:
       file.write("Permissions: User")
    return True


  def getInternetInfo():
    # Needs testing
    with open(diagnosticFile, "w+") as file:
      file.write("IP: " + IP.text)
      return True
    
    
  def getDrivers():
    # NEEDS TESTING
    with open(diagnosticFile, "w+") as file:
      for driver in wrapper.Win32_PnPSignedDriver():
        file.write(str(driver.DeviceName))
      return True

    

# Driver
with open(diagnosticFile, "w+") as file:
  functions.getProcesses()
  functions.getRuntime()
  functions.getSysInfo()
  functions.getStartup()
  functions.getPerms()    
  functions.getInternetInfo()
  functions.getDrivers()
  file.close()
    
