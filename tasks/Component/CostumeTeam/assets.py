from module.atom.image import RuleImage


class CostumeTeamAssets:
    """组队场景自定义识别资源。"""

    I_FIRE_1 = RuleImage(
        roi_front=(1179, 602, 81, 74),
        roi_back=(1179, 602, 81, 74),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_fire.png",
    )
    I_ADD_1_1 = RuleImage(
        roi_front=(596, 241, 114, 51),
        roi_back=(569, 196, 186, 161),
        threshold=0.9,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_add_1.png",
    )
    I_ADD_2_1 = RuleImage(
        roi_front=(1013, 249, 100, 100),
        roi_back=(970, 151, 193, 220),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_add_2.png",
    )
    I_ADD_5_1_1 = RuleImage(
        roi_front=(370, 243, 100, 100),
        roi_back=(370, 243, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_add_5_1.png",
    )
    I_ADD_5_2_1 = RuleImage(
        roi_front=(612, 263, 100, 100),
        roi_back=(612, 263, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_add_5_2.png",
    )
    I_ADD_5_3_1 = RuleImage(
        roi_front=(862, 243, 100, 100),
        roi_back=(862, 243, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_add_5_3.png",
    )
    I_ADD_5_4_1 = RuleImage(
        roi_front=(1118, 228, 100, 100),
        roi_back=(1118, 228, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team1/team1_add_5_4.png",
    )
    I_ADD_1_2 = RuleImage(
        roi_front=(596, 241, 114, 51),
        roi_back=(569, 196, 186, 161),
        threshold=0.9,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_add_1.png",
    )
    I_FIRE_2 = RuleImage(
        roi_front=(1181, 615, 81, 74),
        roi_back=(1181, 615, 81, 74),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_fire.png",
    )
    I_ADD_2_2 = RuleImage(
        roi_front=(1013, 249, 100, 100),
        roi_back=(970, 151, 193, 220),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_add_2.png",
    )
    I_ADD_5_1_2 = RuleImage(
        roi_front=(370, 243, 100, 100),
        roi_back=(370, 243, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_add_5_1.png",
    )
    I_ADD_5_2_2 = RuleImage(
        roi_front=(612, 263, 100, 100),
        roi_back=(612, 263, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_add_5_2.png",
    )
    I_ADD_5_3_2 = RuleImage(
        roi_front=(862, 243, 100, 100),
        roi_back=(862, 243, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_add_5_3.png",
    )
    I_ADD_5_4_2 = RuleImage(
        roi_front=(1118, 228, 100, 100),
        roi_back=(1118, 228, 100, 100),
        threshold=0.8,
        method="Template matching",
        file="./tasks/Component/CostumeTeam/team2/team2_add_5_4.png",
    )
