FROM sagemathinc/cocalc:latest

# Install system packages
RUN apt install -y pandoc-citeproc cmake bamtools bedtools git gzip libcairo2 libcairo2-dev libx11-dev locate rna-star samtools tree xvfb libxt-dev build-essential build-essential procps curl file git

RUN apt install -y python3.8-full

# Setup the fix-r-path script
RUN echo "* * * * * /data/cocalc/fix-r-path.sh" > /etc/cron.d/fix-r-path
RUN chmod 755 /etc/cron.d/fix-r-path

# Fix jupyter symlink
RUN ln -s /usr/bin/jupyter /usr/local/bin/jupyter

# Install missing packages
RUN Rscript -e 'install.packages(c("Rcmdr", "renv", "sem", "rgl", "multcomp", "markdown", "lmtest", "leaps", "aplpack", "RcmdrPlugin.EZR", "RcmdrPlugin.FactoMineR"))'

# pip packages
RUN pip install sqlalchemy

# Install bash kernel
RUN pip3 install bash_kernel
RUN python3 -m bash_kernel.install
RUN chmod ugo+rx -R /usr/local/lib/python3.8/dist-packages/ /usr/local/share/jupyter/kernels/bash
