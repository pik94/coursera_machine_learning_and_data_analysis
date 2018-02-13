import re
import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift


def write_to_csv(data, file):
    """
    Метод пишет данные в csv-файл. Входные данные подаются в виде списка. В файле будет строка вида:
    text1,text2,text3,text4,text5\n
    :param data: список
    :param file: файл, куда надо писать
    :return: None
    """
    for i in range(0, 6):
        if i != 5:
            file.write(data[i] + ",")
        else:
            file.write(data[i] + "\n")
    return


def create_csv_from_txt(file_txt, file_csv):
    line = file_txt.readline()
    header = re.findall("[\w]+", line)
    write_to_csv(header, file_csv)

    file_txt.readline()

    idx = 0
    for line in file_txt:
        data = re.split("\|", line)
        if len(data) < 6:
            break
        else:
            for i in range(0, 5):
                data[i] = re.findall("[\s]*([\w\.\-]*)", data[i])[0]
            data[5] = re.findall("[\s]*([\w\-: ]*)", data[5])[0]
            idx += 1
            if data[3] == "" or data[4] == "":
                continue
            write_to_csv(data, file_csv)
    return


if __name__ == "__main__":
    with open("checkins.dat", "r") as file_txt:
        with open("data.csv", "w") as file_csv:
            create_csv_from_txt(file_txt, file_csv)

    # имеется одна странность: если файл data.csv не закрыт, то read_csv читает меньше строк, чем нужно
    # а если строк совсем мало, то бросается исключение
    data = pd.read_csv("data.csv", header=0)
    # print(data)
    print(len(data))

    X = data.values[0:100000, 3:5]
    model = MeanShift(bandwidth=0.1)
    model.fit(X)

    labels = model.labels_
    cluster_centers = model.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

