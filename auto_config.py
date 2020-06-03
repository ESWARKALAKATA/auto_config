'''
pending : 
apgroup3 neeed to update 
need to add print stateent at every function call by checking configuration file
taking input from excel
'''
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
user_radius3_host_input =  "30.1.1.3"
user_radius3_key_input =   "zxcvbn"


def main():
    user_input = int(input("please enter input to excute apgroups : "))
    if user_input == 1:
        apgroup1(user_vap1_input,user_vap2_input)

    if user_input == 2:
        #please enter virtual_ap print statement
        apgroup1(user_vap1_input,user_vap2_input)
        apgroup2()
    
    if user_input == 3:
        apgroup1(user_vap1_input,user_vap2_input)
        apgroup2()
        apgroup3()
    
        


#apgroup1
def apgroup1(user_vap1_input,user_vap2_input):
    if user_vap1_input == 1: #user_vap1_input = int(input("please enter "1" for vap1 : "))
        wlan_virtual_ap_VAP_1()
    if user_vap2_input == 2: #user_vap2_input = int(input("please enter "2" for vap2: "))
        wlan_virtual_ap_VAP_2()
    APSYS() # ap_system_profile
    MYRADIO_0() # dot11g_radio_profile
    MYRADIO_1() # dot11g_radio_profile
    TMP_1() #dot11a_traffic_mgmt_profile TMP_1

# group2
def apgroup2():
    #apgroup2 has only one option why should we ask user for input
    wlan_virtual_ap_VAP_3()
    APSYS() # ap_system_profile 
    MYRADIO_0()
    MYRADIO_1()
    TMP_1()  #dot11a_traffic_mgmt_profile TMP_1

# group3
def apgroup3():
    print("still this block is pending neeed to update")
    


# virtual_aps
def wlan_virtual_ap_VAP_1():
    aaa_profile_AAA_1()
    ssid_profile_SSID1()  
    print("vap_enable")
    print("vlan 106")

def wlan_virtual_ap_VAP_2():
    aaa_profile_AAA_2()
    ssid_profile_SSID2()
    print("vap_enable")
    print("vlan 107")
    

def wlan_virtual_ap_VAP_3():
    aaa_profile_AAA_1()
    ssid_profile_SSID3()
    print("vlan 106")

def APSYS(): # system_profile
    print("syscontact : ABC")
    #user_input_lms_ip = str(input("Enter lms ip :"))
    print("lms_ip %s",user_input_lms_ip)



#aaa_profiles
def aaa_profile_AAA_1():
    INIT_R1()
    DOT1X_PF()
    FINAL_R1()
    SG_1()

def aaa_profile_AAA_2():
    INIT_R2()
    #authentication_mac MAC_2 "not mentioned discription line 57 in configuration file"
    FINAL_R2()
    SG_2()
    rfc_3576_server_2_2_2_2()

    
#aaa fun reqirements
def rfc_3576_server_2_2_2_2():
    print("aaa rfc_3576_server 2.2.2.2")


def INIT_R1():#  initial_role
    print("access_list session log_c") #user_role
def INIT_R2():
    print("captive_portal CP_SSID_2 ")
    print("access_list session log_c")

def  DOT1X_PF(): #authentication
    MAC_R1()
    DOTIX_R1()

def MAC_R1():# machine_authentication machine_default_role 
    print("access_list session allowall")#user role

def DOTIX_R1():# machine_authentication user_default_role
    print("access_list session allowall")#user role     

def FINAL_R1():  #dot1x_default_role
    print("access_list session allowall")#user role 
def FINAL_R2():
    print("access_list session ra_guard")

def SG_1(): # dot1x_server_group
    RADIUS_1()
    RADIUS_2()
    
def SG_2():
    RADIUS_2()  
#RADIUS
def RADIUS_1():
    #user_radius_1_host_input = input('enter_host_input :')
    #user_radius_2_key_input = input('enter_host_input :')
    print("host  %s", user_radius1_host_input)
    print("key  %s" ,user_radius1_key_input)

def RADIUS_2():
    #user_radius_2_host_input = input('enter_host_input :')
    #user_radius_2_key_input = input('enter_host_input :')
    print("host  %s", user_radius2_host_input)
    print("key  %s" ,user_radius2_key_input)

def RADIUS_3():
    #user_radius_3_host_input = input('enter_host_input :')
    #user_radius_3_key_input = input('enter_host_input :')
    print("host %s", user_radius3_host_input)
    print("key %s" ,user_radius3_key_input)



#SSID'S
def ssid_profile_SSID1():
    #call wifi 1
    print("essid WIFI_1")
    #opmode wpa2_aes

def ssid_profile_SSID2():
    #call wifi 2
    print("essid WIFI_2")

def ssid_profile_SSID3():
    print("essid WIFI_3")
    # calling wifi 3

#wlans
def MYRADIO_0():   # dot11g_radio_profile
    MYARM_0()
    MY_HT_0()
    MY_AM_0()
def MYRADIO_1():    # dot11g_radio_profile
    MYARM_1()

def MYARM_0():   #rf arm_profile
    print("40MHz_allowed_bands None")

def MY_HT_0():  #rf ht_radio_profile
     print("ht_radio_profile")
    
def MY_AM_0(): #am_scan_profile
     print("am_scan_profile")

def MYARM_1():  #rf arm_profile
     print(" 40MHz_allowed_bands None ")

def TMP_1(): #wlan traffic_management_profile
    print("shaping_policy fair_access")

#vlan

def vlan():
    vlan_num = int(input("Enter 1st vlan number : "))
    vlan_num = int(input("Enter 2nd vlan number : "))
    vlan_num = int(input("Enter 3rd vlan number : "))
    vlan_num = int(input("Enter 4rd vlan number : "))




if __name__ == "__main__":
    main()