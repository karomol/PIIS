obstacle_list = [(50, 250), (750, 350), (150, 450), (200, 150), (700, 350), (400, 350),
                 (300, 500), (600, 550), (150, 350), (500, 450), (150, 100), (50, 450),
                 (750, 150), (350, 400), (400, 500), (250, 300), (200, 500), (650, 100),
                 (650, 550), (50, 100), (350, 600), (650, 450), (250, 500), (200, 300),
                 (600, 500), (450, 100), (600, 100), (250, 200), (500, 50), (400, 150),
                 (500, 200), (100, 350), (750, 250), (500, 100), (650, 300), (100, 300),
                 (400, 50), (650, 50), (250, 400), (600, 300), (50, 50), (100, 250), (600, 150),
                 (100, 500), (250, 550), (550, 100), (750, 600), (350, 150), (750, 200),
                 (300, 400), (200, 550), (300, 350), (200, 100), (650, 350), (150, 250), (300, 100),
                 (150, 550), (50, 200), (350, 250), (450, 350), (50, 500)]

graph = {0: [12], 12: [0, 19], 1: [2, 13], 2: [1, 3], 13: [1, 21], 3: [2, 4], 4: [3, 5, 14], 5: [4, 6], 14: [4, 23],
         6: [5, 15], 15: [6, 16], 8: [9], 9: [8], 10: [11, 17], 11: [10, 18], 17: [10, 18, 29], 18: [11, 17],
         19: [12, 20, 30], 21: [13, 20, 22, 31], 23: [14, 24], 16: [15], 29: [17, 28, 41], 20: [19, 21],
         30: [19, 42], 22: [21, 32], 31: [21, 32], 32: [22, 31, 33], 24: [23, 34], 34: [24, 35, 45], 25: [26, 37],
         26: [25, 27], 37: [25, 36, 47], 27: [26, 38], 38: [27, 39, 49], 28: [29, 40], 40: [28, 39, 41, 51],
         41: [29, 40, 52], 42: [30, 53], 33: [32, 43], 43: [33, 44], 35: [34, 36], 45: [34, 44, 56], 36: [35, 37, 46],
         46: [36, 47, 58], 47: [37, 46, 48, 59], 39: [38, 40, 50], 49: [38, 48, 50, 61], 50: [39, 49, 51],
         51: [40, 50, 52], 52: [41, 51, 62], 53: [42, 54, 64], 44: [43, 45], 56: [45, 57], 58: [46, 57, 59],
         48: [47, 49, 60], 59: [47, 58, 60], 60: [48, 59, 61, 69], 61: [49, 60, 70], 62: [52, 63], 54: [53, 65],
         64: [53, 65, 72], 65: [54, 64, 73], 57: [56, 58, 68], 68: [57], 69: [60, 70, 78], 70: [61, 69, 71, 79],
         63: [62], 72: [64, 73, 84], 73: [65, 72], 66: [67, 75], 67: [66], 75: [66, 74, 86], 78: [69, 77, 79],
         71: [70, 80], 79: [70, 78, 80, 92], 80: [71, 79, 81, 93], 84: [72, 96], 74: [75], 86: [75, 87], 76: [77, 90],
         77: [76, 78, 91], 90: [76, 89, 91], 91: [77, 90, 99], 92: [79, 93, 101], 81: [80, 82], 93: [80, 92],
         82: [81, 83, 94], 83: [82, 95], 94: [82, 95, 103], 95: [83, 94, 104], 96: [84, 105], 87: [86, 88],
         88: [87, 89], 89: [88, 90, 98], 98: [89, 109], 99: [91, 100, 111], 101: [92, 100, 113],
         103: [94, 102, 104, 114], 104: [95, 103, 115], 105: [96, 106, 116], 109: [98, 108, 110],
         100: [99, 101, 112], 111: [99, 110, 112, 124], 112: [100, 111, 113, 125], 113: [101, 112, 126],
         102: [103], 114: [103, 115, 129], 115: [104, 114], 106: [105, 107, 117], 116: [105, 117], 107: [106, 118],
         117: [106, 116, 118], 118: [107, 117, 119], 108: [109, 122], 122: [108, 121], 110: [109, 111, 123],
         123: [110, 124], 124: [111, 123, 125], 125: [112, 124, 126], 126: [113, 125, 127], 129: [114, 128],
         119: [118, 120], 120: [119, 121], 121: [120, 122], 127: [126, 128], 128: [127, 129]}

vertex_list = {(0, 1): 0, (2, 1): 1, (3, 1): 2, (4, 1): 3, (5, 1): 4, (6, 1): 5, (7, 1): 6, (9, 1): 7, (11, 1): 8,
               (12, 1): 9, (14, 1): 10, (15, 1): 11, (0, 2): 12, (2, 2): 13, (5, 2): 14, (7, 2): 15, (8, 2): 16,
               (14, 2): 17, (15, 2): 18, (0, 3): 19, (1, 3): 20, (2, 3): 21, (3, 3): 22, (5, 3): 23, (6, 3): 24,
               (9, 3): 25, (10, 3): 26, (11, 3): 27, (13, 3): 28, (14, 3): 29, (0, 4): 30, (2, 4): 31, (3, 4): 32,
               (4, 4): 33, (6, 4): 34, (7, 4): 35, (8, 4): 36, (9, 4): 37, (11, 4): 38, (12, 4): 39, (13, 4): 40,
               (14, 4): 41, (0, 5): 42, (4, 5): 43, (5, 5): 44, (6, 5): 45, (8, 5): 46, (9, 5): 47, (10, 5): 48,
               (11, 5): 49, (12, 5): 50, (13, 5): 51, (14, 5): 52, (0, 6): 53, (1, 6): 54, (3, 6): 55, (6, 6): 56,
               (7, 6): 57, (8, 6): 58, (9, 6): 59, (10, 6): 60, (11, 6): 61, (14, 6): 62, (15, 6): 63, (0, 7): 64,
               (1, 7): 65, (4, 7): 66, (5, 7): 67, (7, 7): 68, (10, 7): 69, (11, 7): 70, (12, 7): 71, (0, 8): 72,
               (1, 8): 73, (3, 8): 74, (4, 8): 75, (8, 8): 76, (9, 8): 77, (10, 8): 78, (11, 8): 79, (12, 8): 80,
               (13, 8): 81, (14, 8): 82, (15, 8): 83, (0, 9): 84, (2, 9): 85, (4, 9): 86, (5, 9): 87, (6, 9): 88,
               (7, 9): 89, (8, 9): 90, (9, 9): 91, (11, 9): 92, (12, 9): 93, (14, 9): 94, (15, 9): 95, (0, 10): 96,
               (3, 10): 97, (7, 10): 98, (9, 10): 99, (10, 10): 100, (11, 10): 101, (13, 10): 102, (14, 10): 103,
               (15, 10): 104, (0, 11): 105, (1, 11): 106, (2, 11): 107, (6, 11): 108, (7, 11): 109, (8, 11): 110,
               (9, 11): 111, (10, 11): 112, (11, 11): 113, (14, 11): 114, (15, 11): 115, (0, 12): 116, (1, 12): 117,
               (2, 12): 118, (3, 12): 119, (4, 12): 120, (5, 12): 121, (6, 12): 122, (8, 12): 123, (9, 12): 124,
               (10, 12): 125, (11, 12): 126, (12, 12): 127, (13, 12): 128, (14, 12): 129}


respawn_list = [(50, 150), (550, 550), (450, 300), (150, 200)]













player = 1
def getDistance():
    d = 4
def get_element_pos():
    f = 5

def GetGraph():
    return graph

enemies = 5


