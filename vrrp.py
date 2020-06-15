from openpyxl import load_workbook
wb = load_workbook("user_input.xlsx")
sheet2 = wb['vrrp']
#vlan block

def vrrp_main():
    VRRP_instance_number = int(sheet2['B1'].value)
    if VRRP_instance_number <= 4000:
        print("vrrp %d"%VRRP_instance_number)
    else:
        print("VRRP_instance_number you have entered was invalid it must be less than 1000")
    master_redundancy_password = str((sheet2['B2'].value))
    print("authentication %s"%master_redundancy_password)
    VRRP_IP_address = str((sheet2['B5'].value))
    a,b,c,d = VRRP_IP_address.split(".")
    if ((int(a) < 1000) & (int(b) < 1000) & (int(c) < 1000) & (int(d) < 1000)):
        print("ip address %s"%VRRP_IP_address)
    else:
        print("VRRP_IP_address you have entered was invalid")
    VRRP_instance_name = str((sheet2['B4'].value))
    print('description "%s"'%VRRP_instance_name)
    print("!")
    print("master-vrrp %d"%VRRP_instance_number)
    peer_IP_address =  str((sheet2['B3'].value))
    e,f,g,h =  peer_IP_address.split(".")
    if ((int(e) < 1000) & (int(f) < 1000) & (int(g) < 1000) & (int(h) < 1000)):
        print("peer-ip-address %s ipsec masterpassword"%peer_IP_address)
    else:
        print(" peer_IP_address you have entered was invalid")
    print("!")

'''
try:
    vrrp_main()
except TypeError:
    print("some of vrrp values was not mentioned in user_inputs file")

'''