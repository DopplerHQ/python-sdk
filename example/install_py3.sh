python3 -m venv env
source env/bin/activate
pip3 install build
python3 -m build --outdir dist ../ 
pip3 install dist/doppler_sdk-1.0.0-py3-none-any.whl