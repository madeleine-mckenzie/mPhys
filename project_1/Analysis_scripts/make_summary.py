# Was using 50 previously for the radius
def get_values(gas, new, old, radius):

    new_in_rad = new[new['r'] <= radius]
    old_in_rad = old[old['r'] <= radius]
    gas_in_rad = gas[gas['r'] <= radius]

    new_count_in_rad = len(new_in_rad)+1

    new_mass = new_in_rad['mass'].sum()

    old_mass = old_in_rad['mass'].sum()

    gas_mass = gas_in_rad['mass'].sum()

    gc_mass = new_mass+old_mass

    # Velocity dispersion
    new_std = new_in_rad['v'].std()
    old_std = old_in_rad['v'].std()
    

    para_array = [gas_mass, new_mass, old_mass, gc_mass, new_std, old_std, new_count_in_rad]
    return para_array


def get_para(p_5, p_20):
    #Read in comgc.para and plum.para
    plum_para = []
    comgc_para = []

    with open('plum.para', 'r') as plum:

        for line in plum:
            # Lines of parameters - 0th element is the number
            row = line.split()
            if(len(row)>0):
                plum_para.append(row[0])



    with open('comgc.para', 'r') as comgc:

        for line in comgc:
            row = line.split()
            if(len(row)>0):
                comgc_para.append(row[0])



    f= open("para_v2.csv","w+")
    # Header for the output file
    f.write('Dwarf mass,Dwarf size,GC mass,GC size,HI hole,Rot E,theta,phi,G mass in 5,NS mass in 5,OS mass in 5,GC mass in 5,NS vel disp in 5,OS vel disp in 5,NS cnt in 5,G mass in 20,NS mass in 20,OS mass in 20,GC mass in 20,NS vel disp in 20,OS vel disp in 20,NS cnt in 20\n')
    f.write(str(comgc_para[0])+', '+str(comgc_para[1])+', '+str(comgc_para[2])+', '+str(comgc_para[3])+', ')
    f.write(str(comgc_para[6])+', ')
    f.write(str(plum_para[1])+', '+str(plum_para[2])+', '+str(plum_para[3])+', ')
    f.write(str(p_5[0])+', '+str(p_5[1])+', '+str(p_5[2])+', '+str(p_5[3])+', '+str(p_5[4])+', '+str(p_5[5])+', '+str(p_5[6])+', ')
    f.write(str(p_20[0])+', '+str(p_20[1])+', '+str(p_20[2])+', '+str(p_20[3])+', '+str(p_20[4])+', '+str(p_20[5])+', '+str(p_20[6]))
    f.close()


def write_rotation(GC_x,GC_y,GC_z,NS_x,NS_y,NS_z):
    f= open("rotation.csv","w+")
    f.write('GC_x,GC_y,GC_z,NS_x,NS_y,NS_z\n')
    f.write(str(GC_x)+', '+str(GC_y)+', '+str(GC_z)+', '+str(NS_x)+', '+str(NS_y)+', '+str(NS_z))
    f.close