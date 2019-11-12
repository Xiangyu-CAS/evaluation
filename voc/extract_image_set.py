import os
import os.path as osp
import shutil

def main():
    src_image_dir = '/ssd/data/VOCdevkit/VOC2007/JPEGImages'
    list_file = '/ssd/data/VOCdevkit/VOC2007/ImageSets/Main/debug.txt'
    dst_image_dir = '/ssd/data/VOCdevkit/test_images_voc2007'
    with open(list_file) as f:
        image_index = [x.strip() for x in f.readlines()]

    for id in image_index:
        src_path = osp.join(src_image_dir, str(id) + '.jpg')
        dst_path = osp.join(dst_image_dir, str(id) + '.jpg')
        shutil.copy(src_path, dst_path)

if __name__ == '__main__':
    main()