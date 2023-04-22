import pygame as pg


class Camera:
	def __init__(self, width, height):
		''' We are taking the width/height of the screen to react to the mouses postion rather than the keys '''
		self.width = width
		self.height = height

		# amount camera moved in pixels
		self.scroll = pg.Vector2(0, 0)
		
		self.diff_x = 0
		self.diff_y = 0
		self.speed = 25


	def update(self):
		''' moving based on mouse postion '''
		mouse_pos = pg.mouse.get_pos()

		# x movement
		if mouse_pos[0] > self.width * 0.97: 
			self.diff_x = -self.speed
		elif mouse_pos[0] < self.width * 0.03:
			self.diff_x = self.speed
		else:
			self.diff_x = 0

		# y movement
		if mouse_pos[1] > self.height * 0.97: 
			self.diff_y = -self.speed
		elif mouse_pos[1] < self.height * 0.03:
			self.diff_y = self.speed
		else:
			self.diff_y = 0

		# update camera scoll
		self.scroll.x += self.diff_x
		self.scroll.y += self.diff_y