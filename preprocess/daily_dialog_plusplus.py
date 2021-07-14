import argparse
import json


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
    parser.add_argument("--dataset_src", "-ds", choices=["daily_dialog++"], type=str,
                        default="daily_dialog++", help="Source raw dataset name")
    parser.add_argument()

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    data = load_raw_data("../data/raw/dailydialog++/dev.json")
    print(data[0]["context"])
