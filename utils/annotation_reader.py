from zipfile import ZipFile
import glob
import pandas as pd

file_list = glob.glob("data/*.zip")

print("total files:", len(file_list))

columns = ["file_name", "timestamp", "car",
           "truck", "bicycle", "motorbike", "bus", "total"]

data = pd.DataFrame(columns=columns)

count = 0

for file in file_list:
    # opening the zip file in READ mode
    with ZipFile(file, 'r') as zip:
        zip.extractall()
        print('Done extracting', file, "...")
    labels = pd.read_fwf("gt/labels.txt", header=None, names=["label"])
    label_list = [row["label"] for index, row in labels.iterrows()]
    gt = pd.read_csv("gt/gt.txt", sep=",", header=None, names=[
                     "frame_id", "track_id", "x", "y", "w", "h", "not_ignored", "class_id", "visibility"])

    total_frames = gt["frame_id"].max()
    try:
        total_frames = int(total_frames)
    except ValueError:
        total_frames = 0

    frames = [{"file_name": file, "timestamp": (id+1)*0.5}
              for id in range(19)]

    if total_frames > 21:
        print(f"......load {file}, total frame: {total_frames}.")
        count += 1

    outlined = False

    for idx, row in gt.iterrows():
        # 19: 1-19; 20: 1-20; 21: 1-21
        frame_id = int(row["frame_id"])
        if total_frames == 20 or total_frames == 21:
            frame_id = int(row["frame_id"]) - 1
        if total_frames == 21 and frame_id == 20:
            continue
        if total_frames > 21 and frame_id % 15 != 0:
            continue
        if total_frames > 21:
            # continue
            # print(frame_id)
            frame_id = frame_id // 15 - 1

        if frame_id == 0:
            continue
        row_id = frame_id - 1
        # print(frame_id, row_id)
        ctg = label_list[int(row["class_id"] - 1)]
        if ctg == "person":
            continue
        frames[row_id][ctg] = frames[row_id].get(ctg, 0) + 1
        frames[row_id]["total"] = frames[row_id].get("total", 0) + 1
        if frames[row_id].get(ctg, 0) > 50:
            outlined = True

    if outlined:
        print(frames)
    df = pd.DataFrame.from_records(frames, columns=columns)
    data = data.append(df)


data.to_csv("annotations_by_frame.csv")
