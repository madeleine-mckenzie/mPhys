class ToutTimeStep:

    def __init__(self):
        self.gal = []
        self.gas = []
        self.new = []
        self.old = []

    def append_gal(self, arr):
        self.gal.append(arr)

    def append_gas(self, arr):
        self.gas.append(arr)

    def append_new(self, arr):
        self.new.append(arr)

    def append_old(self, arr):
        self.old.append(arr)
    
    def get_gal(self):
        return self.gal
    
    def get_gas(self):
        return self.gas
    
    def get_new(self):
        return self.new
    
    def get_old(self):
        return self.old

    def set_all(self, gal_arr, gas_arr, new_arr, old_arr):
        self.gal = gal_arr
        self.gas = gas_arr
        self.new = new_arr
        self.old = old_arr



class ToutData():
    def __init__(self):
        self.timestep = []

    def append_timestep(self, timestep):
        self.timestep.append(timestep)
    
    def get_timestep_i(self, i):
        return self.timestep[i]
    
    def get_timestep(self):
        return self.timestep

    def get_shape(self):
        return len(self.timestep)
 
