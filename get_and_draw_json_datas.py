import json
import os
import matplotlib.pyplot as plt

#读取并解析json数据
def get_all_fid(fid_dirs):
    fids_jsons = os.listdir(fid_dirs)
    # fids_jsons = fids_jsons.sort()
    fid_keys = ["FID_latent/young2old", "FID_latent/old2young", "FID_latent/mean"]  # json文件内的关键字段

    FID_latent_young2old = []
    FID_latent_old2young = []
    FID_latent_mean = []

    for fid in fids_jsons:
        if fid[-5:] != '.json':  # 如果文件后缀不是json文件，跳过
            continue
        print(fid)
        path_fid_json = os.path.join(fid_dirs, fid)
        file = open(path_fid_json)
        fileJson = json.load(file)
        # print(fileJson)
        keys = list(fileJson.keys())    # 获取json中所有的键值
        values = list(fileJson.values())

        if fid_keys[0] in keys:
            FID_latent_young2old.append(fileJson[fid_keys[0]])
        if fid_keys[1] in keys:
            FID_latent_old2young.append(fileJson[fid_keys[1]])
        # if fid_keys[2] in keys:
        #     FID_latent_mean.append(fileJson[fid_keys[2]])

    return FID_latent_young2old, FID_latent_old2young,len(fids_jsons)


def draw(x, y, y2, label1, label2, c1='b',c2='r'):
    plt.plot(x, y, label=label1, color=c1)
    plt.plot(x, y2, label=label2, color=c2)

#主函数
if __name__ == "__main__":
    fid_dirs = './json'  # 修改成自己的目录
    FID_latent_young2old, FID_latent_old2young,number_of_jsons= get_all_fid(fid_dirs)
    x = [x * 8000 for x in range(1, number_of_jsons+1)]  #这些json是迭代8000次生成，坐标值可根据实际随意，但是要与json文件个数对应，本博客使用的是10
    draw(x, FID_latent_young2old, FID_latent_old2young, label1="fid_young2old", label2="fid_old2young")
    plt.legend()  # 将线的注解label1,label2显示在图上
    savename= "FID_latent_across_iters"
    plt.title(savename)   #给图添加标题
    plt.savefig(savename + ".png", dpi=120)
    plt.show()  #显示在在保存后面，否则保存是空白图
