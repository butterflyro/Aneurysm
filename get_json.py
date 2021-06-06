from collections import OrderedDict
# from nnunet.paths import nnUNet_raw_data
from batchgenerators.utilities.file_and_folder_operations import *
import shutil
import SimpleITK as sitk

# folder = os.listdir("adam")
# def convert_for_submission(source_dir, target_dir):
#     """
#     I believe they want .nii, not .nii.gz
#     :param source_dir:
#     :param target_dir:
#     :return:
#     """
#     files = subfiles(source_dir, suffix=".nii.gz", join=False)
#     maybe_mkdir_p(target_dir)
#     for f in files:
#         img = sitk.ReadImage(join(source_dir, f))
#         out_file = join(target_dir, f[:-7] + ".nii")
#         sitk.WriteImage(img, out_file)



if __name__ == "__main__":


    img_tr = os.listdir("/content/drive/MyDrive/ADAM_thay_Hung/ADAM2020/nnUNet/data/nnUNet_raw_data/Task100_ADAM/imagesTr")
    # img_ts = os.listdir("/content/drive/MyDrive/ADAM_thay_Hung/ADAM2020/nnUNet/data/nnUNet_raw_data/Task100_ADAM/imagesTs")

    json_dict = OrderedDict()
    json_dict['name'] = "Aneurysm Detection And segMentation Challenge"
    json_dict['description'] = "Aneurysm Detection And segMentation Challenge"
    json_dict['tensorImageSize'] = "3D"
    json_dict['reference'] = "see challenge website"
    json_dict['licence'] = "see challenge website"
    json_dict['release'] = "0.0"
    json_dict['modality'] = {
        "0": "3D TOF-MRA",
    }
    json_dict['labels'] = {
        "0": "background",
        "1": "Untreated, unruptured aneurysm",
    }
    json_dict['numTraining'] = len(img_tr)
    json_dict['numTest'] = len(img_ts)
    print(len(img_tr))
    print(len(img_ts))
    for i in img_tr:
      print(i)
    json_dict['training']= [{'image':"./imagesTr/ADAM_%s.nii.gz" % i[5:8], "label":"./labelsTr/ADAM_%s.nii.gz" % i[5:8]} for i in img_tr]
    json_dict['test'] = []

    save_json(json_dict, os.path.join("", "dataset.json"))