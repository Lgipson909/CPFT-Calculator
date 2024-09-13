def main():
    while True:
        print("Hello, Welcome to the Citadel CPFT Score Calculator. Please enter your scores as follows and follow the format listed.")

        x = int(input("How many pushups did you do? (e.g., 4 or 45). Min 10: "))

        if x == 10:
            p = 60
        elif x in {11, 12, 13}:
            p = 61
        elif x in {14, 15, 16}:
            p = 62
        elif x == 17:
            p = 63
        elif x in {18, 19, 20}:
            p = 64
        elif x in {21, 22}:
            p = 65
        elif x == 23:
            p = 66
        elif x == 24:
            p = 67
        elif x == 25:
            p = 68
        elif x in {26, 27}:
            p = 69
        elif x == 28:
            p = 70
        elif x == 29:
            p = 71
        elif x == 30:
            p = 72
        elif x == 31:
            p = 73
        elif x == 32:
            p = 75
        elif x == 33:
            p = 76
        elif x == 34:
            p = 77
        elif x == 35:
            p = 78
        elif x == 36:
            p = 79
        elif x == 37:
            p = 80
        elif x == 38:
            p = 82
        elif x == 39:
            p = 83
        elif x == 40:
            p = 84
        elif x == 41:
            p = 86
        elif x == 42:
            p = 87
        elif x == 43:
            p = 88
        elif x == 44:
            p = 89
        elif x == 45:
            p = 90
        elif x == 46:
            p = 91
        elif x == 47:
            p = 92
        elif x == 48:
            p = 93
        elif x == 49:
            p = 94
        elif x == 50:
            p = 95
        elif x == 51:
            p = 96
        elif x in {52, 53}:
            p = 97
        elif x == 54:
            p = 98
        elif x in {55, 56}:
            p = 99
        elif x >= 57:
            p = 100

        y = int(input("How long was your plank? (e.g., For a 3:45 plank, enter 345). Min 110: "))

        if y in {110, 111, 112}:
            o = 40
        elif y in {113, 114, 115}:
            o = 41
        elif y in {116, 117}:
            o = 42
        elif y in {118, 119, 120}:
            o = 43
        elif y in {121, 122}:
            o = 44
        elif y in {123, 124, 125}:
            o = 45
        elif y in {126, 127, 128}:
            o = 46
        elif y in {129, 130}:
            o = 47
        elif y in {131, 132, 133}:
            o = 48
        elif y in {134, 135}:
            o = 49
        elif y in {136, 137, 138}:
            o = 50
        elif y in {139, 140, 141}:
            o = 51
        elif y in {142, 143}:
            o = 52
        elif y in {144, 145, 146}:
            o = 53
        elif y in {147, 148}:
            o = 54
        elif y in {149, 150, 151}:
            o = 55
        elif y in {152, 153}:
            o = 56
        elif y in {154, 155, 156}:
            o = 57
        elif y in {157, 158, 159}:
            o = 58
        elif y in {200, 201}:
            o = 59
        elif y in {202, 203, 204}:
            o = 60
        elif y in {205, 206}:
            o = 61
        elif y in {207, 208, 209}:
            o = 62
        elif y in {210, 211}:
            o = 63
        elif y in {212, 213, 214}:
            o = 64
        elif y in {215, 216, 217}:
            o = 65
        elif y == 218:
            o = 66
        elif y in {220, 221, 222}:
            o = 67
        elif y in {223, 224}:
            o = 68
        elif y in {225, 226, 227}:
            o = 69
        elif y in {228, 229, 230}:
            o = 70
        elif y in {231, 232}:
            o = 71
        elif y in {233, 234, 235}:
            o = 72
        elif y in {236, 237}:
            o = 73
        elif y in {238, 239, 240}:
            o = 74
        elif y in {241, 242}:
            o = 75
        elif y in {243, 244, 245}:
            o = 76
        elif y in {246, 247, 248}:
            o = 77
        elif y in {249, 250}:
            o = 78
        elif y in {251, 252, 253}:
            o = 79
        elif y in {254, 255}:
            o = 80
        elif y in {256, 257, 258}:
            o = 81
        elif y in {259, 300, 301}:
            o = 82
        elif y in {302, 303}:
            o = 83
        elif y in {304, 305, 306}:
            o = 84
        elif y in {307, 308}:
            o = 85
        elif y in {309, 310, 311}:
            o = 86
        elif y in {312, 313}:
            o = 87
        elif y in {314, 315, 316}:
            o = 88
        elif y in {317, 318, 319}:
            o = 89
        elif y in {320, 321}:
            o = 90
        elif y in {322, 323, 324}:
            o = 91
        elif y in {325, 326, 327}:
            o = 92
        elif y in {328, 329}:
            o = 93
        elif y in {330, 331, 332}:
            o = 94
        elif y in {333, 334}:
            o = 95
        elif y in {335, 336, 337}:
            o = 96
        elif y in {338, 339}:
            o = 97
        elif y in {340, 341, 342}:
            o = 98
        elif y in {343, 344}:
            o = 99
        elif y >= 345:
            o = 100

        z = int(input("How long was your 1.5 mile run? For example, for a 10:45 run, enter 1045: "))

        if 1245 >= z > 1215:
            c = 45
        elif 1215 >= z > 1200:
            c = 50
        elif 1200 >= z > 1100:
            c = 55
        elif 1100 >= z > 1030:
            c = 60
        elif 1030 >= z > 1000:
            c = 65
        elif 1000 >= z > 945:
            c = 70
        elif 945 >= z > 930:
            c = 75
        elif 930 >= z > 915:
            c = 80
        elif 915 >= z > 900:
            c = 85
        elif 900 >= z > 845:
            c = 90
        elif 845 >= z > 814:
            c = 95
        elif z <= 815:
            c = 100

        a = p + o + c

        print(f"Your CPFT score is {a}. Have a nice day!")

        done = input("Are you done? (yes/no): ").strip().lower()
        if done == 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
