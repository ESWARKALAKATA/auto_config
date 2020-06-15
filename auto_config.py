import sys
from time import gmtime, strftime
from openpyxl import load_workbook
from vlan_port_channeling import main_vlan 
from vlan_port_channeling import port_channeling_required
from vrrp import vrrp_main
from dhcp import dhcp_main




wb = load_workbook("user_input.xlsx")
sheet = wb['ap_group']
#variables amd their values which are assumed entered by user
#promting user for input vap1 as 1 and vap2 as 2 and vap3 as 3
user_vap_input = int(sheet['B2'].value)


def ap_main():
    user_input = int(sheet['B1'].value)
    if user_input == 1:
        print("ap-group APGROUP-1")
        apgroup1(user_vap_input)

    if user_input == 2:
        #please enter virtual_ap print statement
        print("ap-group APGROUP-1")
        apgroup1()
        apgroup2()
      
    if user_input >2 :
        print("ap-group APGROUP-1")
        apgroup1()
        apgroup2()
        for i in range (3,user_input+1):
            print("ap-group APGROUP-%d"%i)
      
    
#apgroup1
def apgroup1():
    if user_vap_input == 1: #user_vap1_input = int(input("please enter "1" for vap1 : "))
        print("   virtual-ap VAP-1")
        print("   ap-system-profile APSYS    \n!")
        wlan_virtual_ap_VAP_1()
        APSYS()

    if user_vap_input == 2: #user_vap2_input = int(input("please enter "2" for vap2: "))
        print("   virtual-ap VAP-1")
        print("   virtual-ap VAP-2")
        print("   ap-system-profile APSYS    \n!")
        wlan_virtual_ap_VAP_2()

        APSYS() # ap_system_profile
        MYRADIO_0() # dot11g_radio_profile
        MYRADIO_1() # dot11g_radio_profile
        TMP_1() #dot11a_traffic_mgmt_profile TMP_1

# group2
def apgroup2():
    print('ap-group APGROUP-2 \n   virtual-ap VAP-3 \n   dot11a-radio-profile MYRADIO-0 \n   dot11g-radio-profile MYRADIO-1 \n   ap-system-profile APSYS \n   dot11a-traffic-mgmt-profile TMP-1 \n!')
    wlan_virtual_ap_VAP_3()
    APSYS()
    MYRADIO_0()
    MYRADIO_1()
    TMP_1()  


# virtual_aps
def wlan_virtual_ap_VAP_1():
    print("wlan virtual-ap VAP-1 \n   aaa-profile AAA-1 \n   ssid-profile SSID1 \n   vap-enable \n   vlan 106 \n!")
    aaa_profile_AAA_1()
    ssid_profile_SSID1()  
  
def wlan_virtual_ap_VAP_2():
    print("wlan virtual-ap VAP-2 \n   aaa-profile AAA-2 \n   ssid-profile SSID2 \n   vap-enable \n   vlan 107 \n!")
    aaa_profile_AAA_2()
    ssid_profile_SSID2()
  
    

def wlan_virtual_ap_VAP_3():
    print('wlan virtual-ap "VAP-3" \n   aaa-profile "AAA-1" \n   ssid-profile "SSID-2" \n   vap-enable \n   vlan 106 \n!')
    aaa_profile_AAA_1()
    ssid_profile_SSID3()


def APSYS():
   lms_ip = rfc_server = str(sheet['B3'].value)
   print('ap system-profile APSYS \n   syscontact "ABC" \n   lms-ip %s \n!'%lms_ip)


#aaa_profiles
def aaa_profile_AAA_1():
    print('aaa profile AAA-1 \n   initial-role INIT-R1 \n   authentication-dot1x DOT1X-PF \n   dot1x-default-role FINAL-R1 \n   dot1x-server-group SG-1 \n!')
    INIT_R1()
    DOT1X_PF()
    FINAL_R1()
    SG_1()

def aaa_profile_AAA_2():
    rfc_server = str(sheet['B10'].value)
    print('aaa profile AAA-2 \n   initial-role INIT-R2 \n   authentication-mac MAC-2 \n   mac-default-role FINAL-R2 \n   mac-server-group SG-2 \n   rfc-3576-server %s \n!'%rfc_server)
    INIT_R2()
    MAC_2()
    FINAL_R2()
    SG_2()
    #rfc_3576_server_2_2_2_2() #is this just ah print statement

