import json

import tqdm

import pkgutil

FILEPATH = pkgutil.get_data("betamark", "data/arc-agi_evaluation_challenges.json")

# FILEPATH = pkgutil.get_data(__name__, "data/arc-agi_evaluation_challenges.json")
print(FILEPATH)


EVAL_CHALLENGES_FILEPATH = "betamark/data/arc-agi_evaluation_challenges.json"
EVAL_SOLUTIONS_FILEPATH = "betamark/data/arc-agi_evaluation_solutions.json"


eval_challenges_data = json.load(open(EVAL_CHALLENGES_FILEPATH, "r"))
eval_solutions_data = json.load(open(EVAL_SOLUTIONS_FILEPATH, "r"))


def run_eval(user_func) -> dict:
    total_score = 0
    for key_name in tqdm.tqdm(eval_challenges_data.keys()):
        # print(key_name)
        model_input = eval_challenges_data[key_name]
        ground_truth = eval_solutions_data[key_name]
        y_pred = user_func(model_input)
        if len(ground_truth[0]) != len(y_pred):
            continue
        elif len(ground_truth[0][0]) != len(y_pred[0]):
            continue
        else:
            if ground_truth[0] == y_pred:
                total_score += 1  # add 0.5 each time the model predicts correctly

    acc = total_score / len(list(eval_challenges_data.keys()))
    return {"acc": acc}


if __name__ == "__main__":
    user_func = lambda x: [
        [3, 2, 3, 2, 3, 2],
        [7, 8, 7, 8, 7, 8],
        [2, 3, 2, 3, 2, 3],
        [8, 7, 8, 7, 8, 7],
        [3, 2, 3, 2, 3, 2],
        [7, 8, 7, 8, 7, 8],
    ]
    acc_result = run_eval(user_func=user_func)
    print(acc_result)
