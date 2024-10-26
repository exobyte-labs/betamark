# Note from Laurence: I removed a couple of entires after checking a few for BICYCLE presence/absence.

import tqdm
from pathlib import Path

import hashlib
import requests
from io import BytesIO

import imageio.v3 as iio


### Train dataset ###

BASE_URL = "http://images.cocodataset.org/train2017/"
BICYCLE_IDS = [
    483108, 293802, 79841, 515289, 562150,
    412151, 462565, 509822, 321107, 61181,
    18783, 12896, 465692, 391584, 241350,
    438024, 442726, 435937, 292819, 157416,
    10393, 84540, 7125, 507249, 75923,
    240918, 122302, 140006, 536444, 344271,
    420081, 148668, 390137, 114183, 20307,
    280736, 536321, 188146, 559312, 535808,
    451944, 212558, 377867, 139291, 456323,
    549386, 254491, 314515, 415904, 101636,
    315173, 260627, 1722, 31092, 556205,
    49097, 70815, 467000, 416733, 203912,
    408143, 120340, 124462, 142718, 108838,
    445309, 140197, 12993, 111099, 215867,
    565085, 314986, 158708, 263961, 192128,
    377832, 187286, 195510, 406949, 330455,
]
NON_BICYCLE_IDS = [
    522418, 184613, 318219, 554625, 574769,
    60623, 309022, 5802, 222564, 118113,
    193271, 224736, 403013, 374628, 328757,
    384213, 86408, 372938, 386164, 223648,
    204805, 113588, 384553, 337264, 368402,
    12448, 542145, 540186, 242611, 51191,
    269105, 294832, 144941, 173350, 60760,
    324266, 166532, 262284, 360772, 191381,
    111076, 340559, 258985, 229643, 125059,
    455483, 436141, 129001, 232262, 166323,
    580041, 326781, 387362, 138079, 556616,
    472621, 192440, 86320, 256668, 383445,
    565797, 81922, 50125, 364521, 394892,
    1146, 310391, 97434, 463836, 241876,
    156832, 270721, 462341, 310103, 32992,
    122851, 540763, 138246, 197254, 32907,
]
LIST_OF_BICYCLES = [f"{BASE_URL}{str(id).zfill(12)}.jpg" for id in BICYCLE_IDS]
LIST_OF_NON_BICYCLES = [f"{BASE_URL}{str(id).zfill(12)}.jpg" for id in NON_BICYCLE_IDS]


class ImageCache:
    def __init__(self):
        self.cache_dir = Path.home() / ".cache" / "betamark"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_image(self, url):
        # Create filename from URL hash
        url_hash = hashlib.md5(url.encode()).hexdigest()
        cache_path = self.cache_dir / f"{url_hash}.png"

        # Try loading from cache
        if cache_path.exists():
            try:
                return iio.imread(cache_path)
            except Exception as e:
                print(f"Error loading cached image: {e}")
                cache_path.unlink(missing_ok=True)

        # Download if not in cache
        try:
            res = requests.get(url)
            res.raise_for_status()
            img = iio.imread(BytesIO(res.content))
            iio.imwrite(cache_path, img, plugin="pillow")
            return img
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None


def run_eval(user_func) -> dict:
    cache = ImageCache()
    correct_answers = 0
    total_answers = 0

    for url in tqdm.trange(len(LIST_OF_BICYCLES)):
        img = cache.get_image(LIST_OF_BICYCLES[url])
        total_answers += 1
        if user_func(img) == 1:
            correct_answers += 1

    for url in tqdm.trange(len(LIST_OF_NON_BICYCLES)):
        img = cache.get_image(LIST_OF_NON_BICYCLES[url])
        total_answers += 1
        if user_func(img) == 0:
            correct_answers += 1

    return {"acc": correct_answers / total_answers}
