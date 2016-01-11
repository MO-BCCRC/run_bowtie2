'''
Created on July 24, 2014
Last update July 24, 2014
@author: raniba
'''

import os

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Align two fastq files using Bowtie2 and generate a bam file
    '''
    def __init__(self, component_name='run_bowtie2', component_parent_dir=None, seed_dir=None):
        self.version = "1.0.3"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk):

        print chunk.split(":")[0]
        print chunk.split(":")[1]
        cmd_args[2] = chunk.split(":")[0]
        cmd_args[3] = chunk.split(":")[1]

        return cmd, cmd_args

    def make_cmd(self, chunk=None):
        '''
        Align Fastq Files and generate a Bam file
        '''

        bowtie2_runner = os.path.join(self.seed_dir, "run_bowtie2.sh")

        bowtie2_path = self.requirements['bowtie2']
        samtools_path = self.requirements['samtools']

        seq1 = self.args.seq1
        seq2 = self.args.seq2

        reference = self.args.reference
        outfile = self.args.outfile

        #seq1_base = os.path.basename(seq1)
        #seq2_base = os.path.basename(seq2)

        cmd = 'sh'
        cmd_args = [
            bowtie2_runner,
            reference,
            seq1,
            seq2,
            outfile,
            bowtie2_path,
            samtools_path
        ]

        #if chunk is not None:
        #    cmd, cmd_args = self.focus(cmd, cmd_args, chunk)

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    align_bowtie2_pe = Component()
    align_bowtie2_pe.args = component_ui.args
    align_bowtie2_pe.run()

if __name__ == '__main__':

    import component_ui

    _main()
