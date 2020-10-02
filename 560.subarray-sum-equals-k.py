from typing import *

#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        acc = 0
        ht = {0: 1}
        for x in nums:
            acc += x
            if acc - k in ht:
                count += ht[acc - k]
            ht[acc] = ht[acc] + 1 if acc in ht else 1
        return count

    def v1(self, nums, k):
        # F[n] = { ...F[n-1][i]+A[j] }
        count = 0
        dp = {}
        for a in nums:
            dp[0] = dp[0] + 1 if 0 in dp else 1
            dp, copy = {}, dp
            for b in copy:
                if a + b in dp:
                    dp[a + b] = copy[b] + dp[a + b]
                else:
                    dp[a + b] = copy[b] + 0
            count += dp[k] if k in dp else 0
        return count


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().subarraySum([], 0))
    print(1 == Solution().subarraySum([0], 0))
    print(0 == Solution().subarraySum([0], 1))
    print(4 == Solution().subarraySum([1, -1, 1, 2, -2], 0))
    print(0 == Solution().subarraySum([1, 1, 1], 0))
    print(3 == Solution().subarraySum([1, 1, 1], 1))
    print(2 == Solution().subarraySum([1, 1, 1], 2))
    # fmt: off
    print(7 == Solution().subarraySum([1, 1, 1, 2, 6, 4, 4, 2, 3, 3, 2, 4, 5, 2, 4, 2, 2, 2, 2, 1, 1], 10))
    print(512 == Solution().subarraySum([-916, -132, -202, -524, 739, 57, 938, 546, 948, -181, -315, 921, 792, -992, -69, 588, 712, 509, -406, 302, -637, 169, 407, 993, -263, 54, -512, -950, -930, 66, 147, -9, -136, -205, 274, 992, -304, -835, 659, -792, -288, 146, 182, -672, -374, -943, -85, 958, -19, 33, -676, 232, 92, -132, -121, -944, -526, -869, -423, -855, 818, 46, 401, 633, -457, 63, 824, -172, 237, 360, 43, 831, -432, 213, -330, -788, -472, -70, -507, 615, -953, 457, -89, -756, 477, 445, 153, -779, 710, 484, -20, 802, -261, -481, -309, -992, -240, 275, -302, -137, 295, -232, 529, 691, 873, 787, 229, 677, -388, 996, 301, -641, -983, 108, -247, 431, -668, 877, 528, -69, -15, 278, -334, 775, 770, -720, 232, -607, 896, 496, 485, 350, 772, -656, 379, 730, -445, -152, 295, 99, -945, -170, -594, 271, 894, -451, -455, 636, -210, 674, 554, 183, 446, -709, -599, 521, 711, -739, -712, -947, -940, -577, 71, 672, -512, -216, 669, 137, -61, -901, -867, -168, -838, -653, -503, -535, -423, -922, 281, 544, -373, -935, -485, 760, -203, -656, -241, 493, -290, -298, 756, -871, -525, 614, 230, -910, -395, -308, -237, 289, 975, -215, 542, 674, 798, 95, -989, 912, -943, -262, -501, -670, -878, -40, 983, 963, -136, 682, -383, -537, -724, 382, -831, 726, 91, 666, -795, 308, -519, -891, -313, 960, -785, -629, 519, 783, -2, 705, -658, 993, 656, 795, 441, 145, -298, 411, -593, -738, -701, -453, 857, 769, -841, -609, 248, -315, -465, -2, 93, 748, -75, -227, -426, -446, 428, 54, 324, -72, -340, -361, -327, 204, 991, -720, -861, -33, -517, 454, 241, -34, -750, -31, -476, -428, 909, -221, -981, 168, 352, -443, -733, 821, -287, 395, 691, -230, 45, -752, -524, -998, -245, -947, 560, 308, -144, 223, -802, 844, -321, 194, -666, -960, -920, -668, 989, -735, -566, -298, 652, 215, 916, 862, 261, -894, -984, 124, 348, -858, -571, 585, 681, -197, 387, -308, -349, -555, -530, 993, 464, -285, -195, -786, 777, -819, -45, -792, 200, 994, 82, 832, -70, -578, -244, -546, -866, -746, 563, -359, -857, -610, -518, -902, -746, 540, -721, 184, -523, -64, 466, -166, 719, -76, 937, -150, -55, 849, -42, -403, -492, -24, -850, -448, -460, 167, 596, -799, 523, -699, 975, 104, 658, -274, 462, 618, -320, -330, -639, -541, -218, -627, -303, -504, 781, -564, 967, -635, -523, -918, -529, 705, 624, -196, 814, -165, 142, -103, 935, 573, 45, -377, 661, -521, 691, -81, -496, -883, 995, 227, 592, 606, -756, 183, -486, -767, -68, 648, 666, -134, 977, 617, -545, 735, -502, -730, 779, -744, -123, -495, -848, 937, -227, -470, 401, -909, -135, 884, 484, 326, -910, 953, -321, 352, 134, -683, 855, 199, -966, -900, 290, -575, -194, 828, 743, -762, -846, 530, -603, 679, 132, 380, -596, 110, -678, 842, 505, -925, 993, -765, 374, -694, -346, 656, -332, -131, -846, -196, 34, 408, -612, -701, 316, -803, -123, -417, 887, 823, -696, 850, 762, -231, -863, -758, -782, -504, 670, 164, -878, -260, 561, -448, 37, 660, -776, 787, 782, -712, 31, -106, 485, -345, -802, -512, -305, 776, 796, 788, -575, -577, -268, 38, 356, -221, 649, 378, -128, -779, 317, 313, 673, -494, -126, 92, 910, -343, 675, 857, -850, -322, -607, 318, -694, 523, -880, -800, 936, 204, -275, -822, -528, 928, -242, -420, -769, 39, 982, -373, 517, 332, -459, -408, -125, -15, 304, 56, 777, -52, 496, -610, -877, -308, -876, -148, 266, -441, -341, -489, -214, 276, 27, -413, -534, -805, -607, -808, -568, 73, 532, 732, 689, -653, -489, -198, 383, 851, 452, -47, -987, -549, 379, -693, -921, -428, -261, 707, 777, -969, 728, -868, 341, 803, -593, 241, 122, 551, -523, -189, 461, -447, 130, 242, -71, 582, -86, 16, 110, 579, -519, -434, -904, 27, -359, 986, 955, 783, -195, -911, -29, 744, -390, 808, -666, -24, 962, 114, 873, 473, 162, 73, -366, 975, -207, 419, 225, -809, 656, -85, 536, -417, 345, -940, 805, 48, 335, 967, 790, 258, -546, -179, -34, 651, 257, -111, -456, 912, 251, -639, -24, -638, 50, -536, 90, 112, 812, -504, 346, 553, -571, 830, -511, -340, -464, 566, -594, -953, 715, -697, 538, -709, 230, -949, -547, -982, -183, 238, 82, 20, -600, -16, 47, 917, 269, -895, 768, 714, 391, 104, 577, 951, 510, -226, 85, 347, -263, -8, 100, -670, 295, 788, -645, -191, 534, 856, 248, 568, 961, 820, -570, 552, -772, -892, -109, -312, -979, 631, -688, 830, -164, -942, -431, 898, -358, 907, -186, -350, 753, -199, -15, -657, -426, -382, 53, 688, -971, -245, 748, 703, -633, -232, 178, -8, -923, 225, -925, -715, -666, -264, -411, -966, -423, -330, 633, 642, 718, 690, -434, 770, 689, 902, 597, -877, 543, -358, -510, 93, 191, 588, -65, -822, -75, 857, 871, -266, -965, -577, -533, 158, -971, -993, 615, 242, 230, -580, -352, 611, -684, -280, 812, 32, -57, 651, -916, -733, -763, 112, 556, 102, -283, 855, -398, 267, 839, -527, -58, -64, -68, 303, 10, 16, 242, 241, -305, -2, 927, -41, -71, -362, 118, 61, -250, 454, -801, -479, -518, -659, 432, 577, 799, 515, -127, 237, 597, -907, -597, 912, 955, -181, -595, 455, -626, -383, 712, -742, -774, -63, -351, -680, -577, 706, 868, -306, -778, 92, 718, -746, -512, 310, -534, -868, -546, -32, 499, -15, -358, -171, 909, -151, 357, 471, -284, 928, 8, -186, 743, -230, -632, -282, -211, 274, 68, -88, -979, -12, -673, 580, -156, 250, 903, 918, -589, 492, 446, -133, 412, -445, -125, -164, -736, 112, -240, -815, -832, 991, -965, 28, -956, -879, 143, 346, 420, 8, -672, -142, -942, 347, -844, 720, -622, -473, -46, -163, -735, 734, -471, -269, -526, -911, -732, -913, 966, 64, -992, -407, -503, -648, 763, 850, -637, 628, -376, -315, -134, 476, -740, 533, -481, 504, 476, -651, 936, -750, 16, -871, -225, -750, -1, 639, 114, -862, -390, 776, -401, 667, -519, -52, 774, -143, 491, -805, -316, 469, -584, 979, -143, 535, 438, 935, -619, -191, -974, 597, -349, -682, -922, -403, 535, 109, 82, -544, 960, 397, -858, -489, 57, -544, -285, 806, 300, -753, -86, -411, 186, -652, 178, 909, -756, 712, 25, -677, 86, -156, 622, -503, 862, -127, -281, 700, 158, 474, -655, 512, 920, 917, 760, 879, -538, 384, -210, -501, -617, 300, 970, 266, 514, 293, 291, 586, -308, -24, 821, 576, 267, 32, 780, 341, 637, 914, 822, 197, 629, 456, -774, 864, 84, -179, 973, 772, -963, -579, -961, 294, -293, 846, -97, -685, -462, -183, 536, 493, 927, 871, 990, -154, -478, 300, -486, -827, 677, 796, 433, -184, 77, 745, -651, -938, -614, 193, -21, -644, 303, 283, -831, 631, 607, 66, 168, 447, 830, 28, 886, -827, -108, -70, -230, -937, 602, 206, 453, 382, -105, -997, 780, -292, 857, 794, -409, -24, -82, 408, -606, 617, -271, -7, 832, 385, 73, -786, -868, -711, 823, -10, 549, -765, 226, -792, 914, 179, -293, -122, -31, 419, 344, -401, 359, -321, 157, -865, 628, 995, -738, 731, 336, -335, 658, -337, 852, -665, 977, -302, 680, -161, -404, -146, 703, -162, 633, -234, -389, -931, 955, 807, -170, -83, -245, 736, -314, -869, -736, 970, -326, 491, -783, -182, 174, -985, -248, 25, -657, 802, -849, 929, -618, -720, 206, -316, 839, -406, 64, 54, -819, 195, 93, 985, 513, 230, -545, 969, 509, -844, 323, 667, 376, 885, -979, 561, 71, -880, 35, 657, 926, -562, 804, -940, 479, 485, -734, 976, 186, 339, 806, 65, -163, -849, -76, 968, 569, 44, 255, 868, 382, 911, 73, 16, -164, 548, -919, -344, -533, -831, 825, -856, 159, 129, -900, -116, -469, -807, -197, 198, -775, 144, 696, 842, 62, -273, 129, 847, 149, 407, -681, -831, -656, -551, 871, -329, -466, -379, -874, 780, 541, 322, 232, -332, -170, -829, -673, -833, -741, -308, 709, 701, -383, -810, -651, 69, -917, 420, 613, 494, 783, 23, -317, -143, -670, 167, -486, 459, -327, -545, -172, 135, 970, -352, -825, 661, 901, -184, -52, 128, -426, 407, -302, -612, -766, -999, 900, 645, -373, 647, -828, 704, -812, -847, 794, -525, 816, -450, -240, -400, -351, -78, 479, 771, -262, -311, 108, 197, -368, 361, -226, -428, -220, 966, 783, -374, 25, 377, -978, -593, -807, -559, -950, 876, -684, 760, 261, 590, -929, -746, -382, 834, 404, -384, 31, -168, -338, 860, 800, 850, 20, -267, -691, 998, -765, -651, -205, -354, -166, -758, -85, 543, -298, -831, 364, 4, -171, -555, -22, 940, -124, -134, -432, -70, 475, 939, 880, 336, 122, 210, -444, 968, 819, -320, -248, -830, 817, -798, 584, 389, 291, 203, 804, 838, -511, 112, 206, 340, 556, 593, 698, 449, -874, 693, 187, -78, -840, 100, 705, 569, 432, -366, -834, -440, -90, 975, 991, 809, -953, 493, 580, 550, -764, -560, 561, 248, 810, 688, -738, 946, -818, 385, 597, 400, -973, -241, -35, 63, -268, 735, 653, 240, 7, 846, 937, 534, -724, 913, 747, -891, 72, 439, -818, 519, -416, -527, 803, -112, 180, -878, 192, 225, 944, -828, -410, 966, -399, -839, -889, 345, -815, -421, -425, 958, -843, 621, -800, -646, 774, 247, 825, -624, 392, 285, -701, 414, -298, 341, -489, 302, 864, -267, -95, -170, -383, 415, -964, 718, 950, -500, 108, 526, 969, -830, -363, -739, -946, -500, -249, 910, -465, 133, 346, -303, 149, 271, 674, -474, 473, -50, 803, -179, 358, 10, 984, -92, 708, -2, -562, -596, 607, -378, -995, 829, -252, 320, 850, -574, 165, -637, 143, -240, 108, -532, 847, 812, -540, -983, -804, 903, -387, -707, -431, 376, -131, 325, -30, 507, 638, 663, 134, 125, -614, -411, 154, -564, 426, -948, -990, -28, 548, -265, -673, -212, 857, -568, -921, 422, -362, -359, -699, 879, 194, 598, -857, 225, -453, -137, -476, -712, -576, -347, 363, 835, -433, 98, -306, 94, 585, 486, -977, 195, 648, -257, 637, 143, -878, -395, 990, -983, 110, -550, 660, 776, 824, -566, -844, 531, 525, 632, -755, 77, -846, -394, 208, 130, -162, -750, 279, -490, 25, 762, 84, -579, -14, -666, -27, 540, -692, 0, 180, 306, 95, -214, 826, 333, -375, 913, 530, 293, -12, 664, -533, 932, -566, 207, -494, -667, 200, 195, -259, -966, 564, -430, 176, 20, -909, 462, 656, -470, 723, -530, -757, -331, 67, 516, 407, -790, -989, -219, 435, -473, 818, -470, -590, -71, -324, -342, -843, 743, -912, -105, -665, 432, -316, -615, -295, 87, 726, 74, 516, 145, -436, 681, -434, -601, 67, 790, -727, -915, 419, -747, 252, -764, -583, -937, 640, -373, 157, -179, 913, 719, 841, 812, -548, -197, -301, 420, 662, 357, -192, -656, -581, 611, 481, -185, -666, 192, 176, -874, -599, 685, -993, -691, 22, -815, 293, 698, -4, -7, -119, 511, -415, 700, -400, -21, 808, 687, 913, -277, -566, -881, -367, 626, 429, -821, -728, 565, -995, -446, 146, -928, 658, -807, 415, 265, -218, 984, -121, 258, 872, 851, -88, -432, -812, -267, -615, 342, 826, -4, -148, 546, 274, -415, -178, 260, 466, -960, 729, -784, 249, 689, 958, -700, -866, -970, -626, -936, -637, 469, 119, -342, 984, 242, 923, 754, -278, -583, 924, -789, -283, -216, 574, 531, -572, -873, 164, -29, -874, 475, -528, -663, 30, 23, 958, 756, -79, -38, 998, -698, 504, 948, -213, -122, 497, -396, -839, -684, -700, -689, -181, 106, -295, 538, -936, -764, -298, -264, -986, -418, -639, -714, -834, 293, 771, -711, 504, -581, 123, 805, -587, -524, -257, -197, -505, -649, -182, -344, 978, 59, 319, 508, -543, 48, -269, -517, -604, 292, 201, 973, -490, 104, -549, -914, 663, 279, -977, 842, -901, 107, -858, -201, 550, 877, -257, -608, -109, 401, -880, -339, -815, -41, 711, 733, -295, 465, 217, 84, -890, -370, -590, 350, -103, -750, -808, 424, -846, 248, 520, -768, 369, -953, 652, -202, 422, -831, -978, 334, 349, -352, -759, -615, 872, -712, -887, -286, -384, 540, -609, 755, 285, 486, -888, 241, 380, 777, 641, 897, 434, -114, -726, -720, 477, 347, 708, 26, -797, -46, -75, 608, 545, -850, -386, -112, -243, 95, -245, 565, 996, 691, -697, 28, 799, 358, 474, -402, 68, 715, 980, -168, 487, -23, 505, 368, 654, 885, 990, -526, -335, 460, 976, 270, 933, 578, 168, 626, 458, -974, 598, 991, -710, 673, 759, -838, -380, 177, 683, -831, 582, 724, 472, 454, 367, -995, 85, -110, 321, -919, 788, -625, -421, -195, -790, -790, 370, -890, 306, 379, 21, -418, 69, -374, -110, -170, -993, 849, -356, 927, -281, -452, -137, -351, 232, 67, -326, -53, 18, 164, 833, -42, -966, 950, 402, -819, 739, 551, -759, -27, 432, -152, 850, 330, 820, 426, -840, 693, -955, 993, -469, -238, -997, -334, 319, -318, -984, 113, 523, -591, 436, -870, 162, 84, 626, 494, 881, 639, -651, -439, -190, 515, 279, -503, 534, 334, 544, 219, -931, 590, 719, -237, 852, -982, -963, 860, -242, -106, -795, 897, -295, -334, -732, -289, 9, -643, 546, 748, 714, 182, 383, 180, -146, 954, 820, 564, 839, -137, 571, -169, -331, -140, -615, -93, -466, 767, -479, -144, 421, 581, -844, 134, 193, 38, 889, -418, 135, -742, 452, -104, -717, -301, 899, -465, -788, 569, -570, 676, -174, 428, 62, -342, -311, 211, 548, 344, 642, -50, -135, -976, 207, -365, 676, 272, -56, 125, 655, 746, 808, 131, -583, -55, -439, 95, 747, 599, -306, 719, -84, -525, 147, 539, -322, 996, -6, 348, 551, 486, 685, 838, 119, 545, 959, -911, -849, 124, 237, 333, 912, -554, 943, -221, -445, -912, 149, -620, 513, -336, -331, 809, -185, -906, -365, 543, -895, 690, 221, -48, 374, 898, -996, 988, 925, 554, 906, 815, -493, -823, 451, 87, 682, 862, -334, 378, 656, -372, -648, 337, -420, 563, 155, 185, 385, -269, -695, 579, -244, 390, -519, 947, 35, -366, -447, -639, 401, 515, -811, -940, 191, -430, 417, 12, -114, 316, -929, 384, -619, -947, 580, -276, -400, 180, 75, -969, -289, 187, -547, 667, -624, 471, 433, -433, 426, -749, -298, 939, -678, -730, 129, 679, -232, -219, 360, -424, 889, 441, -55, 380, -570, 117, -471, 928, 87, 231, 476, -327, -883, -883, -848, 701, -205, -405, -921, -154, 542, -946, 144, -551, -537, -328, 974, -873, -599, -691, 668, 153, 789, -813, 612, 65, 535, 935, 488, -246, 534, -519, -477, 672, 785, -89, 507, -867, -447, 350, -546, 979, 266, 349, -32, 966, 669, 750, 586, -272, -407, 604, 722, -545, 164, 863, -245, -469, 372, 507, -492, -226, -909, -83, 893, 418, 759, -697, -835, 507, 382, -779, 729, 601, 471, -685, 798, -1000, -237, 567, 913, 956, -441, -123, 682, -184, -55, 847, -197, 984, 521, -931, 268, -460, 298, 903, -571, -329, 459, -448, -9, 289, 386, -993, -282, 197, 74, 612, -377, -104, -307, 97, 303, -15, -932, -960, 800, 188, -537, -39, -739, 349, 972, -769, -164, 672, -216, -803, 181, 754, 923, 433, -757, -576, -950, -57, 783, 637, -534, 626, -220, 524, 169, -672, -743, -329, 974, -221, -595, -531, -839, -360, 249, 411, -366, -674, -62, 724, 192, -222, -613, 552, -380, 61, 427, -566, 613, 44, -91, -318, -278, -96, 226, -954, 225, 307, -909, -864, -260, -594, 209, 153, 212, -345, -597, -603, -834, -385, 254, 10, 989, -431, 434, -430, 628, -954, -25, -314, 709, -464, -19, -196, -730, -419, 737, 947, -150, -978, 17, 682, -30, -530, 118, -82, 87, 357, 52, 18, -669, 772, 692, -532, -483, -308, -701, -868, -941, 520, -160, 866, -147, 31, 980, 210, -870, 824, 31, 719, -285, 738, -267, -728, -370, -631, -633, -889, 255, -993, 169, -631, -215, -228, 530, 402, -980, -357, 424, -125, -870, 532, 341, -699, 242, 986, -470, -906, 675, -576, 398, 52, -958, 0, -688, -380, -165, -548, -575, 429, -105, -361, 298, -471, -774, 875, -749, 166, 867, -40, -605, 146, 210, -96, -791, 607, -494, -459, -675, -96, 798, -332, -207, 606, 73, 415, -23, -571, -317, -655, -6, -293, 505, 674, 526, -295, 63, 910, -304, 621, 247, -260, 549, -731, 527, 940, 141, -505, -157, 131, -857, -571, -615, 68, 418, -870, -665, 73, -615, -200, -102, -633, -24, -489, -753, -51, 153, -442, -603, 642, -357, -410, -965, -621, 460, 782, 682, -355, 104, -836, -212, 46, 200, 839, 410, -628, -87, 344, 714, -197, -378, 963, -231, -600, 299, -401, -21, 118, -881, -843, 29, -264, 596, -356, -968, 408, 450, -254, -968, 698, -631, 992, -622, 57, -927, 301, 729, -619, -794, -459, 362, 902, 867, 983, 950, 924, 175, -729, -790, 847, 625, -183, -240, -365, -99, 624, 501, 731, 269, 22, 61, -187, 422, 141, 289, -747, 113, 872, 494, 432, 170, 823, -665, -187, -825, -980, 721, 960, -23, -975, -796, -921, 102, 400, 760, 520, -585, -238, -125, -556, -397, -132, -380, 877, -703, 149, 273, -866, 470, 83, -613, 581, 925, 437, 318, -740, -546, 243, 173, 223, -983, 838, 309, -303, 356, 425, 737, 569, -489, -94, -277, -789, -923, -593, 689, -743, -352, -608, 542, 559, 339, 662, 296, 643, -285, 128, 862, 701, 642, 357, 12, -55, -398, 96, 20, 948, -205, 109, -754, -855, -836, -541, 392, -340, -817, 23, -80, 212, -532, -287, 36, 914, -594, -771, 78, -221, 703, -636, -714, 757, -147, 548, 353, 700, 693, -587, 685, 176, 790, -8, -316, -765, 312, -628, -236, 392, -181, 417, -213, 667, -578, -432, 210, -57, 545, -811, 425, 550, 153, -952, -45, 302, -761, -948, -312, -67, -121, -366, -641, -994, -680, -168, -164, -440, -930, 811, 69, -199, -363, -872, 230, -858, 533, -210, -901, 700, -177, -238, 380, -311, 758, 794, -845, 983, -930, 909, -947, 99, 182, -831, -375, -146, -336, -65, 985, 818, 91, 422, 959, 825, 194, 429, 361, -684, -937, 350, 993, -825, 817, -828, -398, 233, -392, -37, 644, 727, 615, 440, -501, 750, 622, -136, -615, -173, 861, -175, 740, 279, -812, -839, 515, 803, 7, 574, -25, -705, -147, -41, 955, -699, -188, -749, 257, 774, -812, -427, 145, 43, -33, -871, 934, 230, -796, -652, -304, -895, -892, -667, 419, -777, -201, 132, -147, 304, 791, -792, -203, 144, 721, -949, -863, 127, 342, -374, -29, -468, 977, -482, 588, -767, 403, 610, 646, -782, 757, -185, -500, -723, 382, -478, -181, 716, 670, 95, 546, -145, 428, -521, -292, 7, 36, 714, -376, 391, 560, -776, 34, 747, -135, 295, 447, 6, -948, -336, 607, -564, 366, 55, 265, 441, -930, 669, -872, 752, 29, 859, -297, -935, -279, -810, 691, -783, -882, 468, 717, -396, 885, 374, 10, 640, 63, -895, 515, -387, 897, -827, 220, 556, 453, 678, -750, 754, -442, -80, -447, -425, 52, -2, -484, 171, 551, -241, -576, 473, 35, -199, -58, 522, 654, 133, -859, -983, -70, 156, 837, 956, -852, 667, -201, -383, 857, -561, 342, -377, -689, -705, -847, 633, -698, -545, 207, 961, 384, 470, 955, -955, 201, 819, -775, -732, -282, -860, 751, -474, 248, 401, -515, -620, 628, 639, 992, -639, 908, -285, 901, -899, -503, 293, -167, -20, -20, 856, -1, 853, -401, -397, 435, 831, -984, 357, 921, -206, -4, 398, -688, -597, 767, 549, 720, 896, -657, -604, -651, -81, 580, 762, -990, -479, 838, -924, 383, -894, -902, 615, 911, 687, -504, -120, -251, -467, 614, -676, 377, -98, 707, 137, 859, 274, 635, 19, 668, -548, -705, -371, 388, 648, -484, 806, -430, 947, 405, -599, 101, 72, -452, -834, -413, -69, -516, 841, 330, 661, -70, 857, 925, 620, -776, 168, -176, 141, 284, 383, -75, 283, -93, 63, 325, 345, 354, 432, 307, 303, -271, 668, -463, -318, -615, -798, -160, 443, 139, -161, 656, -340, 86, -129, 16, -204, -272, -84, 591, 770, 22, -641, -497, -521, -964, -625, -335, 517, 879, 844, 124, 781, -635, -510, 202, 753, 924, 112, -416, -77, -244, -310, 883, 400, -533, 749, 419, 589, 995, 683, 613, -121, -614, 652, -247, 631, 3, 399, -974, 552, 581, -544, -120, -45, -720, 105, 293, 370, 678, 387, 825, 122, -635, -153, 460, -657, -452, 904, -164, -663, -203, -121, 888, 198, -715, -717, -662, 498, 952, 821, -797, -326, 560, -70, -680, -7, -726, -436, -674, -143, 268, 411, -989, -831, -959, 883, 830, -693, -366, 782, 390, 829, 193, 409, 913, -34, -455, 584, 312, 27, 218, -203, 677, 847, 172, -581, -394, -133, 229, -984, -894, -54, 148, 553, 812, -560, 48, 67, 41, 413, 772, -305, -332, -227, -731, 62, -739, -929, 918, 214, -963, 224, -397, 736, 16, -202, 335, 145, -86, -312, -731, -984, 215, -684, 958, -534, -208, 270, -988, 405, 344, 670, -24, 358, -916, -259, -570, 514, 212, 466, -758, -556, 149, 462, -120, 931, -953, -478, -557, -929, -474, 560, 297, 223, 522, -695, 477, -986, -786, -453, -270, 550, 772, 225, 784, -704, -471, -9, 323, -383, -402, -752, 227, 929, -950, 497, 744, -558, -75, 943, 32, 604, -901, 289, -486, -747, -520, -871, -533, -510, 451, 633, 955, -276, 358, -166, 206, 254, -438, -143, -512, 390, 120, 958, -680, -407, -528, -792, 902, 219, 124, 600, 627, -570, -354, 597, 307, -472, 966, 770, -651, 580, 528, -976, 959, 386, 455, 561, -211, -71, -39, 535, -337, -592, -26, 890, -680, -191, 790, 740, 616, -515, -469, 975, -942, 299, 93, -823, 736, 107, -525, -179, 17, -138, 546, -655, -937, 667, 616, -303, 883, 570, -354, 503, -917, 529, -133, -775, -455, 641, 258, -163, -621, -673, -886, 135, 11, 667, -740, 319, -447, -624, 594, 880, -175, -185, -236, -182, 961, 594, 990, -396, -88, -952, -168, -810, 83, 841, -355, 108, 89, -947, -421, 433, 491, -576, 26, 950, 875, 830, -37, 365, -374, -74, -24, 938, 326, -133, -915, 520, -830, -569, 441, -348, 728, 870, -491, 172, -152, 898, -51, 53, 843, 341, -411, 958, -417, 23, 508, 100, -649, 746, 343, -903, -555, -96, -590, 669, -577, 859, 297, 265, -505, 799, 217, -261, 560, 178, -718, 228, -778, 472, 457, 946, -628, 883, -934, 144, -956, 839, 868, -352, 924, 97, 416, -622, -810, -496, -957, -665, 293, -48, 887, -733, -206, 993, -417, 474, -797, 574, 653, 898, -11, -937, 994, 122, 59, 687, -706, -325, 130, 485, -592, 517, 465, 643, 718, -200, -791, -905, -318, -321, -256, -918, -906, -218, 423, 914, -384, 334, -482, 813, -193, -751, 733, 109, 33, 73, 701, -749, 400, -405, -723, -152, 118, -933, -990, -894, -314, -567, 96, -539, -536, 412, 39, 366, -643, 366, -675, 663, -197, -390, -35, -945, -738, 565, -897, -230, 230, -208, 925, 597, 735, 449, -764, -177, 375, -649, -94, -95, -438, -375, 579, -260, 859, 860, -265, -165, 198, 67, 565, 903, 872, -364, 232, 361, 940, 504, 101, 678, 820, -613, -387, 296, -530, -709, 948, -481, -285, -380, -944, 893, 758, -811, -14, 453, 864, -967, 503, 150, -658, -326, -873, 907, -57, 683, 437, -896, 988, 680, -640, -251, 42, 972, 927, -166, -491, -695, -708, -119, 947, -769, 524, -787, 440, 751, -506, 511, 486, 45, -718, -869, -572, 630, -180, 910, 336, 782, -701, -818, -14, 57, -449, -150, -499, -785, -581, -26, 571, -803, 131, -459, 231, 403, -423, -697, 972, 806, -536, -638, -402, -816, 655, 568, 544, -885, -646, -336, -308, 644, 279, 412, 821, -38, -22, -545, 420, 917, 981, 952, -480, -519, -868, -989, -64, 417, -184, -171, 632, 470, 730, -624, 867, -919, 295, -166, 987, 747, -589, -867, -295, -627, 618, 231, -160, -507, -716, 317, 833, -728, 450, 717, -202, -963, -223, 390, -458, -268, 783, -960, 490, -336, -775, -116, 698, 344, 359, -102, -903, 143, -698, 604, -117, -87, 320, -173, -135, 977, 408, -677, 657, 617, 242, -456, 532, 915, -890, -513, -781, 701, -472, -344, 663, 408, 102, 64, -688, 339, -386, 141, -283, 278, 337, -400, 428, -934, -454, 614, 473, 114, -536, 182, 98, 98, -908, 567, -973, -712, 802, -732, 355, 968, 256, -531, 608, -512, 238, -538, 684, 269, -821, -914, 234, -682, -568, -366, -432, -501, -365, 421, -72, 537, 694, -687, 902, 594, -500, -664, 43, 491, -701, -423, 744, 778, -695, -735, -273, -143, -757, 296, -87, -886, -480, -970, 748, -827, 309, -686, -817, 21, -480, 623, -533, -744, 128, 566, -828, 547, 86, 261, 974, -852, 678, -885, -430, 921, -621, 885, 910, -999, -201, -953, 852, 321, 114, -137, -950, 43, -599, 351, 716, 772, -990, 434, -734, 598, 378, 364, 14, -132, -956, -269, 237, 479, -471, 467, -945, -645, -689, 84, -659, -119, 736, 202, 835, 576, -77, -127, 899, 892, 77, 427, 120, -77, 774, -954, 862, 376, 388, -20, -957, 367, 892, 934, -998, -814, -15, -520, -402, -656, -801, -794, 283, 589, -573, 634, 208, 148, -119, -996, -821, -794, -344, 616, -142, -353, 799, -583, 432, 20, -242, 657, -273, -602, -773, -439, -415, 888, -696, -582, -812, -266, -83, -344, -968, 948, 136, 758, -252, -230, 593, 889, -967, 670, 391, 90, -242, -635, -119, 847, 512, 499, -711, 173, 487, 419, 949, 782, 450, -972, -977, 547, 722, 613, 525, 688, -33, 204, 80, 598, 924, 434, -550, 54, -449, -458, -356, 258, -817, 269, -945, -159, -316, 930, -59, 651, 992, -621, -490, -963, -981, -192, 358, -850, -919, 118, -382, -335, 479, 951, -205, 187, 824, 381, -898, -204, 434, 830, -25, -629, -582, 905, 249, 593, -991, 394, 745, -55, 0, 771, -293, 405, 826, -941, -951, 944, -313, 946, -856, 366, 264, -875, 191, 526, 265, 756, 394, 419, 186, 175, 933, -710, -813, 888, -311, -957, -925, 932, -246, 934, -856, -469, 435, -906, 975, -727, 104, -290, -129, 888, -910, 481, 898, -338, 822, 449, 863, -613, -922, 976, 345, -904, 616, -965, 454, 805, -545, 24, 288, 579, 926, 193, 83, -511, -4, 611, 947, -212, 909, -406, 374, 305, 524, -407, -389, 257, -91, -868, -497, 887, -250, 323, 295, 926, -57, -534, 7, -425, 573, -599, 537, 130, -807, -808, -233, 656, -664, 285, -99, 9, 648, -733, -925, 35, -269, 796, 695, 628, 286, -184, 526, -50, -800, -240, 53, 16, -870, 934, -384, -452, 866, -572, -410, -714, -737, -702, 749, 18, -768, -59, 384, -940, 304, -347, 396, 382, -99, 46, 418, 305, -977, 129, 110, -304, 447, 230, 955, 936, -357, 834, -59, -924, 416, -520, 455, 359, -92, 11, -983, 903, 334, -124, 383, -915, 964, -510, -721, 179, 233, -967, -171, -604, -210, -781, 978, -287, -500, 823, -617, 951, 883, -700, 70, 466, 971, 964, 627, -252, -845, 100, -320, -685, -968, -483, 117, 610, -457, -6, 475, -818, -761, -556, -997, 48, -331, -526, -466, -642, 820, 896, 236, 646, 902, -62, 399, 83, -2, -98, 573, -672, -809, 114, 972, -770, -415, -674, -960, -477, -769, -825, -686, -93, 983, 167, -358, -858, 506, -504, -50, 913, 898, -781, -866, -666, 263, 608, 901, -595, -422, -873, -316, 466, 600, -234, -863, -633, -401, -15, 879, -596, 200, 184, 186, -18, -464, -350, 464, -450, 969, 96, -881, -109, -131, -8, 218, 937, 607, 724, -728, 809, 282, -608, -154, 428, 490, -393, 667, -189, -675, -386, -950, -865, -542, 474, -117, -328, 856, 198, -262, 857, -600, -143, 886, 190, -336, 130, -901, -192, -479, -564, 420, 791, -256, -433, 308, -957, -721, -46, -136, 431, -351, -834, -803, 619, -613, 281, 113, -98, 442, -161, 348, 229, 79, -778, 666, -431, 35, 527, 866, -433, 206, -121, -428, 566, 597, -887, 850, -614, 709, -972, -827, -505, 897, 672, 167, -121, -268, -252, -649, 463, -163, -452, 152, -165, 598, -881, 826, -421, 190, 720, -173, 625, -820, 606, 196, 587, -5, -325, -520, 123, -255, 171, -738, -348, 106, -474, -581, 137, 293, 993, 685, 515, -558, 222, -938, -556, 554, 643, -483, 995, 170, 506, 777, -345, 757, -294, 725, -919, -12, -801, -977, -771, -491, 283, -95, 20, 397, -420, -539, -804, -204, 616, -959, 26, 817, 240, 313, 495, -97, 243, 79, -767, 302, 0, -244, 789, -477, -152, 995, 149, -639, -444, 99, -262, 91, 183, 66, -830, 837, 39, -283, -486, 577, 753, 145, -770, 692, 194, 581, -542, 332, -844, -417, -128, 884, 555, 705, 799, 837, -394, 316, -636, -482, -741, 238, 64, 571, 761, -388, -125, -423, 141, -552, -504, 425, 521, 530, -825, 383, 963, 859, -610, -136, -709, -886, -945, 711, 349, -24, -213, 374, 95, 919, -425, 838, -342, 580, 831, -458, 612, -996, -277, -765, -130, -923, -717, -886, 409, 400, -88, 466, -968, -593, 824, -752, 954, 620, -724, 500, -427, 623, 843, -785, -74, 462, 736, -527, -751, 110, -485, 999, -274, -20, -720, -651, 402, -574, -483, -707, 296, -831, -59, -449, -638, -61, -995, 715, -819, -110, -652, -532, -424, -599, -8, -848, 678, -923, 789, 103, -799, -728, 655, -623, -549, 786, -264, 940, -981, -930, -434, 219, 143, -810, -373, 709, 549, -617, -425, 332, 949, -504, 123, -348, 37, -382, 971, 572, 427, 207, -301, -524, 36, 2, -895, -396, -527, -73, 822, 278, 326, -931, -400, 11, 664, -177, 641, 310, -792, -585, -30, 974, -615, 499, -297, 421, 663, 840, 283, 845, 293, -718, -694, 386, -53, -131, -976, -974, -118, 318, 764, -999, 644, 961, -750, -222, 812, -437, -572, -582, -891, 713, 42, 219, -256, 760, -257, -860, -972, -122, 951, 351, 423, -819, -715, -288, 610, -272, 561, 457, -388, 924, -244, 232, -378, 175, 78, -619, 812, -85, 748, 204, -519, 870, 106, 872, 771, 178, -406, 602, 971, 845, 257, 188, 381, -814, -219, 389, 381, 324, -53, 479, 212, 541, -820, -238, -279, -123, 479, 881, 279, 793, 94, 624, 750, -508, 620, -700, 854, -185, 217, 835, -714, -670, 860, 932, 456, -397, -771, 204, -241, 136, 239, -638, 739, -117, -194, 898, -576, -859, -599, 112, 77, 618, -430, 799, -738, 32, 416, -993, -232, -647, 830, 792, -678, -928, -262, 865, 289, 925, 988, 989, 883, -116, -897, -202, 465, -650, -784, -83, -843, -214, 406, 756, -934, 328, -110, 345, 601, 306, -93, 90, -237, 360, -241, -696, -47, -977, -546, -152, 497, -573, 449, -993, -527, 234, -440, -291, 143, -817, -114, 399, -36, 553, 771, -411, -502, -704, -420, 943, 984, 696, 572, 760, 937, 859, -349, -685, -867, 937, 976, -751, -402, -553, 311, 53, -398, -869, -348, -616, -232, 111, 681, 375, -917, -49, 433, 453, 809, 28, 856, 748, 69, 759, 572, 770, 248, -144, 542, 178, 714, 781, -900, -236, 843, 930, 622, -248, -296, 844, 194, -215, -415, -246, -818, -802, 857, -894, -323, -939, 899, 802, -114, 82, -977, 653, 476, 519, -335, 845, -920, -733, 505, -915, 256, 384, -956, -597, 201, -473, -9, -92, -708, -147, 874, 815, 726, -587, 892, -625, -892, 253, 367, -726, -708, 353, -843, -405, 868, -183, -871, -386, -556, 233, 111, 57, 49, -309, 404, -87, -804, 790, -140, -873, 981, 467, 65, 324, 39, 623, -220, 954, 848, 283, -100, -75, -888, -713, -231, -838, -285, 590, 121, 62, 460, 571, -549, -133, -94, -883, 642, -434, -316, -818, 503, 335, 50, -303, -899, -659, -567, -129, 270, -499, -164, 190, 779, 532, -161, -490, -555, 731, -314, -735, 23, -943, 835, 303, 963, -253, 772, -282, -168, -789, -415, 679, 118, -961, -463, 992, -560, 235, -403, -997, -800, -713, -593, 897, -367, 377, -662, 305, -37, 782, 893, 670, -971, -16, 303, 144, 101, -851, -968, 592, -857, 859, 217, -62, -14, -115, -245, -554, -983, -56, 810, 367, -846, 795, 909, 552, -156, 465, 476, 776, 195, -595, 697, -877, -775, 188, -653, 737, -135, 923, -454, -36, -664, 984, 745, -80, -334, -560, -557, -409, -844, 976, -464, 530, 564, -204, 51, -420, -69, -199, -485, 500, 202, -177, -276, -319, -761, -584, 746, 864, -248, 497, 732, -720, 200, -637, -530, -806, 779, -518, 386, -665, -879, 594, -303, -503, 496, 651, 702, -121, -984, 958, 171, 937, 603, -919, -240, -724, 2, -995, 604, -586, -92, -235, -744, -848, 456, -823, 195, 467, 807, -404, 533, 990, 896, 365, 327, -857, 727, -86, -100, -304, 892, 160, 509, -779, -117, -152, -654, 749, -42, 328, 957, 822, -633, 48, -226, -184, 234, -573, 564, -82, 21, 475, 267, 169, -505, 996, 735, -806, -541, 609, 984, -580, -235, -21, 970, -39, -152, 545, 830, 842, -274, -366, -183, -628, -457, 992, 745, -797, -22, 207, -627, 320, -988, -783, 692, 736, 723, 412, -482, -909, -151, 120, -414, -846, 773, -446, -482, -116, -382, -869, -756, -746, 368, -581, 36, 70, 207, -229, -156, 920, 454, -112, -306, -184, -536, -176, -4, 99, -118, -465, -736, 178, 644, 879, 847, -14, -452, 302, 226, -447, -838, -416, 763, -900, 24, -454, -270, 684, 591, 821, -5, -584, -333, 582, -117, -251, 666, 184, -489, 425, -844, -392, 661, -176, 259, 813, -479, 717, 851, -188, 667, -826, -506, -338, 658, -603, -326, 710, -414, 481, 52, 506, 676, 88, 169, -383, 215, 65, -128, -190, 531, -935, -127, 208, 288, 648, 13, -630, -27, -498, -322, 804, 97, -254, 254, -897, 884, 568, 685, 162, -715, 610, -437, 559, -899, -288, -140, -186, -54, 343, -831, 687, 953, 28, 427, -108, 581, -328, -872, 605, 846, 917, -343, 923, 954, -181, 269, -979, -279, 899, 513, 11, 368, 369, 625, 617, -475, -790, -659, 996, 975, 776, 787, 434, -859, -746, 68, 761, -506, -250, -712, -411, 954, 555, -82, 482, 795, 835, 998, -598, 36, 834, 236, -53, -286, -934, 764, 938, -197, 680, -914, -197, 251, 753, 124, 261, 86, 887, -892, 174], 10))
    # fmt: on
