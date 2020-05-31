#variables amd their values which are assumed entered by user
user_input = 2
#promting user for input vap1 as 1 and vap2 as 2 and vap3 as 3
user_vap1_input = 1
user_vap2_input = 2
user_vap3_input = 3
user_input_lms_ip = "72.1.1.1"
user_radius1_host_input = " 30.1.1.1"
user_radius1_key_input =  " qwerty"
user_radius2_host_input =  "30.1.1.2"
user_radius2_key_input =   "asdfgh"
user_radius2_host_input =  "30.1.1.3"
user_radius2_key_input =   "zxcvbn"


def main():
    #user_input = int(input("please enter input to excute apgroups : "))
    if user_input == 2:
        #please enter virtual-ap print statement
        apgroup1(user_vap1_input,user_vap2_input)
        apgroup2()
    


#apgroup1
def apgroup1(user_vap1_input,user_vap2_input):
    if user_vap1_input == 1: #user_vap1_input = int(input("please enter "1" for vap1 : "))
        wlan_virtual-ap_VAP-1()
    if user_vap2_input == 2: #user_vap2_input = int(input("please enter "2" for vap2: "))
        wlan_virtual-ap_VAP-2()
    APSYS() # ap-system-profile
    MYRADIO-0() # dot11g-radio-profile
    MYRADIO-1() # dot11g-radio-profile
    TMP-1() #dot11a-traffic-mgmt-profile TMP-1

# group2
def apgroup2(): #apgroup2 has only one option why should we ask user for input
    wlan_virtual-ap_VAP-3()
    APSYS() # ap-system-profile 
    MYRADIO-0()
    MYRADIO-1()
    TMP-1()  #dot11a-traffic-mgmt-profile TMP-1

            


# virtual-aps
def wlan_virtual-ap_VAP-1():
    aaa-profile_AAA-1()
    ssid-profile_SSID1()  
    print("vap-enable")
    print("vlan 106")

def wlan_virtual-ap_VAP-2():
    aaa-profile_AAA-2()
    ssid-profile_SSID2()
    print("vap-enable")
    print("vlan 107")
    

def wlan_virtual-ap_VAP-3():
    aaa-profile_AAA-1()
    ssid-profile_SSID3()
    print("vlan 106")

def APSYS(): # system-profile
    print("syscontact "ABC")
    #user_input_lms_ip = str(input("Enter lms ip :"))
    print("lms-ip %s",user_input_lms_ip)



#aaa-profiles
def aaa-profile_AAA-1():
    INIT-R1()
    DOT1X-PF()
    FINAL-R1()
    SG-1()

def aaa-profile_AAA-2():
    INIT-R2()
    #authentication-mac MAC-2 "not mentioned discription line 57 in configuration file"
    FINAL-R2()
    SG-2()
    rfc-3576-server 2.2.2.2()

    
#aaa fun reqirements
def rfc-3576-server 2.2.2.2():
    print("aaa rfc-3576-server 2.2.2.2")


def INIT-R1():#  initial-role
    print("access-list session log-c") #user-role
def INIT-R2()
    print("captive-portal CP-SSID-2 ")
    print("access-list session log-c")

def  DOT1X-PF(): #authentication
    MAC-R1()
    DOT1X-R1()

def MAC-R1():# machine-authentication machine-default-role 
    print("access-list session allowall")#user role

def DOTIX-R1():# machine-authentication user-default-role
    print("access-list session allowall")#user role     

def FINAL-R1():  #dot1x-default-role
    print("access-list session allowall")#user role 
def FINAL-R2():
    print("access-list session ra-guard")

def SG-1(): # dot1x-server-group
    RADIUS-1()
    RADIUS-2()
    
def SG-2():
    RADIUS-2()  
#RADIUS
def RADIUS-1():
    #user_radius-1_host_input = input('enter_host_input :')
    #user_radius-2_key_input = input('enter_host_input :')
    print("host  %s", user_radius_host_input)
    print("key  %s" ,user_radius_key_input)

def RADIUS-2():
    #user_radius-2_host_input = input('enter_host_input :')
    #user_radius-2_key_input = input('enter_host_input :')
    print("host  %s", user_radius_host_input)
    print("key  %s" ,user_radius_key_input)

def RADIUS-3():
    #user_radius-3_host_input = input('enter_host_input :')
    #user_radius-3_key_input = input('enter_host_input :')
    print("host %s", user_radius_host_input)
    print("key %s" ,user_radius_key_input)



#SSID'S
def ssid-profile_SSID1():
    #call wifi 1
    essid "WIFI-1"
    opmode wpa2-aes

def ssid-profile_SSID2():
    #call wifi 2
    essid "WIFI-2"

def ssid-profile_SSID3():
    # calling wifi 3

#wlans
def MYRADIO-0():   # dot11g-radio-profile
    MYARM-0()
    MY-HT-0()
    MY-AM-0()
def MYRADIO-1():    # dot11g-radio-profile
    MY-AM-1()

def MYARM-0():   #rf arm-profile
    print("40MHz-allowed-bands None")

def MY-HT-0():  #rf ht-radio-profile
     print("ht-radio-profile")
    
def MY-AM-0(): #am-scan-profile
     print("am-scan-profile")

def MYARM-1():  #rf arm-profile
     print(" 40MHz-allowed-bands None ")

def TMP-1(): #wlan traffic-management-profile
    print("shaping-policy fair-access")

