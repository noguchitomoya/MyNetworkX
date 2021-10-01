import numpy as np


class RGB:
    def __init__(self, feature_array):

        self.joint_feature = feature_array
        self.red = None
        self.green = None
        self.blue = None
        self.color_code = None
        self.color_element_0_to_1 = None
        self.get_rgb()



    def get_rgb(self):
        red_list = list()
        blue_list = list()
        green_list = list()
        color_0_to_1 = list()
        for i in self.joint_feature:
            red = int(176 * i)
            blue = int(176 * (1 - i))
            red_list.append(red)
            blue_list.append(blue)
            green_list.append(25)
            color_0_to_1.append([red / 255, 25 / 255, blue / 255])

        self.red = red_list
        self.blue = blue_list
        self.green = green_list
        self.color_element_0_to_1 = color_0_to_1

    def get_color_code(self):
        color_code_list = list()
        for i in range(25):
            red = hex(self.red[i])[2:]
            green = hex(self.green[i])[2:]
            blue = hex(self.blue[i])[2:]
            color_code_list.append(red + green + blue)
        self.color_code = color_code_list


# feature =  np.load("joint_feature[31].npy")
# rgb = RGB(feature)
# rgb.get_rgb()
# rgb.get_color_code()
# for i in range(25):
#     print(str(i) + "   " + str(rgb.color_code[i]))
