FROM sagemathinc/cocalc:latest

# Install system packages
RUN apt install -y pandoc-citeproc cmake bamtools bedtools git gzip libcairo2 libcairo2-dev libx11-dev locate pip rna-star samtools tree xvfb libxt-dev python3-pip build-essential build-essential procps curl file git python3-pip

# Setup the fix-r-path script
RUN echo "* * * * * /data/cocalc/fix-r-path.sh" > /etc/cron.d/fix-r-path
RUN chmod 755 /etc/cron.d/fix-r-path

# Fix jupyter symlink
RUN ln -s /usr/bin/jupyter /usr/local/bin/jupyter

# Install missing packages
RUN Rscript -e 'install.packages(c("Rcmdr", "renv", "sem", "rgl", "multcomp", "markdown", "lmtest", "leaps", "aplpack", "RcmdrPlugin.EZR", "RcmdrPlugin.FactoMineR"))'

# pip packages
RUN pip install sqlalchemy
