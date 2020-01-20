import json
from colortools import ciede2000
from colortools import colortools
#from solver_core import jbrik_cube


# https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
# raspistill -q 100 -e png -t 1 -sh 100 -br 60 -o /tmp/rubiks-side-U.png
# raspistill -v -w 400 -h 400  -e png -t 1 -sh 100 -br 50 -mm spot -o /tmp/jbrik/rubiks-side-R.png

#https://www.speedsolving.com/threads/rubiks-color-resolver-convert-rgb-values-of-each-square-to-u-l-f-r-b-or-d.64053/
#https://github.com/cs0x7f/min2phase/issues/7
# https://python-colormath.readthedocs.io/en/latest/delta_e.html

knowncolors = {
    "Red": [185,0,0],
    "Orange": [255,89,0],
    "Yellow": [255,255,0],
    "Green": [0, 155, 72],
    "Blue": [0, 69, 173],
    "White": [255,255,255]
}

testcolors = {
# {"1": [253, 254, 253],
    # "2": [254, 255, 254],
    # "3": [254, 255, 254],
    # "4": [254, 255, 254],
    # "5": [199, 194, 221],
    # "6": [254, 255, 254],
    # "7": [254, 254, 254],
    # "8": [254, 255, 254],
    # "9": [254, 255, 254]}

    (199, 194, 221): "1 yellow",
}



def map_rgb_to_rowcells(jsonin):
    mappedcolors = {}
    count = 1
    for i in range (1, 19):
        for j in range (1,4):
            if count <= jsonin.__len__():
                key = i.__str__() + "." + j.__str__()
                #print key
                mappedcolors[key] = jsonin[count.__str__()]
                count += 1

    return mappedcolors

#print(mappedcolors)

def convert_mapped_rowcells_to_cubestatestr(mappedcolors):
    results = {}
    for rowcell in mappedcolors:
        color = colortools.find_closest_lab_color(mappedcolors[rowcell])
        results[rowcell] = color

    cstr = ""
    for i in range (1, 19):
        for j in range (1,4):
            key = i.__str__() + "." + j.__str__()
            if results.__contains__(key):
                print(key + " " + results[key])
                if results[key] == "White":
                    cstr += "w"
                if results[key] == "Green":
                    cstr += "g"
                if results[key] == "Yellow":
                    cstr += "y"
                if results[key] == "Blue":
                    cstr += "b"
                if results[key] == "Red":
                    cstr += "r"
                if results[key] == "Orange":
                    cstr += "o"

    return cstr

#mappedcolors = map_rgb_to_rowcells(jsonstr)
#print convert_mapped_rowcells_to_cubestatestr(mappedcolors)

#lowestcolorname = colortools.find_closest_lab_color([83, 195, 92])
#print("Closest match to: " + lowestcolorname)




