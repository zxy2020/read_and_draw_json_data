import json
import os
import matplotlib.pyplot as plt


fid_dirs_1024 = '/home/ai004/work/zeng2020.08.05/faceAgeEdit/stargan-v2/1024/0922/eval'
fid_dirs_512 = "/home/ai004/work/zeng2020.08.05/faceAgeEdit/stargan-v2/0917/expr/0917/eval"

x = [x * 8000 for x in range(1, 13)]
y2 = [14] * len(x)


def get_all_fid(fid_dirs):
    fids_jsons = os.listdir(fid_dirs)

    # fids_jsons = fids_jsons.sort()

    fid_keys = ["FID_latent/young2old", "FID_latent/old2young", "FID_latent/mean",
                "FID_reference/young2old", "FID_reference/old2young", "FID_reference/mean", ]

    FID_latent_young2old = []
    FID_latent_old2young = []
    FID_latent_mean = []
    FID_reference_mean = []

    for fid in fids_jsons:
        if fid[:3] != "FID":
            continue
        if fid[-5:] != '.json':
            continue
        if fid[-11:-5] == 'latent':
            continue
        print(fid)
        path_fid_json = os.path.join(fid_dirs, fid)
        file = open(path_fid_json)
        fileJson = json.load(file)
        # print(fileJson)
        keys = list(fileJson.keys())
        values = list(fileJson.values())

        if fid_keys[3] in keys:
            FID_latent_young2old.append(fileJson[fid_keys[3]])
        if fid_keys[4] in keys:
            FID_latent_old2young.append(fileJson[fid_keys[4]])
        if "FID_latent/mean" in keys:
            FID_latent_mean.append(fileJson["FID_latent/mean"])
        if "FID_reference/mean" in keys:
            FID_reference_mean.append(fileJson["FID_reference/mean"])
    return FID_latent_young2old, FID_latent_old2young


def draw(x, y, y2, label1, label2, color='b'):
    plt.plot(x, y, label=label1, color=color)
    plt.plot(x, y2, label=label2, color=color)


if __name__ == "__main__":
    FID_latent_young2old, FID_latent_old2young = get_all_fid(fid_dirs_512)
    draw(x, FID_latent_young2old, FID_latent_old2young, "512_young2old", "512_old2young")
    FID_latent_young2old, FID_latent_old2young = get_all_fid(fid_dirs_1024)
    draw(x, FID_latent_young2old, FID_latent_old2young, "1024_young2old", "1024_old2young", color='r')

    #
    plt.plot(x, y2, label="fid_stargan_demo", color='y')
    plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))  # 打开图线命名

    savename = "reference_FID_512_VS_1024"
    plt.title(savename)

    plt.savefig(savename + ".png", dpi=120)
# plt.plot(x, FID_latent_old2young, label="FID_latent_old2young")


# # plt.show()
