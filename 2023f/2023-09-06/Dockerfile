FROM ubuntu:22.04
RUN apt update && apt install -y git fish emacs build-essential sudo man-db curl golang

RUN adduser --disabled-password --gecos '' sam && \
	adduser sam sudo && \
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER sam
WORKDIR /home/sam
RUN git clone -c feature.manyFiles=true https://github.com/spack/spack.git \
	&& echo '\nsource ~/spack/share/spack/setup-env.sh' >> ~/.bashrc
RUN git clone --branch stable https://github.com/nojhan/liquidprompt.git ~/liquidprompt \
	&&  echo '\nsource ~/liquidprompt/liquidprompt' >> ~/.bashrc
RUN mkdir -p ~/.local/bin \
	&& echo '\nexport PATH=${HOME}/.local/bin:${PATH}' >> ~/.bashrc
ENV PATH=/home/sam/.local/bin:${PATH}
RUN curl -sfL https://direnv.net/install.sh | bash \
	&& echo '\neval "$(direnv hook bash)"' >> ~/.bashrc
RUN bash -c "source ~/spack/share/spack/setup-env.sh && spack env create myenv && spack env activate myenv && spack install --add pigz"
RUN git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
