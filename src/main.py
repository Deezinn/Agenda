from menu import Menu
class Main:
    def __init__(self):
        self.menu = Menu()
    def run(self):
        self.menu.opcoes()

if __name__ == "__main__":
    main = Main()
    main.run()
