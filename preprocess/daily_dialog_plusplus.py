import os
import argparse
import importlib

ALL_RESPONSE_TYPES = [
    "positive_responses",
    "adversarial_negative_responses",
    "random_negative_responses"
]

CLASS_NAME_MAP = {
    "processor_daily_dialog_plusplus_mlr":
    "daily_dialog_plus_plus_mlr_loss_processor"
}

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_src", "-ds", choices=["daily_dialog++"], type=str,
                        default="daily_dialog++", help="Source raw dataset name")
    parser.add_argument()

    args = parser.parse_args()
    return args



