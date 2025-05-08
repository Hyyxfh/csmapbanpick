import random

def pick_map(available_maps, action):
    print(f"\n可选地图: {', '.join(available_maps)}")
    while True:
        choice = input(f"{action}，请输入地图名称: ").strip()
        if choice in available_maps:
            return choice
        print("输入无效，请重新输入有效的地图名称。")

def choose_side(team):
    while True:
        side = input(f"{team} 请选择开局方（CT 或 T）: ").strip().upper()
        if side in ["CT", "T"]:
            return side
        print("无效输入，请输入 'CT' 或 'T'。")

def bo3_veto(team_a, team_b, maps):
    print(f"\n🎮 开始 BO3 地图选择：{team_a} vs {team_b}")
    available_maps = maps.copy()

    # Ban 阶段
    ban1 = pick_map(available_maps, f"{team_a} 先 Ban")
    available_maps.remove(ban1)

    ban2 = pick_map(available_maps, f"{team_b} Ban")
    available_maps.remove(ban2)

    # Pick 阶段
    pick1 = pick_map(available_maps, f"{team_a} 选地图（地图1）")
    available_maps.remove(pick1)

    pick2 = pick_map(available_maps, f"{team_b} 选地图（地图2）")
    available_maps.remove(pick2)

    # Ban 阶段
    ban3 = pick_map(available_maps, f"{team_a} Ban")
    available_maps.remove(ban3)

    ban4 = pick_map(available_maps, f"{team_b} Ban")
    available_maps.remove(ban4)

    # 剩下的为决胜图
    decider = available_maps[0]

    # 边选交互过程
    print("\n🧭 边选环节：")
    side_first_map_team = team_b
    side_first_map_choice = choose_side(side_first_map_team)

    side_second_map_team = team_a
    side_second_map_choice = choose_side(side_second_map_team)

    decider_side_team = random.choice([team_a, team_b])
    print(f"\n🎲 随机决定决胜图边选权归 {decider_side_team}")
    decider_side_choice = choose_side(decider_side_team)

    # 输出 veto 结果
    print("\n✅ 最终地图与边选结果：\n")
    print(f"地图1：{pick1}（{team_a}选） - {team_b} 选择 CT/T：{side_first_map_choice}")
    print(f"地图2：{pick2}（{team_b}选） - {team_a} 选择 CT/T：{side_second_map_choice}")
    print(f"决胜图：{decider}（自动决定） - {decider_side_team} 选择 CT/T：{decider_side_choice}")

    print("\n📋 Veto 流程记录：")
    print(f"{team_a} Ban: {ban1}")
    print(f"{team_b} Ban: {ban2}")
    print(f"{team_a} Pick: {pick1}")
    print(f"{team_b} Pick: {pick2}")
    print(f"{team_a} Ban: {ban3}")
    print(f"{team_b} Ban: {ban4}")
    print(f"Decider: {decider}")

# 示例地图池
default_map_pool = ["Mirage", "Inferno", "Nuke", "Dust2", "Train", "Ancient", "Anubis"]

# 启动流程
if __name__ == "__main__":
    print("🔥 CS:GO BO3 地图选图系统")
    team_a = input("请输入队伍A名称: ")
    team_b = input("请输入队伍B名称: ")
    bo3_veto(team_a, team_b, default_map_pool)
