import datasets
import tqdm

VERBOSE = False

ds = datasets.load_dataset("tinyBenchmarks/tinyMMLU")

if VERBOSE:
    print(ds)
    print(ds["dev"][0]["input_formatted"])
    print("----------")
    print(ds["dev"][0]["answer"])


def strip_model_resp(model_resp: str) -> str:
    assert type(model_resp) == str
    model_resp = model_resp.strip()
    model_resp = model_resp[0]
    model_resp = model_resp.upper()
    return model_resp


def run_eval(user_func) -> dict:
    answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    correct_count = 0
    total = 0
    for i in tqdm.trange(len(ds["dev"])):
        input_formtted = ds["dev"][i]["input_formatted"]
        ground_truth_answer = ds["dev"][i]["answer"]
        predicted_answer = answer_map[strip_model_resp(user_func(input_formtted))]
        total += 1
        if ground_truth_answer == predicted_answer:
            correct_count += 1
    acc = correct_count / total
    return {"acc": acc}


def run_validation(user_func) -> dict:
    answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    correct_count = 0
    total = 0
    for i in tqdm.trange(len(ds["test"])):
        input_formtted = ds["test"][i]["input_formatted"]
        ground_truth_answer = ds["test"][i]["answer"]
        predicted_answer = answer_map[strip_model_resp(user_func(input_formtted))]
        total += 1
        if ground_truth_answer == predicted_answer:
            correct_count += 1
    acc = correct_count / total
    return {"acc": acc}


if __name__ == "__main__":

    def placeholder(x):
        return "A"

    print(run_validation(user_func=placeholder))