#WHAT ARE LINES RELATED TO 59 TO 64 IN CONFIGURATION FILE   ?
#aaa  reqirements
def rfc_3576_server_2_2_2_2(): #how to find this in configuration file?
    print("aaa rfc_3576_server 2.2.2.2")

def INIT_R1():
    print("user-role INIT-R1 \n access-list session log-c \n!") #user_role
def INIT_R2():
    print('user-role INIT-R2 \n captive-portal CP-SSID-2 \n access-list session log-c \n!')
    captive_portal_CP()
def captive_portal_CP():
    print('aaa authentication captive-portal CP-SSID-2 \n   default-role FINAL-R2   default-guest-role FINAL-R2 \n   server-group SG-2 \n   login-page https://abcd.php \n   welcome-page http://abcd.com \n!')


def DOT1X_PF(): 
    MAC_R1()
    DOTIX_R1()

def MAC_R1():
    print("user-role MAC-R1 \n access-list session allowall \n!")#user role

def DOTIX_R1():
    print("user-role DOT1X-R1 \n access-list session allowall \n!")#user role     

def FINAL_R1(): 
    print("user-role FINAL-R1   \n access-list session allowall \n!")#user role 
def FINAL_R2():
    print("user-role FINAL-R2   \n access-list session ra-guard \n!")
def MAC_2():
    print('aaa authentication mac MAC-2 \n!')
def SG_1():
    RADIUS_1()
    RADIUS_2()
    
def SG_2():
    RADIUS_2()  
#RADIUS

def RADIUS_1():
    rad1_server_ip = str(sheet['B4'].value)
    rad1_key = str(sheet['B5'].value)
    print('aaa authentication-server radius RADIUS-1 \n   host %s  \n   key %s \n!'%(rad1_server_ip,rad1_key))

def RADIUS_2():
    rad2_server_ip = str(sheet['B6'].value)
    rad2_key = str(sheet['B7'].value)
    print('aaa authentication-server radius RADIUS-2 \n   host %s  \n   key %s \n!'%(rad2_server_ip,rad2_key))

def RADIUS_3():
    rad3_server_ip = str(sheet['B8'].value)
    rad3_key = str(sheet['B9'].value)
    print('aaa authentication-server radius RADIUS-3 \n   host %s  \n   key %s \n!'%(rad3_server_ip,rad3_key))


#SSID'S
def ssid_profile_SSID1():
    print('wlan ssid-profile "SSID-1" \n   essid "WIFI-1" \n   opmode wpa2-aes \n!')


def ssid_profile_SSID2():
    print('wlan ssid-profile SSID-2 \n   essid "WIFI-2" \n!')

def ssid_profile_SSID3():
    print('wlan ssid-profile "SSID-3" \n   essid "WIFI-3" \n   opmode wpa2-aes \n!')


#wlans
def MYRADIO_0():   # dot11g_radio_profile
    print('rf dot11a-radio-profile MYRADIO-0 \n   arm-profile MYARM-0 \n   ht-radio-profile MY-HT-0 \n   am-scan-profile MY-AM-0 \n!')
    MYARM_0()
    MY_HT_0()
    MY_AM_0()
def MYRADIO_1():  
    print('rf dot11g-radio-profile MYRADIO-1 \n   arm-profile MYARM-1 \n!')
    MYARM_1()

def MYARM_0():   
    print('rf arm-profile MYARM-0 \n   40MHz-allowed-bands None \n!')
def MY_HT_0():  
    print("rf ht-radio-profile MY-HT-0 \n!")
    
def MY_AM_0():
    print("am_scan_prorf am-scan-profile MY-AM-0 \n!")


def MYARM_1(): 
    print("rf arm-profile MYARM-1 \n   40MHz-allowed-bands None \n! ")


def TMP_1(): 
    print("wlan traffic-management-profile TMP-1 \n   shaping-policy fair-access \n!")

actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())
file_name =  str(sheet['B11'].value)

if __name__ == "__main__":
  
    sys.stdout = open(file_name +  "-" + str(actual_time) + ".txt", "w+") #This line is to write into the file
    try:
        ap_main()
        main_vlan()
        port_channeling_required()
        vrrp_main()
        dhcp_main()
    except TypeError :
        print("excel values were not found for to write below statements") #this will written in file if you no values found


# should take care excel input even error occured that is also redirected to file
