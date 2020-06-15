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
    if user_vlan_selction < 6 :
        for i in range (1,user_vlan_selction+1):
            vlan()
    else:
        print("%d vlans were not allowed please enter below 6"%user_vlan_selction)

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
    accepted_list = []
    print('interface port-channel %d'%i)
    user_vlan_per = str(sheet1['B'+str(lemp)].value) 
    user_vlan_list = user_vlan_per.split(",")
    def check_vlan(i):
        for k in vlan_list:
            if i == k:
                accepted_list.append(i)
    i = 0
    while(i < len(user_vlan_list)):
        check_vlan(int(user_vlan_list[i]))
        i = i+1
    print("switchport trunk allowed vlan ",*accepted_list, sep = ", " ) #This valns are olny which selected in vlan section
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

