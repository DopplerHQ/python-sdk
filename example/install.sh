python -m venv env
source env/bin/activate
pip install build
python -m build --outdir dist ../ 
pip install dist/doppler_sdk-1.0.0-py3-none-any.whl
