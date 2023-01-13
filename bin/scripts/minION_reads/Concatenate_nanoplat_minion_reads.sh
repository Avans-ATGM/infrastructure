#Only for Barcoded DNA runs

for folder in 2022-011;do for barcode in $folder/*/no_sample/*/fastq_pass/barcode?? $folder/*/no_sample/*/fastq_pass/unclassified ;do zcat $barcode/*.fastq.gz > $(echo $barcode|cut -f1 -d/)/$(echo $barcode|cut -f1 -d/)-$(echo $barcode|cut -f6 -d/)-$(echo $barcode|cut -f5 -d/).fastq && gzip $(echo $barcode|cut -f1 -d/)/$(echo $barcode|cut -f1 -d/)-$(echo $barcode|cut -f6 -d/)-$(echo $barcode|cut -f5 -d/).fastq && NanoPlot --threads 12 --outdir $(echo $barcode|cut -f1 -d/)/NanoPlot/$(echo $barcode|cut -f1 -d/)-$(echo $barcode|cut -f6 -d/) --N50 --title $(echo $barcode|cut -f1 -d/)/$(echo $barcode|cut -f1 -d/)-$(echo $barcode|cut -f6 -d/)-$(echo $barcode|cut -f5 -d/) --fastq $(echo $barcode|cut -f1 -d/)/$(echo $barcode|cut -f1 -d/)-$(echo $barcode|cut -f6 -d/)-$(echo $barcode|cut -f5 -d/).fastq.gz;done;done


for folder in 2022-016;do pycoQC --quiet -f $folder/*/no_sample/*/sequencing_summary_*.txt -o $folder/pycoQC_$folder.html && cp $folder/*/no_sample/*/report_*.html $folder/Report_$folder.html;done

