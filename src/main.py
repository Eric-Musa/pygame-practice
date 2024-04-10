import pygame
from pygame.locals import *
 

class App:
    def __init__(self, max_count=-1):
        print('constructor')
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.count = 0
        self.max_count = max_count
 
    def on_init(self):
        print('on init')
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        print('event', event)
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        print('loop')
        pass

    def on_render(self):
        print('render')
        pass

    def on_cleanup(self):
        print('cleanup')
        pygame.quit()
 
    def on_execute(self):
        print('execute')
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            

            print('running')
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.count += 1
            print(self.count)
            if self.max_count > 0 and self.count > self.max_count:
                print('break')
                break
        self.on_cleanup()
 

if __name__ == "__main__":
    theApp = App(10)
    theApp.on_execute()
