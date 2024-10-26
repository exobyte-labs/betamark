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


LIST_VALIDATION_BICYCLES = [
    "http://images.cocodataset.org/val2017/000000087038.jpg",
    "http://images.cocodataset.org/val2017/000000174482.jpg",
    "http://images.cocodataset.org/val2017/000000296649.jpg",
    "http://images.cocodataset.org/val2017/000000301135.jpg",
    "http://images.cocodataset.org/val2017/000000356387.jpg",
    "http://images.cocodataset.org/val2017/000000038829.jpg",
    "http://images.cocodataset.org/val2017/000000361103.jpg",
    "http://images.cocodataset.org/val2017/000000403565.jpg",
    "http://images.cocodataset.org/val2017/000000441586.jpg",
    "http://images.cocodataset.org/val2017/000000101762.jpg",
    "http://images.cocodataset.org/val2017/000000203317.jpg",
    "http://images.cocodataset.org/val2017/000000074058.jpg",
    "http://images.cocodataset.org/val2017/000000210273.jpg",
    "http://images.cocodataset.org/val2017/000000169996.jpg",
    "http://images.cocodataset.org/val2017/000000226417.jpg",
    "http://images.cocodataset.org/val2017/000000274687.jpg",
    "http://images.cocodataset.org/val2017/000000010363.jpg",
    "http://images.cocodataset.org/val2017/000000476704.jpg",
    "http://images.cocodataset.org/val2017/000000138639.jpg",
    "http://images.cocodataset.org/val2017/000000139099.jpg",
    "http://images.cocodataset.org/val2017/000000152771.jpg",
    "http://images.cocodataset.org/val2017/000000309391.jpg",
    "http://images.cocodataset.org/val2017/000000432553.jpg",
    "http://images.cocodataset.org/val2017/000000196843.jpg",
    "http://images.cocodataset.org/val2017/000000045596.jpg",
    "http://images.cocodataset.org/val2017/000000070774.jpg",
    "http://images.cocodataset.org/val2017/000000193926.jpg",
    "http://images.cocodataset.org/val2017/000000319607.jpg",
    "http://images.cocodataset.org/val2017/000000492077.jpg",
    "http://images.cocodataset.org/val2017/000000357737.jpg",
    "http://images.cocodataset.org/val2017/000000162858.jpg",
    "http://images.cocodataset.org/val2017/000000076416.jpg",
    "http://images.cocodataset.org/val2017/000000508370.jpg",
    "http://images.cocodataset.org/val2017/000000577932.jpg",
    "http://images.cocodataset.org/val2017/000000144333.jpg",
    "http://images.cocodataset.org/val2017/000000261888.jpg",
    "http://images.cocodataset.org/val2017/000000135670.jpg",
    "http://images.cocodataset.org/val2017/000000011149.jpg",
    "http://images.cocodataset.org/val2017/000000259640.jpg",
    "http://images.cocodataset.org/val2017/000000008211.jpg",
    "http://images.cocodataset.org/val2017/000000306136.jpg",
    "http://images.cocodataset.org/val2017/000000228436.jpg",
    "http://images.cocodataset.org/val2017/000000488592.jpg",
    "http://images.cocodataset.org/val2017/000000350023.jpg",
    "http://images.cocodataset.org/val2017/000000490936.jpg",
    "http://images.cocodataset.org/val2017/000000350122.jpg",
    "http://images.cocodataset.org/val2017/000000295809.jpg",
    "http://images.cocodataset.org/val2017/000000424162.jpg",
    "http://images.cocodataset.org/val2017/000000242287.jpg",
    "http://images.cocodataset.org/val2017/000000259830.jpg",
    "http://images.cocodataset.org/val2017/000000492937.jpg",
    "http://images.cocodataset.org/val2017/000000570834.jpg",
    "http://images.cocodataset.org/val2017/000000224051.jpg",
    "http://images.cocodataset.org/val2017/000000061108.jpg",
    "http://images.cocodataset.org/val2017/000000395180.jpg",
    "http://images.cocodataset.org/val2017/000000472623.jpg",
    "http://images.cocodataset.org/val2017/000000007386.jpg",
    "http://images.cocodataset.org/val2017/000000210299.jpg",
    "http://images.cocodataset.org/val2017/000000109055.jpg",
    "http://images.cocodataset.org/val2017/000000571857.jpg",
    "http://images.cocodataset.org/val2017/000000507037.jpg",
    "http://images.cocodataset.org/val2017/000000251140.jpg",
    "http://images.cocodataset.org/val2017/000000142324.jpg",
    "http://images.cocodataset.org/val2017/000000097988.jpg",
    "http://images.cocodataset.org/val2017/000000338625.jpg",
    "http://images.cocodataset.org/val2017/000000301376.jpg",
    "http://images.cocodataset.org/val2017/000000289343.jpg",
    "http://images.cocodataset.org/val2017/000000256941.jpg",
    "http://images.cocodataset.org/val2017/000000279278.jpg",
    "http://images.cocodataset.org/val2017/000000426166.jpg",
    "http://images.cocodataset.org/val2017/000000388258.jpg",
    "http://images.cocodataset.org/val2017/000000291634.jpg",
    "http://images.cocodataset.org/val2017/000000122166.jpg",
    "http://images.cocodataset.org/val2017/000000414510.jpg",
    "http://images.cocodataset.org/val2017/000000266400.jpg",
    "http://images.cocodataset.org/val2017/000000254814.jpg",
    "http://images.cocodataset.org/val2017/000000370208.jpg",
    "http://images.cocodataset.org/val2017/000000055022.jpg",
    "http://images.cocodataset.org/val2017/000000013177.jpg",
    "http://images.cocodataset.org/val2017/000000531134.jpg",
    "http://images.cocodataset.org/val2017/000000429109.jpg",
    "http://images.cocodataset.org/val2017/000000008899.jpg",
    "http://images.cocodataset.org/val2017/000000343561.jpg",
]

