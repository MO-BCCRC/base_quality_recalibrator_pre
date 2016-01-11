'''
Created on Sep 09, 2014

@author: raniba
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    GATK RealignerTargetCreator : Create suspecious regions where a realignment will be done
    '''
    def __init__(self, component_name='bqsr_pre', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        GATK BaseRecalibrator (Pre)
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        bqsr_jar = self.requirements['gatk']
        bqsr_infile = self.args.infile
        bqsr_dbsnp = self.args.dbsnp
        bqsr_outfile = self.args.outfile
        bqsr_ref_genome = self.args.ref_genome

        cmd = self.requirements['java']
        cmd_args = [java_mem,
                    java_jar_option,
                    bqsr_jar,
                    "-T", "BaseRecalibrator",
                    "-R", bqsr_ref_genome,
                    "-knownSites", bqsr_dbsnp,
                    "-I", bqsr_infile,
                    "-o", bqsr_outfile]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    bqsr_pre = Component()
    bqsr_pre.args = component_ui.args
    bqsr_pre.run()

if __name__ == '__main__':

    import component_ui

    _main()
