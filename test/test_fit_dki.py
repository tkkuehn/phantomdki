import unittest

from dmriphantomutils import fit_dki
from test import test_data

class TestFitDki(unittest.TestCase):
    def testMain(self):
        test_nifti_path = test_data.get_data_nifti()
        test_bval_path = test_data.get_data_bval()
        test_bvec_path = test_data.get_data_bvec()
        test_mask_path = test_data.get_data_mask_nifti()
        test_fa_path = test_data.get_temp_output_nifti()
        fit_dki.main(test_nifti_path, test_bval_path, test_bvec_path,
                     mask_path=test_mask_path, blur=True, fa_path=test_fa_path)
