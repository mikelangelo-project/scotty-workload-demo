import logging

from scotty import utils

logger = logging.getLogger(__name__)

def run(context):
    workload = context.v1.workload
    exp_helper = utils.ExperimentHelper(context)
    logger.info('{}'.format(workload.params['greeting']))
    logger.info('I\'m workload generator {}'.format(workload.name))

def collect(context):
    workload_utils = utils.WorkloadUtils(context)
    with workload_utils.open_file('my_result.txt', 'w+') as f:
        f.write('my result content')

def clean(context):
    pass
