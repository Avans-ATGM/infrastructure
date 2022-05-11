FROM sagemathinc/cocalc:08fa3bbfaeaa54612d5d715f6ea5d5c072670db3ad553958906c5762ef142b94

# Install system packages
RUN apt install pandoc-citeproc cmake bamtools bedtools cairo2 git gzip libcairo2 libcairo2-dev libx11-dev locate pip python3-virtuelenv rna-star samtools tree xvfb brew libxt-dev python3-pip build-essential build-essential procps curl file git python3-pip

# Setup the fix-r-path script
RUN echo "* * * * * /data/cocalc/fix-r-path.sh" > /etc/cron.d/fix-r-path
RUN chmod 755 /etc/cron.d/fix-r-path

# Fix jupyter symlink
RUN ln -s /usr/bin/jupyter /usr/local/bin/jupyter

# Install missing packages
RUN Rscript -e 'install.packages(c("Rcmdr", "renv", "sem", "rgl", "multcomp", "markdown", "lmtest", "leaps", "aplpack", "RcmdrPlugin.EZR", "RcmdrPlugin.FactoMineR"))'

# pip packages
RUN pip install sqlalchemy
