python -m venv .venv
source .venv/bin/activate
pip install build
python -m build --outdir dist ../ 
pip install dist/doppler_sdk-1.2.1-py3-none-any.whl
