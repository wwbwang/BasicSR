from os import path as osp
from PIL import Image
import os

from basicsr.utils import scandir

# generate a  txt file which records information of LR & HR datasets for training
# TODO LR TIFF is 16bit, while HR TIFF is 8bit. (not sure)

def generate_meta_info_div2k():
    """Generate meta info for DIV2K dataset.
    """

    gt_folder = '../../datasets/BioSR/F-actin/F-actin_output/subtestHR/'
    meta_info_txt = '../../basicsr/data/meta_info/001_MSRResNet_x2_f64b16_DIV2K_1000k_B16G1_wandb.txt'

    img_list = sorted(list(scandir(gt_folder)))

    with open(meta_info_txt, 'w') as f:
        for idx, img_path in enumerate(img_list):
            img = Image.open(osp.join(gt_folder, img_path))  # lazy load
            width, height = img.size
            mode = img.mode
            if mode == 'RGB':
                n_channel = 3
            elif mode == 'L':
                n_channel = 1
            # 16bit TIFF
            elif mode == 'I;16':
                n_channel = 1
            else:
                raise ValueError(f'Unsupported mode {mode}.')

            info = f'{img_path} ({height},{width},{n_channel})'
            print(idx + 1, info)
            f.write(f'{info}\n')


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    generate_meta_info_div2k()
