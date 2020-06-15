#DHCP
from openpyxl import load_workbook
wb = load_workbook("user_input.xlsx")
sheet = wb['dhcp']
def dhcp_main():
    user_DHCP_reqirment = str(sheet['B1'].value)
    if user_DHCP_reqirment == "Yes":
        print("service dhcp")
        print("!")
        dhcp_network_id = str(sheet['B3'].value)
        dhcp_network_mask = str(sheet['B4'].value)
        ex_range_start_ip = str(sheet['B6'].value)
        ex_range_end_ip = str(sheet['B7'].value)
        print(f"ip dhcp excluded-address {ex_range_start_ip} {ex_range_end_ip}")
        user_pool_name = str(sheet['B2'].value)
        print("ip dhcp pool %s"%user_pool_name)
        defualt_router = str(sheet['B9'].value)
        print("default-router %s"%defualt_router)
        usr_lease_time = str(sheet['B10'].value)
        days,dump,hours,dump1,minutes,dump2,seconds,dump3 = usr_lease_time.split(" ")
        print(days,hours,minutes,seconds)
        print("!")
        print("ip dhcp pool  %s"%user_pool_name)
        print("option 60 text MYOPTION ")
        dhcp_options_43 = str(sheet['B8'].value)
        print("option 43 ip %s"%dhcp_options_43)
        print(f"network {dhcp_network_id} {dhcp_network_mask}")
        print("!")


 


