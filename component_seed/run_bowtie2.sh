# Args:
#   [1] : REF_GENOME - Path to reference genome BAM file was aligned to
#   [2] : FASTQ_1 - First FASTQ with paired end data
#   [3] : FASTQ_2 - Second FASTQ with paired end data
#   [4] : OUT_FILE - Path where output will be written in BAM format

version='1.0.0'
REF_GENOME=$1

FASTQ_1=$2

FASTQ_2=$3

OUT_FILE=$4

bowtie2=$5
samtools=$6

#example
#-bash-3.2$ ./bowtie2 -I 0 -X 200 -p 8 -x genomes/GRCh37-lite -1 example/reads/reads_1.fq -2 example/reads/reads_2.fq --no-mixed --no-overlap --no-contain --no-discordant -S test.sam
#samtools view -bSh -o test.bam test.sam


#example
#./bowtie2 -I 100 -X 500 -p 8 -x genomes/GRCh37-lite --fr -1 example/reads/reads_1.fq -2 example/reads/reads_2.fq -S test.sam
#samtools view -bSh -o test.bam test.sam



reads1=${FASTQ_1##*/}
reads_1_base=${reads1%.*}

reads2=${FASTQ_2##*/}
reads_2_base=${reads2%.*}


#$REF_GENOME for test on genesis /extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite

$bowtie2 -I 100 -X 500 -p 8 -x $REF_GENOME --fr -1 $FASTQ_1 -2 $FASTQ_2 -S $reads_1_base$reads_2_base.sam

$samtools view -Sb $reads_1_base$reads_2_base.sam -o $OUT_FILE


if [ -f $reads_1_base$reads_2_base.sam ]
then
  rm $reads_1_base$reads_2_base.sam
fi
