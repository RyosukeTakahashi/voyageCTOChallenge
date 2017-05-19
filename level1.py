import io
import json
import random

# レビュイーのidとエンジニアリストをもとに、
# レビュアー候補3人をランダムに選択し、カンマ区切りで標準出力に出力するプログラムを書け。
# レビュアー候補3人にレビュイーは含まれないこととする。
# レビュアー候補3人のうち、同じチームのエンジニアが1人以上かつ違うチームのエンジニアが1人以上含まれていることとする。
# 候補がいない/足りない場合、そこには"N/A"と出力する。
# e.g. b,d,N/A

json_engineers = open('/data/level1.json')

engineers_dict = {
    "engineers": [
        {"id": "a", "team": "pex"},
        {"id": "b", "team": "pex"},
        {"id": "c", "team": "pex"},
        {"id": "d", "team": "fluct"},
        {"id": "e", "team": "fluct"},
        {"id": "f", "team": "fluct"},
        {"id": "g", "team": "fintech"},
        {"id": "h", "team": "fintech"},
        {"id": "i", "team": "fintech"},
        {"id": "j", "team": "hrtech"}
    ]
}


def choose_reviewee():
    engineers_count = len(engineers_dict["engineers"])
    engineer_index = random.randint(0, engineers_count - 1)
    reviewee = engineers_dict["engineers"][engineer_index]
    return reviewee


def get_engineer_id(engineer):
    return engineer["id"]


def get_engineer_team(engineer):
    return engineer["team"]


def get_reviewee_teammate_engineer_list(reviewee, engineers_dict):
    reviewee_team = get_engineer_team(reviewee)
    reviewee_id = get_engineer_id(reviewee)
    engineers = engineers_dict["engineers"]
    teammate = [engineer for engineer in engineers if
                engineers["team"] == reviewee_team and engineers["id"] != reviewee_id]

    return teammate


def get_reviewee_other_teammember_engineer_list(reviewee, engineers_dict):
    reviewee_team = get_engineer_team(reviewee)
    engineers = engineers_dict["engineers"]
    other_teammember = [engineer for engineer in engineers if
                        engineers_dict["engineers"]["team"] != reviewee_team]

    return other_teammember


def choose_teammate_reviewer(reviewee):
    teammate = get_reviewee_teammate_engineer_list(reviewee, engineers_dict)
    if teammate is None:
        engineer_index = random.randint(0, len(teammate) - 1)
        reviewer = teammate[engineer_index]
    else:
        reviewer = {"id": "N/A", "team":"N/A"}

    return reviewer


def choose_other_teammember_reviewer(reviewee):
    other_teammember = get_reviewee_other_teammember_engineer_list(reviewee, engineers_dict)
    engineer_index = random.randint(0, len(other_teammember) - 1)
    reviewer = other_teammember[engineer_index]

    return reviewer
