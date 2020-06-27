class UserCode:
    def __init__(self):
        # TODO: tune gains
        self.Kp = 2.7
        self.Kd = 4.6
        self.x_prev = 0
            
    def compute_control_command(self, t, dt, x_measured, x_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to compute_control_command
        :param x_measured: measured position (scalar)
        :param x_desired: desired position (scalar)
        :return - control command u
        '''
        # TODO: implement PD controller
        v = (x_measured - self.x_prev) / dt if t!=0 and dt != 0 else 0 
        self.x_prev = x_measured
        u = self.Kp * (x_desired - x_measured) + self.Kd * (-v)
                
        return u
