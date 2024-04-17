# from facefusion.core import conditional_process, limit_resources, get_frame_processors_modules, pre_check, facefusion
from pathlib import Path
from itertools import product
from subprocess import run
from random import shuffle
import shutil

def get_sources(folder_path: str):
    for i in Path(folder_path).iterdir():
        if i.name.endswith('jpg') or i.name.endswith('png'):
            yield i

def get_targets(folder_path: str):
    for i in Path(folder_path).iterdir():
        if i.name.endswith('mp4') or i.name.endswith('webm') or i.name.endswith('gif'):
            yield i

def main(folder_path: str, output_path: str):
    sources = get_sources(folder_path)
    targets = get_targets(folder_path)
    tasks = list(product(sources, targets))
    shuffle(tasks)
    for source, target in tasks:
        filename = f'{source.stem}-{target.stem}'
        filename_ascii = "".join(i for i in filename if i.isascii())
        output = Path(output_path) / (filename_ascii + ".webm")
        if any(output.parent.glob(f"{output.stem}.*")):
            print(f"skipping...")
            continue
        try:
            run(
                [
                    './venv/Scripts/python.exe',
                    'run.py',
                    '-s',
                    str(source),
                    '-t',
                    str(target),
                    '-o',
                    str(output),
                    '--headless',
                ]
            )
        except Exception as e:
            print(f'failed to process {source} and {target} to {output_path}')
            shutil.rmtree(r"c:\Users\geral\AppData\Local\Temp\facefusion")
            raise e
        print("completd")
        

main(r"C:\Users\geral\Documents\Clover\temp", r"C:\Users\geral\Documents\Clover\temp\out")
# main(r"C:\Users\geral\Downloads\h", r"C:\Users\geral\Documents\Clover\temp\out")