LIST_VALIDATION_NON_BICICYLES = [
    "http://images.cocodataset.org/val2017/000000397133.jpg",
    "http://images.cocodataset.org/val2017/000000037777.jpg",
    "http://images.cocodataset.org/val2017/000000252219.jpg",
    "http://images.cocodataset.org/val2017/000000403385.jpg",
    "http://images.cocodataset.org/val2017/000000006818.jpg",
    "http://images.cocodataset.org/val2017/000000480985.jpg",
    "http://images.cocodataset.org/val2017/000000458054.jpg",
    "http://images.cocodataset.org/val2017/000000331352.jpg",
    "http://images.cocodataset.org/val2017/000000386912.jpg",
    "http://images.cocodataset.org/val2017/000000502136.jpg",
    "http://images.cocodataset.org/val2017/000000491497.jpg",
    "http://images.cocodataset.org/val2017/000000184791.jpg",
    "http://images.cocodataset.org/val2017/000000348881.jpg",
    "http://images.cocodataset.org/val2017/000000289393.jpg",
    "http://images.cocodataset.org/val2017/000000522713.jpg",
    "http://images.cocodataset.org/val2017/000000181666.jpg",
    "http://images.cocodataset.org/val2017/000000017627.jpg",
    "http://images.cocodataset.org/val2017/000000143931.jpg",
    "http://images.cocodataset.org/val2017/000000303818.jpg",
    "http://images.cocodataset.org/val2017/000000463730.jpg",
    "http://images.cocodataset.org/val2017/000000460347.jpg",
    "http://images.cocodataset.org/val2017/000000322864.jpg",
    "http://images.cocodataset.org/val2017/000000226111.jpg",
    "http://images.cocodataset.org/val2017/000000153299.jpg",
    "http://images.cocodataset.org/val2017/000000308394.jpg",
    "http://images.cocodataset.org/val2017/000000456496.jpg",
    "http://images.cocodataset.org/val2017/000000058636.jpg",
    "http://images.cocodataset.org/val2017/000000041888.jpg",
    "http://images.cocodataset.org/val2017/000000184321.jpg",
    "http://images.cocodataset.org/val2017/000000565778.jpg",
    "http://images.cocodataset.org/val2017/000000297343.jpg",
    "http://images.cocodataset.org/val2017/000000336587.jpg",
    "http://images.cocodataset.org/val2017/000000122745.jpg",
    "http://images.cocodataset.org/val2017/000000219578.jpg",
    "http://images.cocodataset.org/val2017/000000555705.jpg",
    "http://images.cocodataset.org/val2017/000000443303.jpg",
    "http://images.cocodataset.org/val2017/000000500663.jpg",
    "http://images.cocodataset.org/val2017/000000418281.jpg",
    "http://images.cocodataset.org/val2017/000000025560.jpg",
    "http://images.cocodataset.org/val2017/000000403817.jpg",
    "http://images.cocodataset.org/val2017/000000085329.jpg",
    "http://images.cocodataset.org/val2017/000000329323.jpg",
    "http://images.cocodataset.org/val2017/000000239274.jpg",
    "http://images.cocodataset.org/val2017/000000286994.jpg",
    "http://images.cocodataset.org/val2017/000000511321.jpg",
    "http://images.cocodataset.org/val2017/000000314294.jpg",
    "http://images.cocodataset.org/val2017/000000233771.jpg",
    "http://images.cocodataset.org/val2017/000000475779.jpg",
    "http://images.cocodataset.org/val2017/000000301867.jpg",
    "http://images.cocodataset.org/val2017/000000312421.jpg",
    "http://images.cocodataset.org/val2017/000000185250.jpg",
    "http://images.cocodataset.org/val2017/000000356427.jpg",
    "http://images.cocodataset.org/val2017/000000572517.jpg",
    "http://images.cocodataset.org/val2017/000000270244.jpg",
    "http://images.cocodataset.org/val2017/000000516316.jpg",
    "http://images.cocodataset.org/val2017/000000125211.jpg",
    "http://images.cocodataset.org/val2017/000000562121.jpg",
    "http://images.cocodataset.org/val2017/000000360661.jpg",
    "http://images.cocodataset.org/val2017/000000016228.jpg",
    "http://images.cocodataset.org/val2017/000000382088.jpg",
    "http://images.cocodataset.org/val2017/000000266409.jpg",
    "http://images.cocodataset.org/val2017/000000430961.jpg",
    "http://images.cocodataset.org/val2017/000000080671.jpg",
    "http://images.cocodataset.org/val2017/000000577539.jpg",
    "http://images.cocodataset.org/val2017/000000104612.jpg",
    "http://images.cocodataset.org/val2017/000000476258.jpg",
    "http://images.cocodataset.org/val2017/000000448365.jpg",
    "http://images.cocodataset.org/val2017/000000035197.jpg",
    "http://images.cocodataset.org/val2017/000000349860.jpg",
    "http://images.cocodataset.org/val2017/000000180135.jpg",
    "http://images.cocodataset.org/val2017/000000486438.jpg",
    "http://images.cocodataset.org/val2017/000000400573.jpg",
    "http://images.cocodataset.org/val2017/000000109798.jpg",
    "http://images.cocodataset.org/val2017/000000370677.jpg",
    "http://images.cocodataset.org/val2017/000000238866.jpg",
    "http://images.cocodataset.org/val2017/000000369370.jpg",
    "http://images.cocodataset.org/val2017/000000502737.jpg",
    "http://images.cocodataset.org/val2017/000000515579.jpg",
    "http://images.cocodataset.org/val2017/000000515445.jpg",
    "http://images.cocodataset.org/val2017/000000173383.jpg",
    "http://images.cocodataset.org/val2017/000000438862.jpg",
    "http://images.cocodataset.org/val2017/000000180560.jpg",
    "http://images.cocodataset.org/val2017/000000347693.jpg",
    "http://images.cocodataset.org/val2017/000000039956.jpg",
]

# from PIL import Image
# import requests


# from scipy import misc
from io import BytesIO

import imageio
import requests


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


def run_validation(user_func) -> dict:
    correct_answers = 0
    total_answers = 0
    for i in tqdm.trange(len(LIST_VALIDATION_BICYCLES)):
        res = requests.get(LIST_VALIDATION_BICYCLES[i])
        np_img = imageio.v2.imread(BytesIO(res.content))
        model_resp = user_func(np_img)

        total_answers += 1
        if model_resp == 1:
            correct_answers += 1

    for i in tqdm.trange(len(LIST_VALIDATION_NON_BICICYLES)):
        res = requests.get(LIST_VALIDATION_NON_BICICYLES[i])
        np_img = imageio.v2.imread(BytesIO(res.content))
        model_resp = user_func(np_img)

        total_answers += 1
        if model_resp == 0:
            correct_answers += 1

    acc = correct_answers / total_answers
    return {"acc": acc}


if __name__ == "__main__":

    def placeholder(x):
        return 0

    print(run_validation(user_func=placeholder))
