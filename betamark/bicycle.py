# Note from Laurence: I removed a couple of entires after checking a few for BICYCLE presence/absence.

import tqdm

# # Train dataset
LIST_OF_BICYCLES = [
    "http://images.cocodataset.org/train2017/000000483108.jpg",
    "http://images.cocodataset.org/train2017/000000293802.jpg",
    "http://images.cocodataset.org/train2017/000000079841.jpg",
    "http://images.cocodataset.org/train2017/000000515289.jpg",
    "http://images.cocodataset.org/train2017/000000562150.jpg",
    "http://images.cocodataset.org/train2017/000000412151.jpg",
    "http://images.cocodataset.org/train2017/000000462565.jpg",
    "http://images.cocodataset.org/train2017/000000509822.jpg",
    "http://images.cocodataset.org/train2017/000000321107.jpg",
    "http://images.cocodataset.org/train2017/000000061181.jpg",
    "http://images.cocodataset.org/train2017/000000018783.jpg",
    "http://images.cocodataset.org/train2017/000000012896.jpg",
    "http://images.cocodataset.org/train2017/000000465692.jpg",
    "http://images.cocodataset.org/train2017/000000391584.jpg",
    "http://images.cocodataset.org/train2017/000000241350.jpg",
    "http://images.cocodataset.org/train2017/000000438024.jpg",
    "http://images.cocodataset.org/train2017/000000442726.jpg",
    "http://images.cocodataset.org/train2017/000000435937.jpg",
    "http://images.cocodataset.org/train2017/000000292819.jpg",
    "http://images.cocodataset.org/train2017/000000157416.jpg",
    "http://images.cocodataset.org/train2017/000000010393.jpg",
    "http://images.cocodataset.org/train2017/000000084540.jpg",
    "http://images.cocodataset.org/train2017/000000007125.jpg",
    "http://images.cocodataset.org/train2017/000000507249.jpg",
    "http://images.cocodataset.org/train2017/000000075923.jpg",
    "http://images.cocodataset.org/train2017/000000240918.jpg",
    "http://images.cocodataset.org/train2017/000000122302.jpg",
    "http://images.cocodataset.org/train2017/000000140006.jpg",
    "http://images.cocodataset.org/train2017/000000536444.jpg",
    "http://images.cocodataset.org/train2017/000000344271.jpg",
    "http://images.cocodataset.org/train2017/000000420081.jpg",
    "http://images.cocodataset.org/train2017/000000148668.jpg",
    "http://images.cocodataset.org/train2017/000000390137.jpg",
    "http://images.cocodataset.org/train2017/000000114183.jpg",
    "http://images.cocodataset.org/train2017/000000020307.jpg",
    "http://images.cocodataset.org/train2017/000000280736.jpg",
    "http://images.cocodataset.org/train2017/000000536321.jpg",
    "http://images.cocodataset.org/train2017/000000188146.jpg",
    "http://images.cocodataset.org/train2017/000000559312.jpg",
    "http://images.cocodataset.org/train2017/000000535808.jpg",
    "http://images.cocodataset.org/train2017/000000451944.jpg",
    "http://images.cocodataset.org/train2017/000000212558.jpg",
    "http://images.cocodataset.org/train2017/000000377867.jpg",
    "http://images.cocodataset.org/train2017/000000139291.jpg",
    "http://images.cocodataset.org/train2017/000000456323.jpg",
    "http://images.cocodataset.org/train2017/000000549386.jpg",
    "http://images.cocodataset.org/train2017/000000254491.jpg",
    "http://images.cocodataset.org/train2017/000000314515.jpg",
    "http://images.cocodataset.org/train2017/000000415904.jpg",
    "http://images.cocodataset.org/train2017/000000101636.jpg",
    "http://images.cocodataset.org/train2017/000000315173.jpg",
    "http://images.cocodataset.org/train2017/000000260627.jpg",
    "http://images.cocodataset.org/train2017/000000001722.jpg",
    "http://images.cocodataset.org/train2017/000000031092.jpg",
    "http://images.cocodataset.org/train2017/000000556205.jpg",
    "http://images.cocodataset.org/train2017/000000049097.jpg",
    "http://images.cocodataset.org/train2017/000000070815.jpg",
    "http://images.cocodataset.org/train2017/000000467000.jpg",
    "http://images.cocodataset.org/train2017/000000416733.jpg",
    "http://images.cocodataset.org/train2017/000000203912.jpg",
    "http://images.cocodataset.org/train2017/000000408143.jpg",
    "http://images.cocodataset.org/train2017/000000120340.jpg",
    "http://images.cocodataset.org/train2017/000000124462.jpg",
    "http://images.cocodataset.org/train2017/000000142718.jpg",
    "http://images.cocodataset.org/train2017/000000108838.jpg",
    "http://images.cocodataset.org/train2017/000000445309.jpg",
    "http://images.cocodataset.org/train2017/000000140197.jpg",
    "http://images.cocodataset.org/train2017/000000012993.jpg",
    "http://images.cocodataset.org/train2017/000000111099.jpg",
    "http://images.cocodataset.org/train2017/000000215867.jpg",
    "http://images.cocodataset.org/train2017/000000565085.jpg",
    "http://images.cocodataset.org/train2017/000000314986.jpg",
    "http://images.cocodataset.org/train2017/000000158708.jpg",
    "http://images.cocodataset.org/train2017/000000263961.jpg",
    "http://images.cocodataset.org/train2017/000000192128.jpg",
    "http://images.cocodataset.org/train2017/000000377832.jpg",
    "http://images.cocodataset.org/train2017/000000187286.jpg",
    "http://images.cocodataset.org/train2017/000000195510.jpg",
    "http://images.cocodataset.org/train2017/000000406949.jpg",
    "http://images.cocodataset.org/train2017/000000330455.jpg",
]


