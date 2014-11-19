import curses

class CursesTest:




    def __init__(self):
        self.max = 1
        self.text = '123123qweqew'
        self.menu = ['Menu1', 'Menu2', 'jk', 'jajajaj']

        self.screen = curses.initscr()

        curses.start_color()

        self.h = curses.color_pair(1)
        self.n = curses.A_NORMAL

        self.key_pressed = None
        self.position = 0
        self.pad_p = 0


        self.make_me_rainbow()

        pos = 1
        x = None

        self.context = [
                {  },
                { 'text' : 'pozycja no 2' },
                { 'text' : 'jajaj' }
                    ]

        self.draw_screen()


    def setup_position(self, max_x, max_y):

        self.context = [
                { 'text' : 'pos 1', 'pos_x' : 4, 'pos_y' : 4 },
                { 'text' : 'pos 1', 'pos_x' : 5, 'pos_y' : 4 },
                { 'text' : 'pos 1', 'pos_x' : 6, 'pos_y' : 4 }
                    ]





    def make_me_rainbow(self):
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
        curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_GREEN)



    def draw_screen(self):
        self.maxY, self.maxX = self.screen.getmaxyx()

        self.headWin = curses.newwin(1, self.maxX, 0, 0)
        self.bodyWin = curses.newwin(self.maxY - 2, self.maxX, 1, 0)
        self.footerWin = curses.newwin(1, self.maxX, self.maxY - 1, 0)
        self.init_head()
        #self.init_body()
        #self.init_footer()


    def init_head(self):
        info = " text "
        self.headWin.addstr(0, 0, info, curses.color_pair(4))
        rightStr = "Tekst po prawej"
        self.headWin.addstr(0, self.maxX - len(rightStr) - 1, rightStr,
                            curses.color_pair(2))
        self.headWin.bkgd(' ', curses.color_pair(7))
        self.headWin.noutrefresh() 


    #def init_body(self)


    #def init_footer(self)




        


    def make_menu(self):

        self.screen.clear()
        self.screen.box()

        pad = self.screen.subpad(20, 20, 30, 20)
        # These loops fill the pad with letters; addch() is
        # explained in the next section
        #for y in range(0, 29):
            #for x in range(0, 39):
                #pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

        # Displays a section of the pad in the middle of the screen.
        # (0,0) : coordinate of upper-left corner of pad area to display.
        # (5,5) : coordinate of upper-left corner of window area to be filled
        #         with pad content.
        # (20, 75) : coordinate of lower-right corner of window area to be
        #          : filled with pad content.
        pad.border()

        pad.scrollok(1)
        pad.idlok(1)



        self.setup_position(1, 2)


        #win.refresh()

        self.screen.addstr(15, 15, 'nnfgnf')


        if self.key_pressed == 258:
            if self.position < len(self.context) - 1:
                self.position += 1
            else:
                self.position = 0
        elif self.key_pressed == 259:
            if self.position > 0:
                self.position += -1
            else:
                self.position = len(self.context) - 1
        
        self.max_xy = self.screen.getmaxyx()

        #for value in self.context:
            #self.screen.addstr(value['pos_x'], value['pos_y'], value['text'], self.n)






        actual = self.context[self.position]
        self.screen.addstr(actual['pos_x'], actual['pos_y'], actual['text'], self.h)

        self.screen.addstr(20, 20, str(self.max_xy[1]), self.h)


        if self.key_pressed == 258:
            self.pad_p += 1
        elif self.key_pressed == 259:
            self.pad_p -= 1



        self.screen.refresh()
        pad.refresh()
        self.key_pressed = self.screen.getch()



    def __listen_for_key(self, key):
        if key == ord("1"):
            self.text = 'asdasd'



    def build_ui(self):
        while True:
            self.make_menu()
            

while True:
    CursesTest()

