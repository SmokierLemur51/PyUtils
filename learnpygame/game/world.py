import pygame as pg
import random
import noise
from .settings import TILE_SIZE



class World:

	def __init__(self, hud, grid_length_x, grid_length_y, width, height):
		self.hud = hud
		self.grid_length_x = grid_length_x
		self.grid_length_y = grid_length_y
		self.width = width
		self.height = height
 
		self.perlin_scale = grid_length_x / 2

		self.grass_tiles = pg.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
		self.tiles = self.load_images()
		self.world = self.create_world()

		self.temp_tile = None



	def update(self, camera):
		mouse_pos = pg.mouse.get_pos()

		if self.hud.selected_tile is not None:
			grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1], camera.scroll)

			img = self.hud.selected_tile["image"].copy()
			img.set_alpha(100)

			render_pos = self.world[grid_pos[0]][grid_pos[1]]["render_pos"]

			self.temp_tile = {
				"image": img,
				"render_pos": render_pos,
			}


	def draw_world(self, screen, camera):
		screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

		for x in range(self.grid_length_x):
			for y in range(self.grid_length_y):
				render_pos = self.world[x][y]["render_pos"]
				tile = self.world[x][y]["tile"]
				if tile != "":
					screen.blit(
						self.tiles[tile], 
						(
							render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x, 
							render_pos[1] - (self.tiles[tile].get_height() - TILE_SIZE) + camera.scroll.y,
						),
					)

		if self.temp_tile is not None:
			render_pos = self.temp_tile["render_pos"]
			screen.blit(
				self.temp_tile["image"],
				(
					render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
					render_pos[1] - (self.temp_tile["image"].get_height() - TILE_SIZE) + camera.scroll.y,
				)
			)

	def create_world(self):
		world = []

		for grid_x in range(self.grid_length_x):
			world.append([])
			for grid_y in range(self.grid_length_y):
				world_tile = self.grid_to_world(grid_x, grid_y)
				world[grid_x].append(world_tile)

				# rendering blocks to surface to reduce draw clls
				render_pos = world_tile["render_pos"]
				self.grass_tiles.blit(self.tiles["block"], (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1]))

		return world


	def grid_to_world(self, grid_x, grid_y):

		rect = [
			(grid_x * TILE_SIZE, grid_y * TILE_SIZE),
			(grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
			(grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
			(grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
		]

		iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

		# render pos for tile
		minx = min([x for x, y in iso_poly])
		miny = min([y for x, y in iso_poly])

		r = random.randint(1, 100)
		perlin = 100 * noise.pnoise2(grid_x/self.perlin_scale, grid_y/self.perlin_scale)

		if (perlin >= 15) or (perlin <= -35):
			tile = "tree"
		else:
			if r <= 1:
				tile = "tree"
			elif r <= 2:
				tile = "rock"
			else:
				tile = ""


		out = {
			"grid": [grid_x, grid_y],
			"cart_rect": rect,
			"iso_poly": iso_poly,
			"render_pos": [minx, miny],
			"tile": tile,
		}

		return out


	def cart_to_iso(self, x, y):
		iso_x = x - y
		iso_y = (x + y) / 2 
		return iso_x, iso_y


	def mouse_to_grid(self, x, y, scroll):
		''' the goal is to reverse the isometric calculations into cartesian coordinates '''

		# transform to world position by removing camera scroll and offset
		world_x = x - scroll.x - self.grass_tiles.get_width()/2
		world_y = y - scroll.y

		# transform to cart, this is the inverse of cart_to_iso func
		cart_y = (2 * world_y - world_x)/2
		cart_x = cart_y + world_x

		# transform to grid coordinates
		grid_x = int(cart_x // TILE_SIZE)
		grid_y = int(cart_y // TILE_SIZE)

		return grid_x, grid_y


	def load_images(self):
		block = pg.image.load("assets/graphics/block.png").convert_alpha()
		tree = pg.image.load("assets/graphics/tree.png").convert_alpha()
		rock = pg.image.load("assets/graphics/rock.png").convert_alpha()

		return {"block": block, "tree": tree, "rock": rock,}