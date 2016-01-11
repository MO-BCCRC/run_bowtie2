#run_bowtie2 : Paired Ends Alignment using Bowtie2

```
Development information

date created : July 24 2014
last update  : Oct 6  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Fastq files (R1 and R2), reference genome
Output       : Bam file
Seed used    : Bowtie2

```

###Usage
This component is using Bowtie2 to do a paired end reads alignment, for more information about the command called you can refer to the seed or to the component_main.py of this repo
This implementation is limiting read lengths to min 100bp and max 500bp, if your analysis requires more flexibility, please set bowtie2 -I option to 0 (no min) and increase the -X 

###Dependencies

- Bowtie2
- python
- samtools


###Example

Calling the component is easy. The seed is a simple shell script that takes 2 fastq files and a reference geneome file, produces a sam files and convert the sam file into a bam file using samtools.

> You need to index the reference genome using bowtie2 

```
# Args:
#   [1] : REF_GENOME - Path to reference genome BAM file was aligned to
#   [2] : FASTQ_1 - First FASTQ with paired end data
#   [3] : FASTQ_2 - Second FASTQ with paired end data
#   [4] : OUT_FILE - Path where output will be written in BAM format


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


REF_GENOME=$1

FASTQ_1=$2

FASTQ_2=$3

OUT_FILE=$4


reads1=${FASTQ_1##*/}
reads_1_base=${reads1%.*}

reads2=${FASTQ_2##*/}
reads_2_base=${reads2%.*}


#$REF_GENOME for test on genesis /extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite

bowtie2 -I 100 -X 500 -p 8 -x $REF_GENOME --fr -1 $FASTQ_1 -2 $FASTQ_2 -S $reads_1_base$reads_2_base.sam

samtools view -Sb $reads_1_base$reads_2_base.sam -o $OUT_FILE


if [ -f $reads_1_base$reads_2_base.sam ]
then 
  rm $reads_1_base$reads_2_base.sam
fi

```


###Known issues



###Last updates



### test data
Reference : /genesis/extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite   
seq1 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R1_001.fastq 
seq2 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R2_001.fastq  
outfile : test.bam   

bowtie2 path : /genesis/extscratch/shahlab/raniba/Software/bowtie2/  
samtools path : /extscratch/shahlab/raniba/pipelines/miseq_pipeline/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools 


