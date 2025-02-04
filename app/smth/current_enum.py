from enum import Enum

class Current(Enum):
    CA_KERN = 'kern_ca_temp'
    CA_SD = 'sd_ca_temp'

curr_lst = ['kern_ca_temp', 'new_ca_kern_trial', 'sd_ca_temp']