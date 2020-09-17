# Cleanup
rm build -R
rm dist -R
rm ssw_aligner.egg-info -R

# Creating distribution
python3 setup.py bdist_wheel

# Installing Locally
python3 -m pip install dist/ssw_aligner-0.0.9-cp37-cp37m-linux_x86_64.whl --user --upgrade
#pip install dist/ssw_aligner-0.0.9-cp37-cp37m-linux_x86_64.whl --user

