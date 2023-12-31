import time
import random
# from colorama import Fore, Back, Style, init
import pyttsx3

class WordGame:
    def __init__(self):
        self.correct_answers = 0
        self.periods = 50
        self.engine = pyttsx3.init()

    def speak_word(self, word):
        self.engine.say(word)
        self.engine.runAndWait()

    def display_message(self, message, color="white"):
        colors = {"white": "\033[0m", "green": "\033[92m", "red": "\033[91m"}
        print(f"{colors[color]}{message}{colors['white']}")
        time.sleep(0)

    def display_message_1(self, message, color="white"):
        colors = {"white": "\033[0m", "green": "\033[92m", "red": "\033[91m"}
        print(f"{colors[color]}{message}{colors['white']}")
        time.sleep(1)

    def play_game(self):
        import random

        class ColorfulTextPrinter:
            def __init__(self):
                self.color_mapping = {
                    "red": "\033[91m",
                    "green": "\033[92m",
                    "yellow": "\033[93m",
                    "blue": "\033[94m",
                    "purple": "\033[95m",
                    "cyan": "\033[96m",
                    "white": "\033[97m",
                    "reset": "\033[0m"
                }

            def print_colored_red(self, element):
                print(f"{self.color_mapping['red']}{element}{self.color_mapping['reset']}", end=" ")

            def print_colored_green(self, element):
                print(f"{self.color_mapping['green']}{element}{self.color_mapping['reset']}", end=" ")

            def print_colored_yellow(self, element):
                print(f"{self.color_mapping['yellow']}{element}{self.color_mapping['reset']}", end=" ")

            def print_colored_purple(self, element):
                print(f"{self.color_mapping['purple']}{element}{self.color_mapping['reset']}", end="\n")

            def print_colored_cyan(self, element):
                print(f"{self.color_mapping['cyan']}{element}{self.color_mapping['reset']}", end="\n")



        printer = ColorfulTextPrinter()
        tcrt = "Lessons in order:"
        printer.print_colored_cyan(tcrt)
        printer = ColorfulTextPrinter()
        tcrt = f"\t1. People "
        printer.print_colored_cyan(tcrt)
        printer = ColorfulTextPrinter()
        tcrt = f"\t2. School "
        printer.print_colored_cyan(tcrt)
        printer = ColorfulTextPrinter()
        tcrt = f"\t3. Houses "
        printer.print_colored_cyan(tcrt)
        printer = ColorfulTextPrinter()
        tcrt = f"\t4. Work "
        printer.print_colored_cyan(tcrt)

        time.sleep(2)

        choose = int(input("So which one do we practice? (1-4): "))

        szavak_0 = []
        with open(f"angol_szavak_{choose}.txt", "r", encoding="utf-8") as file:
            for egysor in file:
                egysor = egysor.strip()
                szavak_0.append(egysor)
        # print(szavak_0)

        szavak = []
        i = 0
        for egyelem in szavak_0:
            try:
                i += 1
                szavak.append([szavak_0[i - 1], szavak_0[i]])
                i += 3
            except:
                continue
        # print(szavak)

        self.display_message("\nOk. Let's learn the words!", "green")

        osszes_szo = []
        megtanult_szavak = []
        i = 0
        k = 5
        in_correct = 0
        f = 0
        while len(szavak) != 0:
            try:
                f += 1
                self.display_message_1(f"\n{f}. What's mean this word? ", "green")
                # self.speak_word("Helo. Let's learn the words! Let's start with the first task. Choose the correct translation! ")
                while i < k:
                    self.display_message(f"\n{szavak[i][1]} - ", "green")
                    e = 0
                    segitseg = [szavak[i][0]]
                    while e < 3:
                        x = random.randint(0, len(szavak))
                        angolul = szavak[x][0]
                        magyarul = szavak[x][1]
                        segitseg.append(angolul)
                        e += 1
                    if in_correct == 0:
                        while len(segitseg) != 0:
                            l = random.randint(0, len(segitseg) - 1)
                            print(f"\t{segitseg[l]}")
                            segitseg.remove(segitseg[l])
                    if in_correct > 0:
                        while len(segitseg) != 0:
                            l = random.randint(0, len(segitseg) - 1)
                            if segitseg[l] == szavak[i][0]:
                                self.display_message(f"\t{segitseg[l]}", "green")
                                segitseg.remove(segitseg[l])
                            elif segitseg[l] != szavak[i][0]:
                                self.display_message(f"\t{segitseg[l]}", "red")
                                segitseg.remove(segitseg[l])
                    valasza = input(f"What is the correct answer? ")
                    if valasza == szavak[i][0]:
                        self.display_message(f"Correct! ", "green")
                        self.speak_word(valasza)
                        megtanult_szavak.append(szavak[i])
                        i += 1
                        in_correct = 0
                    else:
                        self.display_message(f"Wrong! Try again! ", "red")
                        in_correct += 1
                k += 5
                z = 5
                f += 1
                self.display_message_1(f"\n{f}. Translate the words! \n", "green")
                while z != 0:
                    y = random.randint(0, len(megtanult_szavak) - 1)
                    valasza = input(f"{megtanult_szavak[y][1]} - ")
                    if valasza == megtanult_szavak[y][0]:
                        self.display_message(f"Correct! ", "green")
                        self.speak_word(megtanult_szavak[y][0])
                        z -= 1
                    else:
                        valasza = valasza.strip(" ").split(" ")
                        megoldas = megtanult_szavak[y][0]
                        megoldas = megoldas.strip(" ").split(" ")
                        jo_valaszok = []
                        p = 0
                        for egyelem in megoldas:
                            if egyelem in valasza:
                                jo_valaszok.append(p)
                            p += 1
                        printer = ColorfulTextPrinter()
                        wrong = "Wrong!"
                        printer.print_colored_red(wrong)
                        printer = ColorfulTextPrinter()
                        tcrt = "The correct translation is:"
                        printer.print_colored_yellow(tcrt)
                        for q in range(0, len(megoldas), 1):
                            if q in jo_valaszok:
                                printer = ColorfulTextPrinter()
                                element = megoldas[q]
                                printer.print_colored_green(element)
                            else:
                                printer = ColorfulTextPrinter()
                                element = megoldas[q]
                                printer.print_colored_red(element)
                        add = ""
                        print(add)
                        self.speak_word(megtanult_szavak[y][0])
                if f % 2 == 0:
                    d = 0
                    printer = ColorfulTextPrinter()
                    hear = f"\n{f}.5. So you've learned {len(megtanult_szavak)} words so far. (If you enter: 1, you can replay it.) "
                    printer.print_colored_purple(hear)
                    self.display_message_1("")
                    time.sleep(1)
                    while d < 4:
                        m = random.randint(0, len(megtanult_szavak))
                        solve = megtanult_szavak[m][0]
                        print(f"Write here what you hear: ", end="")
                        time.sleep(1)
                        self.speak_word(megtanult_szavak[m][0])
                        hear = input("")
                        if hear == megtanult_szavak[m][0]:
                            self.display_message_1(f"Correct! In Hungarian: '{megtanult_szavak[m][1]}'", "green")
                            self.speak_word(megtanult_szavak[m][0])
                            d += 1
                        if hear != megtanult_szavak[m][0] and hear != '1':
                            hear = hear.strip(" ").split(" ")
                            megoldas = megtanult_szavak[m][0]
                            megoldas = megoldas.strip(" ").split(" ")
                            jo_valaszok = []
                            p = 0
                            for egyelem in megoldas:
                                if egyelem in hear:
                                    jo_valaszok.append(p)
                                p += 1
                            printer = ColorfulTextPrinter()
                            wrong = "Wrong!"
                            printer.print_colored_red(wrong)
                            printer = ColorfulTextPrinter()
                            tcrt = "The word you heard before:"
                            printer.print_colored_yellow(tcrt)
                            for q in range(0, len(megoldas), 1):
                                if q in jo_valaszok:
                                    printer = ColorfulTextPrinter()
                                    element = megoldas[q]
                                    printer.print_colored_green(element)
                                else:
                                    printer = ColorfulTextPrinter()
                                    element = megoldas[q]
                                    printer.print_colored_red(element)
                            add = ""
                            print(add)
                            self.speak_word(megtanult_szavak[m][0])
                            time.sleep(1)
                        if hear == '1':
                            print(f"Again! Write here what you hear: ", end="")
                            self.speak_word(megtanult_szavak[m][0])
                            hear_re = input("")
                            if hear_re == megtanult_szavak[m][0]:
                                self.display_message_1(f"Correct! In Hungarian: '{megtanult_szavak[m][1]}'", "green")
                                self.speak_word(megtanult_szavak[m][0])
                                d += 1
                            else:
                                hear_re = hear_re.strip(" ").split(" ")
                                megoldas = megtanult_szavak[m][0]
                                megoldas = megoldas.strip(" ").split(" ")
                                jo_valaszok = []
                                p = 0
                                for egyelem in megoldas:
                                    if egyelem in hear_re:
                                        jo_valaszok.append(p)
                                    p += 1
                                printer = ColorfulTextPrinter()
                                wrong = "Wrong!"
                                printer.print_colored_red(wrong)
                                printer = ColorfulTextPrinter()
                                tcrt = f"The word you heard before:"
                                printer.print_colored_yellow(tcrt)
                                for q in range(0, len(megoldas), 1):
                                    if q in jo_valaszok:
                                        printer = ColorfulTextPrinter()
                                        element = megoldas[q]
                                        printer.print_colored_green(element)
                                    else:
                                        printer = ColorfulTextPrinter()
                                        element = megoldas[q]
                                        printer.print_colored_red(element)
                                add = ""
                                print(add)
                                self.speak_word(megtanult_szavak[m][0])
                                time.sleep(1)

                # if f % 2 == 0:
                #     s = 0
                #     while s < 2:
                #         printer = ColorfulTextPrinter()
                #         read = f"\n{f}.5. A little game! There are 3 English words hidden in this stream of letters. What are these? "
                #         printer.print_colored_cyan(read)
                #         self.display_message_1("")
                #         time.sleep(1)
                #         texts = []
                #         for i in range(ord('a'), ord('z') + 1):
                #             texts.append(chr(i))
                #         egy = random.randint(0, len(megtanult_szavak))
                #         ketto = random.randint(0, len(megtanult_szavak))
                #         harom = random.randint(0, len(megtanult_szavak))
                #
                #         hossza_1 = random.randint(10, 30)
                #         hossza_2 = random.randint(10, 30)
                #         hossza_3 = random.randint(10, 30)
                #         hossza_4 = random.randint(10, 30)
                #
                #         for h in range(0, hossza_1, 1):
                #             szam = random.randint(0, len(texts))
                #             print(f"{texts[szam]}", end="")
                #         print(f'{megtanult_szavak[egy]}', sep="", end="")
                #         for h in range(0, hossza_2, 1):
                #             szam = random.randint(0, len(texts))
                #             print(f"{texts[szam]}", end="")
                #         print(f'{megtanult_szavak[ketto]}', sep="", end="")
                #         for h in range(0, hossza_3, 1):
                #             szam = random.randint(0, len(texts))
                #             print(f"{texts[szam]}", end="")
                #         print(f'{megtanult_szavak[harom]}', sep="", end="")

            except:
                continue

if __name__ == "__main__":
    game = WordGame()
    game.play_game()
