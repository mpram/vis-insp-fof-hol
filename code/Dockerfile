FROM rpiguru/docker-python3-opencv-arm:aarch64-latest

RUN apt-get update -y

RUN apt-get upgrade -y

RUN apt-get install gfortran -y

RUN apt-get install libhdf5-dev libc-ares-dev libeigen3-dev -y

RUN apt-get install libatlas-base-dev libopenblas-dev libblas-dev -y

RUN apt-get install liblapack-dev -y

RUN pip install pybind11

RUN pip install Cython==0.29.21

RUN pip install h5py==2.10.0

RUN pip install --upgrade setuptools

RUN pip install gdown

RUN gdown https://drive.google.com/uc?id=1fR9lsi_bsI_npPFB-wZyvgjbO0V9FbMf

RUN pip install tensorflow-2.2.0-cp37-cp37m-linux_aarch64.whl

RUN pip install Pillow

RUN pip install azure-iot-device

RUN pip install imutils

RUN pip install flask



COPY FlashModel/ /FlashModel



CMD ["tail","-f","/dev/null"]
