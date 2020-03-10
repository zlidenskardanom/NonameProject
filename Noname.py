from game.window import *

class InitGame():
	def __init__(self):
		self.WIDTH = 1920
		self.HEIGHT = 1080
		self.fullscreen = 0
		self.visiblemouse = True
		self.rungame = True
		
		self.centeredwindow()
		self.preinitsound()
		self.initwindow()
		self.setvisisblemouse()
		self.managegame = ManageGame()
	def centeredwindow(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
	def preinitsound(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
	def initwindow(self):
		pygame.init()
		pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\2.png")))
		if self.fullscreen == 0:
			self.surf_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		elif self.fullscreen == 1:
			self.surf_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
		pygame.display.set_caption("Noname")
	def setvisisblemouse(self):
		pygame.mouse.set_visible(self.visiblemouse)
	def initstart(self):
		while self.rungame:
			self.managegame.update()

class ManageGame():
	def __init__(self):
		self.scene = 0
		self.gamewindow = GameWindow(60)
		self.menuwindow = MenuWindow(60)
	def update(self):
		if self.scene == 0:
			self.menuwindow.start()
		elif self.scene == 1:
			self.gamewindow.start()

if __name__ == "__main__":
	thegame = InitGame()
	thegame.initstart()