LIST_OF_NON_BICYCLES = [
    "http://images.cocodataset.org/train2017/000000522418.jpg",
    "http://images.cocodataset.org/train2017/000000184613.jpg",
    "http://images.cocodataset.org/train2017/000000318219.jpg",
    "http://images.cocodataset.org/train2017/000000554625.jpg",
    "http://images.cocodataset.org/train2017/000000574769.jpg",
    "http://images.cocodataset.org/train2017/000000060623.jpg",
    "http://images.cocodataset.org/train2017/000000309022.jpg",
    "http://images.cocodataset.org/train2017/000000005802.jpg",
    "http://images.cocodataset.org/train2017/000000222564.jpg",
    "http://images.cocodataset.org/train2017/000000118113.jpg",
    "http://images.cocodataset.org/train2017/000000193271.jpg",
    "http://images.cocodataset.org/train2017/000000224736.jpg",
    "http://images.cocodataset.org/train2017/000000403013.jpg",
    "http://images.cocodataset.org/train2017/000000374628.jpg",
    "http://images.cocodataset.org/train2017/000000328757.jpg",
    "http://images.cocodataset.org/train2017/000000384213.jpg",
    "http://images.cocodataset.org/train2017/000000086408.jpg",
    "http://images.cocodataset.org/train2017/000000372938.jpg",
    "http://images.cocodataset.org/train2017/000000386164.jpg",
    "http://images.cocodataset.org/train2017/000000223648.jpg",
    "http://images.cocodataset.org/train2017/000000204805.jpg",
    "http://images.cocodataset.org/train2017/000000113588.jpg",
    "http://images.cocodataset.org/train2017/000000384553.jpg",
    "http://images.cocodataset.org/train2017/000000337264.jpg",
    "http://images.cocodataset.org/train2017/000000368402.jpg",
    "http://images.cocodataset.org/train2017/000000012448.jpg",
    "http://images.cocodataset.org/train2017/000000542145.jpg",
    "http://images.cocodataset.org/train2017/000000540186.jpg",
    "http://images.cocodataset.org/train2017/000000242611.jpg",
    "http://images.cocodataset.org/train2017/000000051191.jpg",
    "http://images.cocodataset.org/train2017/000000269105.jpg",
    "http://images.cocodataset.org/train2017/000000294832.jpg",
    "http://images.cocodataset.org/train2017/000000144941.jpg",
    "http://images.cocodataset.org/train2017/000000173350.jpg",
    "http://images.cocodataset.org/train2017/000000060760.jpg",
    "http://images.cocodataset.org/train2017/000000324266.jpg",
    "http://images.cocodataset.org/train2017/000000166532.jpg",
    "http://images.cocodataset.org/train2017/000000262284.jpg",
    "http://images.cocodataset.org/train2017/000000360772.jpg",
    "http://images.cocodataset.org/train2017/000000191381.jpg",
    "http://images.cocodataset.org/train2017/000000111076.jpg",
    "http://images.cocodataset.org/train2017/000000340559.jpg",
    "http://images.cocodataset.org/train2017/000000258985.jpg",
    "http://images.cocodataset.org/train2017/000000229643.jpg",
    "http://images.cocodataset.org/train2017/000000125059.jpg",
    "http://images.cocodataset.org/train2017/000000455483.jpg",
    "http://images.cocodataset.org/train2017/000000436141.jpg",
    "http://images.cocodataset.org/train2017/000000129001.jpg",
    "http://images.cocodataset.org/train2017/000000232262.jpg",
    "http://images.cocodataset.org/train2017/000000166323.jpg",
    "http://images.cocodataset.org/train2017/000000580041.jpg",
    "http://images.cocodataset.org/train2017/000000326781.jpg",
    "http://images.cocodataset.org/train2017/000000387362.jpg",
    "http://images.cocodataset.org/train2017/000000138079.jpg",
    "http://images.cocodataset.org/train2017/000000556616.jpg",
    "http://images.cocodataset.org/train2017/000000472621.jpg",
    "http://images.cocodataset.org/train2017/000000192440.jpg",
    "http://images.cocodataset.org/train2017/000000086320.jpg",
    "http://images.cocodataset.org/train2017/000000256668.jpg",
    "http://images.cocodataset.org/train2017/000000383445.jpg",
    "http://images.cocodataset.org/train2017/000000565797.jpg",
    "http://images.cocodataset.org/train2017/000000081922.jpg",
    "http://images.cocodataset.org/train2017/000000050125.jpg",
    "http://images.cocodataset.org/train2017/000000364521.jpg",
    "http://images.cocodataset.org/train2017/000000394892.jpg",
    "http://images.cocodataset.org/train2017/000000001146.jpg",
    "http://images.cocodataset.org/train2017/000000310391.jpg",
    "http://images.cocodataset.org/train2017/000000097434.jpg",
    "http://images.cocodataset.org/train2017/000000463836.jpg",
    "http://images.cocodataset.org/train2017/000000241876.jpg",
    "http://images.cocodataset.org/train2017/000000156832.jpg",
    "http://images.cocodataset.org/train2017/000000270721.jpg",
    "http://images.cocodataset.org/train2017/000000462341.jpg",
    "http://images.cocodataset.org/train2017/000000310103.jpg",
    "http://images.cocodataset.org/train2017/000000032992.jpg",
    "http://images.cocodataset.org/train2017/000000122851.jpg",
    "http://images.cocodataset.org/train2017/000000540763.jpg",
    "http://images.cocodataset.org/train2017/000000138246.jpg",
    "http://images.cocodataset.org/train2017/000000197254.jpg",
    "http://images.cocodataset.org/train2017/000000032907.jpg",
]


# from PIL import Image
# import requests


# from scipy import misc
import imageio
import requests
from io import BytesIO


def run_eval(user_func) -> dict:
    correct_answers = 0
    total_answers = 0
    for i in tqdm.trange(len(LIST_OF_BICYCLES)):
        res = requests.get(LIST_OF_BICYCLES[i])
        np_img = imageio.v2.imread(BytesIO(res.content))
        model_resp = user_func(np_img)

        total_answers += 1
        if model_resp == 1:
            correct_answers += 1

    for i in tqdm.trange(len(LIST_OF_NON_BICYCLES)):
        res = requests.get(LIST_OF_NON_BICYCLES[i])
        np_img = imageio.v2.imread(BytesIO(res.content))
        model_resp = user_func(np_img)

        total_answers += 1
        if model_resp == 0:
            correct_answers += 1

    acc = correct_answers / total_answers
    return {"acc": acc}
