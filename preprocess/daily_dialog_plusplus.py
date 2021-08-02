import json
import argparse
from transformers import AutoTokenizer, AutoModel


def load_raw_data(file_path: str):
    """ 加载原始数据文本

    :param file_path: 原始文本地址
    :return dialog_data: 样本列表
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            dialog_data = json.load(file)
    except json.JSONDecodeError:
        with open(file_path, "r", encoding="utf-8") as file:
            dialog_data = [json.loads(line) for line in file.readlines()]
    return dialog_data


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", "-mn", type=str, required=False,
                        default="bert-base-uncased", help="transformers model name")
    parser.add_argument("--return_tensors", "-rt", type=str, required=False, default="pt", help="cal framework")
    parser.add_argument("--max_length", "-ml", type=int, required=False, default=512, help="sentence max length")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_opt()
    raw_data = load_raw_data("../data/raw/dailydialog++/dev.json")
    # with open("../data/preprocess/preprocess_data.txt")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    pt_model = AutoModel.from_pretrained(args.model_name)
    inputs = tokenizer("Hello World! [SEP]", return_tensors="pt", padding=True, truncation=True, max_length=args.max_length)
    outputs = pt_model(**inputs)
    print(outputs.last_hidden_state.size())
    # print(inputs["input_ids"].numpy().tolist())
