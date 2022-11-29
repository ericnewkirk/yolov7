import torch

torch.cuda.memory_reserved()

"""python train.py --workers 8 --device 0 --batch-size 12 --data data/elkrec_elk_only.yaml --img 640 640 --cfg cfg/training/elkrec_elk_only.yaml --name prelim"""

"""python detect.py --weights runs/train/prelim16/weights/best.pt --conf 0.1 --img-size 640 --source D:/ElkRecreation/2020/GS_BSM_2020_02 --device 0 --save-txt --name prelim """

25071 / 3022

"""python detect.py --weights runs/train/micro3/weights/best.pt --conf 0.1 --img-size 640 --source D:/ElkRecreation/2020/GS_BSM_2020_02 --device 0 --save-txt --nosave --name micro """