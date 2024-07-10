FROM nvidia/cuda:12.5.0-devel-ubuntu22.04

LABEL com.nvidia.volumes.needed="nvidia_driver"

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

RUN apt-get update && apt-get install -y --no-install-recommends \
    ocl-icd-libopencl1 \
    ca-certificates \
    python3 \
    curl \
    wget \
    pciutils \
    zip \
    python3-pip \
    git \
    python3-psutil \
    python3-requests \
    clinfo \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN update-pciids && rm -rf /var/lib/apt/lists/*

WORKDIR /root/agent-python

RUN git clone https://github.com/hashtopolis/agent-python.git && cd agent-python && pip3 install -r requirements.txt && ./build.sh

COPY entrypoint.sh /root/entrypoint.sh

# Make scripts executable
RUN chmod +x /root/entrypoint.sh

ENTRYPOINT ["/root/entrypoint.sh"]
