python3 -m venv .venv
source .venv/bin/activate
pip3 install build
python3 -m build --outdir dist ../ 
pip3 install dist/doppler_sdk-1.2.0-py3-none-any.whl