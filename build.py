from pybuilder.core import init, task, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")

default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('mockito')

@task
def test(logger):
   logger.info("Hello, PyBuilder")
