import json
import numpy as np
from voc.voc import pascal_voc
'''
off-line evaluation code
1. ./voc/extract_image_set: extract images to certain directory
2. run inference engine and collect the output files
   - [[xmin, ymin, xmax, xmax, class_id]..] num_image * (num_object * 5)
3. all_boxes[num_classes][num_images] 
'''

def main():
    evaluator = pascal_voc(root='/ssd/data/VOCdevkit',
               image_set='test',
               year='2007')
    id_lists = evaluator._image_index
    num_classes = len(evaluator._classes)
    all_boxes = [[[] for _ in range(len(id_lists))] for _ in range(num_classes)]

    #------------------ load all_boxes here------------------------------
    json_file = '/home/xiangyuzhu/workspace/detections/models/research/object_detection/output/results.json'
    #json_file = 'temp.json'
    with open(json_file) as f:
        preds = json.load(f)
    for k, v in preds.items():
        id = id_lists.index(k)
        objs = np.array(preds[k]['bbox'])
        classes = np.array(preds[k]['cls'])
        # for i in range(num_classes):
        #     all_boxes[i][id] = objs[classes==i]
        all_boxes[15][id] = objs[classes == 1] ## coco person to voc
    #--------------------------------------------------------------------
    evaluator.evaluate_detections(all_boxes, './')


if __name__ == '__main__':
    main()
