import numpy as np

num_of_lamps, num_of_operation = map(int, input().split())
intensitys = np.array(list(map(int, input().split())))

coordinates = np.arange(1, len(intensitys) + 1)

intensity_area_min = []
intensity_area_max = []

for o in range(num_of_operation):
    intensity_area_min = coordinates - intensitys - 0.5
    intensity_area_max = coordinates + intensitys + 0.5

    # i + 1が自分の座標
    for i in range(num_of_lamps):
        if intensitys[i] < num_of_lamps:
            # 自分より大きい（自分除く）の座標indexのminリストの中から自分の座標より小さいものを探してカウント
            min_count = np.count_nonzero(intensity_area_min[i+1:] <= i + 1)
            # 自分より小さい（自分除く）の座標indexのmaxリストの中から自分の座標より大きいものを探してカウント
            max_count = np.count_nonzero(intensity_area_max[:i] >= i + 1)

            # + 1は自分
            intensitys[i] = min_count + max_count + 1

    if np.all(intensitys >= num_of_lamps):
        break

out = ",".join(map(str, intensitys))
print(out.replace(',', ' '))