facerotcolormap = {
    # face 1
#    0: '{"1": [113, 19, 32], "2": [114, 4, 19], "3": [149, 72, 87], "4": [198, 211, 88], "5": [192, 198, 190], "6": [104, 196, 120], "7": [217, 59, 73], "8": [4, 94, 135], "9": [195, 205, 196]}',
#    1: '{"1": [248, 79, 111], "2": [87, 81, 53], "3": [230, 243, 125], "4": [13, 138, 184], "5": [136, 144, 142], "6": [219, 229, 226], "7": [209, 220, 216], "8": [76, 199, 97], "9": [74, 201, 96]}',
#    2: '{"1": [185, 200, 201], "2": [0, 100, 152], "3": [237, 108, 131], "4": [52, 171, 72], "5": [190, 204, 201], "6": [218, 231, 142], "7": [101, 15, 28], "8": [116, 20, 37], "9": [136, 51, 65]}',
#    3: '{"1": [140, 43, 64], "2": [101, 202, 122], "3": [215, 225, 223], "4": [136, 29, 51], "5": [207, 216, 214], "6": [48, 147, 187], "7": [124, 11, 29], "8": [215, 226, 94], "9": [241, 77, 101]}'

    # face 2
#    0: '{"1": [231, 232, 130], "2": [247, 75, 107], "3": [248, 97, 128], "4": [32, 116, 174], "5": [248, 82, 111], "6": [231, 235, 137], "7": [215, 213, 212], "8": [240, 75, 97], "9": [217, 212, 213]}',
#    1: '{"1": [224, 218, 220], "2": [9, 111, 176], "3": [233, 236, 147], "4": [243, 95, 119], "5": [245, 85, 111], "6": [246, 84, 110], "7": [215, 213, 215], "8": [225, 229, 128], "9": [238, 77, 100]}',
#    2: '{"1": [223, 216, 218], "2": [247, 78, 108], "3": [229, 224, 225], "4": [228, 231, 134], "5": [249, 92, 119], "6": [21, 116, 181], "7": [235, 77, 98], "8": [240, 78, 101], "9": [225, 229, 129]}',
#    3: '{"1": [242, 76, 108], "2": [230, 232, 134], "3": [227, 220, 225], "4": [240, 88, 113], "5": [244, 85, 114], "6": [245, 77, 107], "7": [221, 226, 128], "8": [19, 105, 170], "9": [215, 211, 213]}'

    # face 3
#    0: '{"1": [20, 117, 173], "2": [228, 222, 219], "3": [50, 135, 189], "4": [103, 198, 105], "5": [240, 239, 151], "6": [19, 118, 179], "7": [15, 110, 173], "8": [13, 110, 173], "9": [85, 192, 85]}',
#    1: '{"1": [6, 101, 163], "2": [71, 187, 72], "3": [42, 122, 177], "4": [26, 112, 169], "5": [229, 232, 125], "6": [221, 215, 212], "7": [71, 180, 73], "8": [9, 100, 161], "9": [14, 99, 159]}',
#    2: '{"1": [102, 192, 99], "2": [4, 103, 166], "3": [41, 120, 178], "4": [33, 116, 170], "5": [229, 231, 125], "6": [82, 188, 77], "7": [17, 102, 161], "8": [215, 210, 208], "9": [17, 100, 160]}',
#    3: '{"1": [16, 108, 171], "2": [3, 104, 168], "3": [106, 199, 112], "4": [218, 217, 217], "5": [231, 235, 142], "6": [15, 110, 173], "7": [13, 103, 166], "8": [70, 184, 76], "9": [10, 103, 167]}'

    # face 4
#    0: '{"1": [239, 234, 132], "2": [240, 236, 135], "3": [252, 102, 134], "4": [239, 236, 147], "5": [173, 29, 56], "6": [96, 197, 90], "7": [226, 220, 219], "8": [229, 221, 220], "9": [236, 234, 131]}',
#    1: '{"1": [217, 206, 207], "2": [226, 223, 104], "3": [229, 226, 124], "4": [218, 210, 211], "5": [183, 87, 119], "6": [226, 223, 105], "7": [217, 220, 104], "8": [62, 174, 64], "9": [236, 56, 81]}',
#    2: '{"1": [228, 225, 104], "2": [223, 211, 213], "3": [227, 215, 217], "4": [85, 185, 84], "5": [164, 36, 64], "6": [231, 228, 107], "7": [237, 67, 88], "8": [226, 225, 105], "9": [225, 223, 100]}',
#    3: '{"1": [232, 62, 78], "2": [54, 169, 54], "3": [222, 221, 111], "4": [219, 219, 103], "5": [141, 7, 28], "6": [215, 204, 205], "7": [212, 214, 95], "8": [214, 213, 91], "9": [209, 198, 199]}',

    # face 5
#    0: '{"1": [94, 191, 89], "2": [159, 10, 33], "3": [243, 239, 165], "4": [248, 115, 133], "5": [113, 206, 149], "6": [166, 24, 43], "7": [83, 187, 94], "8": [78, 189, 93], "9": [246, 98, 114]}',
#    1: '{"1": [86, 193, 82], "2": [250, 94, 116], "3": [114, 201, 116], "4": [101, 199, 107], "5": [104, 204, 124], "6": [165, 21, 42], "7": [244, 97, 116], "8": [155, 13, 32], "9": [233, 234, 139]}',
#    2: '{"1": [250, 71, 106], "2": [96, 196, 87], "3": [131, 205, 123], "4": [173, 36, 60], "5": [138, 213, 153], "6": [252, 83, 118], "7": [237, 234, 135], "8": [162, 8, 32], "9": [94, 193, 89]}',
#    3: '{"1": [235, 234, 144], "2": [155, 13, 33], "3": [251, 119, 148], "4": [165, 51, 71], "5": [123, 212, 164], "6": [85, 194, 102], "7": [80, 188, 98], "8": [244, 104, 118], "9": [79, 190, 98]}',

    # face 6
    0: '{"1": [157, 9, 34], "2": [253, 109, 138], "3": [99, 195, 104], "4": [231, 224, 228], "5": [17, 116, 187], "6": [157, 16, 39], "7": [151, 23, 42], "8": [224, 218, 222], "9": [14, 105, 175]}',
    1: '{"1": [153, 7, 33], "2": [233, 225, 228], "3": [164, 33, 61], "4": [231, 224, 227], "5": [19, 117, 184], "6": [249, 86, 115], "7": [21, 112, 180], "8": [154, 8, 31], "9": [84, 188, 88]}',
    2: '{"1": [14, 114, 181], "2": [235, 224, 227], "3": [170, 45, 74], "4": [168, 26, 54], "5": [30, 123, 187], "6": [234, 224, 227], "7": [93, 194, 97], "8": [250, 81, 112], "9": [157, 11, 35]}',
    3: '{"1": [89, 191, 86], "2": [156, 5, 32], "3": [54, 132, 192], "4": [248, 99, 124], "5": [31, 126, 190], "6": [234, 223, 224], "7": [151, 19, 38], "8": [227, 218, 219], "9": [156, 13, 35]}',
}
facerotpos = {
    1:3,
    2:6,
    3:9,
    4:2,
    5:5,
    6:8,
    7:1,
    8:4,
    9:7
}


def get_destpos_for_rotcount(startpos, rotcount):
    for i in range(1, rotcount+1):
        dest = facerotpos[startpos]
        startpos = dest

    return dest

def adjust_facevals_for_rotation(jsonin, rotcount):
    result = {}
    #jsonin = json.loads(facevals[1])
    for start in jsonin:
        endpos = get_destpos_for_rotcount(int(start), rotcount)
        result[int(start)] = jsonin[endpos.__str__()]
        #result[endpos] = jsonin[start.__str__()]

    return result

def adjust_facevals_for_all_rotations(facecolormap, rotcount):
    adjrotface = {}
    adjrotface[0] = facecolormap[0]

    for i in range(1, rotcount + 1):
        jsonin = json.loads(facecolormap[i])
        # convert to jcon here
        str = json.dumps(adjust_facevals_for_rotation(jsonin, i))
        adjrotface[i] = str
    return adjrotface




rotcount = 3
adjfacemap = adjust_facevals_for_all_rotations(facerotcolormap, rotcount)
for res in adjfacemap:
    print(res.__str__() + " " + adjfacemap[res].__str__())


bestapproxcolor = colortools.map_to_lowest_average_lab_color_distance_for_rowcell(adjfacemap)

print
for tile in bestapproxcolor:
    print(tile.__str__() + " " + bestapproxcolor[tile])
