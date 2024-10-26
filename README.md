# betamark

An experimental benchmark meant for portability and finite compute.

### Installation Instructions

```bash
pip install git+https://github.com/exobyte-labs/betamark.git
```

To update the installation:

```bash
pip install git+https://github.com/exobyte-labs/betamark.git -U
```

For HackOS 1, the current code base uses train or dev datasets. For the final benchmarking near demo time, this repository will be updated to use validation datasets.

### External Datasets of Interest:

* Genomic Benchmarks (with dataset for OCR): [root GitHub repo](https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks), [OCR](https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks/tree/main/datasets/human_ocr_ensembl)
* MS COCO: https://cocodataset.org/#home
* MMLU: https://paperswithcode.com/dataset/mmlu


### TinyMMLU Eval

```python
from betamark import tiny_mmlu

def placeholder(x):
    """
    Params:
    -------
    x: string that is a text prompt

    Returns:
    --------
    y_pred: str, ideally a single character {A, B, C, D} corresponding to a multiple choice answer from MMLU or tinyMMLU
    """
    return "A"

tiny_mmlu.run_eval(user_func=placeholder)

```

### OCR Binary Classification

```python
from betamark import ocr

def placeholder(x):
    """
    Params:
    -------
    x: string representing a genomic sequence

    Returns:
    --------
    y_pred: int where 0 is negative (not an OCR) or 1 (is an OCR)
    """

    return 0

ocr.run_eval(user_func=placeholder)

```

### Bike Detection on MS Coco Subsample

```python
from betamark import bicycle

def placeholder(x):
    """
    Params:
    -------
    x: NumPy array representation of an image (dimensions are non-fixed)

    Returns:
    --------
    y_pred: int where 0 is negative (no bicycle) or 1 (there is a bicycle)
    """
    return 0

bicycle.run_eval(user_func=placeholder)

```

### Example of Running Validation Code

When the validation code is pushed at around 2:00 PM ET (Saturday, Oct. 26), please do the following:

(1) Run the following command to update `betamark`

```bash
pip install git+https://github.com/exobyte-labs/betamark.git -U
```

(2) Replace `run_eval` with `run_validation`, for example, the bicycle case becomes:

```python
bicycle.run_validation(user_func=placeholder)
```

The function static types are the same, so you don't need to worry about integration. The same replacement applies for `ocr` and `tiny_mmlu`.
