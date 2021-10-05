import numpy as np


class RGB:
    def __init__(self, feature_array):

        self.joint_feature = feature_array
        self.gain = 10
        self.offset_x = 0.2
        self.offset_green = 0.6
        self.red = None
        self.green = None
        self.blue = None
        self.color_code = None
        self.color_element_0_to_1 = None
        self.get_rgb()

    def sigmoid(self, x, gain=1, offset_x=0):
        return ((np.tanh(((x + offset_x) * gain) / 2) + 1) / 2)

    def colorBarRGB(self, x):
        # if x <= 0.485:
        #     x = x / 0.50
        # elif x >= 0.515 and x * 1.50 <= 1.0:
        #     x = x * 1.50

        x = (x * 2) - 1
        red = self.sigmoid(x, self.gain, -1 * self.offset_x)
        blue = 1 - self.sigmoid(x, self.gain, self.offset_x)
        green = self.sigmoid(x, self.gain, self.offset_green) + (1 - self.sigmoid(x, self.gain, -1 * self.offset_green))
        green = (green - 1.0)

    # green = (green - 1.0)/2.0
        return (red, green, blue)


    def get_rgb(self):
        red_list = list()
        blue_list = list()
        green_list = list()
        color_0_to_1 = list()
        for i in self.joint_feature:
            tmp = self.colorBarRGB(i)
            red = int(255 * tmp[0])
            blue = int(255 * tmp[2])
            green = int(255 * tmp[1])
            # red = int(176 * i)
            # blue = int(176 * (1 - i))

            red_list.append(red)
            blue_list.append(blue)
            green_list.append(green)
            color_0_to_1.append([red / 255, green / 255, blue / 255])
            # color_0_to_1.append([red / 255, 25 / 255, blue / 255])

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
