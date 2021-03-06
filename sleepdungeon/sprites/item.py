#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from ..render_context import RenderContext
from ..base.context import Context
from ..base.game_constants import SpriteType, ZIndex
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR


class Item(Sprite):
    def __init__(self, name: str, x: int, y: int):
        if not hasattr(type(self), "_BASE_SURFACE"):
            type(self)._BASE_SURFACE = pygame.image.load(IMG_DIR + "items" + name + ".png")
        super().__init__()
        self.width = 1
        self.height = 1
        self.z_index = ZIndex.GROUND
        self.position = Position(x, y)


    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return type(self)._SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ITEM

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        cls._SURFACE = pygame.transform.smoothscale(
            cls._BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )
