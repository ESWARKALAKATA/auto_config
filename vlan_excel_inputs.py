from openpyxl import load_workbook
wb = load_workbook("user_input.xlsx")
sheet = wb['vlan']
sheet1 = wb['port-channel']
sheet2 = wb['vrrp']

#vlan block
vlan_list = []
temp = 1

def main_vlan():
    global temp
    global vlan_list
    user_vlan_selction =  int(sheet['B'+str(temp)].value)
    temp = temp + 1
    for i in range (1,user_vlan_selction+1):
        vlan()

def vlan():
    global vlan_list
    global temp
    user_vlan = int(sheet['B'+str(temp)].value)
    temp = temp+1

    vlan_list.append(user_vlan)
   
    print("vlan  %d"%(user_vlan))
    user_ip = str(sheet['B'+str(temp)].value)
    temp = temp+1
    print("interface vlan %d"%(user_vlan))
    print("ip address %s"%(user_ip))
    vlan_name = str(sheet['B'+str(temp)].value)
    temp = temp+1
    print('description "%s" '%(vlan_name))
    print("!")
    

#port channel


lemp = 1
def port_channeling_required():
    global lemp
    if str(sheet1['B'+str(lemp)].value) == "yes":
        lemp = lemp+1
        user_input_name = int(sheet1['B'+str(lemp)].value) 
        lemp = lemp+1
        for i in range(1,user_input_name+1):
            port(i)
        
   
def port(i):
    global lemp
    print('interface port-channel %d'%i)
    user_vlan_per = str(sheet1['B'+str(lemp)].value)
    print("switchport trunk allowed vlan %s"% user_vlan_per)
    lemp =lemp+1

    user_port_selection = str(sheet1['B'+str(lemp)].value)
    lemp = lemp+1
    port1,port2 = user_port_selection.split(",")
    print("interface gigabitethernet %s"%port1)
    print("lacp group %d mode active"%i)
    print("!")
    print("interface gigabitethernet %s"%port2)
    print("lacp group %d mode active"%i)
    print("!")  
 
    
    '''
    make it to prited later
    accepted_list = []
    for k in range vlan_list:
        if k == (user_vlan_per.split(",")):
            accepted_list.append(k)
            print("switchport trunk allowed vlan ,accepted_list)
        else:
            "vlan error"
    print("switchport trunk allowed vlan",end=" " ) #is this value print by what vlans selected port channel
    print(  *vlan_list, sep = ", ")
    '''

#vrrp

def vrrp_main():
    VRRP_instance_number = int(sheet2['B1'].value)
    print("vrrp %d"%VRRP_instance_number)
    master_redundancy_password = str((sheet2['B2'].value))
    print("authentication %s"%master_redundancy_password)
    VRRP_IP_address = str((sheet2['B5'].value))
    print("ip address %s"%VRRP_IP_address)
    VRRP_instance_name = str((sheet2['B4'].value))
    print('description "%s"'%VRRP_instance_name)
    print("!")
    print("master-vrrp %d"%VRRP_instance_number)
    peer_IP_address =  str((sheet2['B3'].value))
    print("peer-ip-address %s ipsec masterpassword"%peer_IP_address)
    print("!")


if __name__ == "__main__":
    main_vlan()
    port_channeling_required
    vrrp_main()