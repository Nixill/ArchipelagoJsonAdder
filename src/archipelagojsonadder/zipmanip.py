#!/usr/bin/env python3
"""
    This file exists to do the thing and make the zip file compatable.  I'm told that the data will be coming to me, so I shall trust it is one trusts
    a god.
"""
from pathlib import Path
from typing import Any, Self
import zipfile
from dataclasses import dataclass
import os 
import json
from pprint import pprint

TESTDATA_DIR = 'testdata'

@dataclass
class APWorldJSONStruct:
    game: str
    minimum_ap_version: str
    world_version: str
    authors: list[str]

    @classmethod
    def validate(cls, data: dict[str, str | list[str]]) -> bool:
        test_data = cls(
            game = data.get('game'),
            minimum_ap_version = data.get('minimum_ap_version'),
            world_version = data.get('world_version'),
            authors = data.get('authors') or []
        )

        # ALSO UGLY
        # Could be better.  idk how.
        if isinstance(test_data.game, str) and isinstance(test_data.minimum_ap_version, str) and isinstance(test_data.world_version, str):
            return True
        else:
            return False

def get_world_name():
    ...

def validate_zip_file(apworld_file: Path) -> bool:
    json_filename = 'archipelago.json'
    apworld_file_name = apworld_file.name
    world_name = apworld_file.stem # temp just trust me
    json_filepath = f'{world_name}/{json_filename}'

    if not apworld_file.exists():
        # you might know this better.  lol.
        raise FileNotFoundError

    # lemme know if it fails after more rigorous testing
    with zipfile.ZipFile(apworld_file, mode='r') as zip:
        # adds all files into list that are stored in the 'world_name' dir
        valid_files = [file for file in zip.infolist() if file.filename.startswith(world_name)]

        # check that there's no extra files.  if there are, chances are you got a weird apworld file.
        if len(valid_files) != len(zip.infolist()):
            print('Invalid dir structure.  Verify only one folder in apworld file.')
            return False

        try:
            json_fileinfo = zip.getinfo(json_filepath)
        except KeyError as e:
            print(f'No archipelago.json file found at {json_filepath}')
            return False

        try:
            filedata = zip.read(json_filepath)
        except KeyError as e:
            print(f'KeyError on archive {apworld_file}: {e}')
            return False
        
        return APWorldJSONStruct.validate(json.loads(filedata))

def open_apworld_file(apworld_path: Path) -> zipfile.ZipFile:
    ...

if __name__ == '__main__':
    # This is *U G L Y*
    # you could probably do a cool list comprehension trick or whatever.
    # this is a rough test to make sure my function works.
    # sue me
    print(f'bloondstd6 validation: {validate_zip_file(Path(f'{TESTDATA_DIR}\\bloonstd6.apworld'))}')
    print(f'manicminers validation: {validate_zip_file(Path(f'{TESTDATA_DIR}\\manicminers.apworld'))}')
    print(f'ufo50 validation: {validate_zip_file(Path(f'{TESTDATA_DIR}\\ufo50.apworld'))}')