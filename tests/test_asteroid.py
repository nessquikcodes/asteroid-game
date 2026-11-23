import pygame
import pytest

from asteroid import Asteroid
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEEDUP


@pytest.fixture
def asteroids():
    group = pygame.sprite.Group()
    Asteroid.containers = (group,)
    yield group
    Asteroid.containers = ()

def test_small_asteroid_disappears(asteroids):
    small_asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS)

    small_asteroid.split()

    assert not asteroids

def test_medium_asteroid_splits_into_two_small(asteroids):
    medium_asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS * 2)

    medium_asteroid.split()
    assert len(asteroids) == 2

    for asteroid in asteroids:
        assert asteroid.radius == ASTEROID_MIN_RADIUS

def test_large_asteroid_splits_into_two_medium(asteroids):
    large_asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS * 3)

    large_asteroid.split()
    assert len(asteroids) == 2

    for asteroid in asteroids:
        assert asteroid.radius == (ASTEROID_MIN_RADIUS * 2)

def test_split_asteroids_move_faster(asteroids):
    test_asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS * 2)

    test_asteroid.velocity = pygame.Vector2(100, 0)

    test_asteroid.split()
    assert len(asteroids) == 2

    for asteroid in asteroids:
        assert asteroid.velocity.length() == pytest.approx(100 * ASTEROID_SPLIT_SPEEDUP)
