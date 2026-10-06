"""모든 게임 모듈이 지켜야 하는 약속(계약)을 검사한다.

- GAME_NAME: 비어 있지 않은 문자열
- play(): 호출 가능한 함수
새 게임 파일이 추가돼도 자동으로 검사 대상에 포함된다.
"""

import importlib
import pkgutil

import games


def iter_game_modules():
    for info in pkgutil.iter_modules(games.__path__):
        yield importlib.import_module(f"games.{info.name}")


def test_each_game_follows_contract():
    for mod in iter_game_modules():
        assert isinstance(mod.GAME_NAME, str) and mod.GAME_NAME, mod.__name__
        assert callable(mod.play), mod.__name__
